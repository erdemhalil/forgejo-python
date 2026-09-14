"""Acceptance tests against the committed ``_generated/models`` tree.

These tests pin the model-generation criteria: all 246 definitions are emitted,
models parse representative fixtures, two generator runs are byte-identical,
and generated models never import from ``_generated.api``.
"""

from __future__ import annotations

import ast
from typing import TYPE_CHECKING

import pytest
from pydantic import BaseModel, ValidationError

from codegen.__main__ import generate
from codegen.ir import ListType, MapType, NamedRef, iter_types
from pyfj._generated import models

if TYPE_CHECKING:
    from collections.abc import Callable, Iterator
    from pathlib import Path

    from codegen.ir import IR, TypeExpr


def _walk_refs(expr: TypeExpr) -> Iterator[str]:
    if isinstance(expr, NamedRef):
        yield expr.name
    elif isinstance(expr, (ListType, MapType)):
        yield from _walk_refs(expr.item if isinstance(expr, ListType) else expr.value)


def test_every_named_reference_resolves(real_ir: IR) -> None:
    known = set(real_ir.types_by_name)
    missing: set[str] = set()
    for type_def in real_ir.types:
        for node in iter_types(type_def):
            for field in node.fields:
                missing.update(name for name in _walk_refs(field.type) if name not in known)
            if node.alias_target is not None:
                missing.update(name for name in _walk_refs(node.alias_target) if name not in known)
    for operation in real_ir.operations:
        types: list[TypeExpr] = [parameter.type for parameter in operation.parameters]
        if operation.body is not None:
            types.append(operation.body.type)
        types.extend(response.type for response in operation.responses if response.type is not None)
        for expr in types:
            missing.update(name for name in _walk_refs(expr) if name not in known)
    assert missing == set()


def _models_dir(repo_root: Path) -> Path:
    return repo_root / "src" / "pyfj" / "_generated" / "models"


def test_all_definitions_are_emitted(real_ir: IR, repo_root: Path) -> None:
    assert len(real_ir.definitions) == 246
    assert len(real_ir.types) == 249  # 246 definitions + 3 inline response models
    committed = {path.stem for path in _models_dir(repo_root).glob("*.py")}
    assert committed == {type_def.module for type_def in real_ir.types} | {"__init__"}


def test_generator_runs_are_byte_identical(
    real_ir: IR, repo_root: Path, tmp_path: Path, read_modules: Callable[[Path], dict[str, bytes]]
) -> None:
    first_dir = tmp_path / "first"
    second_dir = tmp_path / "second"
    common = {
        "root": repo_root,
        "mapping_path": repo_root / "codegen" / "mapping.toml",
        "registry_path": repo_root / "codegen" / "registry.toml",
    }
    generate(
        **common,
        models_dir=first_dir,
        api_dir=tmp_path / "first_api",
        report_path=tmp_path / "first_report.md",
    )
    generate(
        **common,
        models_dir=second_dir,
        api_dir=tmp_path / "second_api",
        report_path=tmp_path / "second_report.md",
    )
    assert read_modules(first_dir) == read_modules(second_dir)


def test_committed_tree_matches_the_generator(
    real_ir: IR, repo_root: Path, tmp_path: Path, read_modules: Callable[[Path], dict[str, bytes]]
) -> None:
    generated_dir = tmp_path / "generated"
    generate(
        root=repo_root,
        models_dir=generated_dir,
        api_dir=tmp_path / "api",
        report_path=tmp_path / "naming-report.md",
    )
    assert read_modules(generated_dir) == read_modules(_models_dir(repo_root))


def test_every_docstring_and_field_description_is_preserved(real_ir: IR) -> None:
    """No Spec description may lose words to wrapping/escaping (regression: docstring truncation)."""
    for type_def in real_ir.types:
        for node in iter_types(type_def):
            if node.kind != "model":
                continue
            model = getattr(models, node.name)
            if node.description:
                assert model.__doc__ is not None
                assert " ".join(model.__doc__.split()) == " ".join(node.description.split())
            for field in node.fields:
                if field.description is None:
                    continue
                actual = " ".join(model.model_fields[field.name].description.split())
                assert actual == " ".join(field.description.split())


def test_models_never_import_from_the_api(repo_root: Path) -> None:
    for path in _models_dir(repo_root).glob("*.py"):
        text = path.read_text(encoding="utf-8")
        assert "_generated.api" not in text
        assert "from pyfj._generated import api" not in text


def test_committed_init_reexports_every_generated_type(real_ir: IR, repo_root: Path) -> None:
    init = (_models_dir(repo_root) / "__init__.py").read_text(encoding="utf-8")
    tree = ast.parse(init)
    imported: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom) and (node.module or "").startswith("pyfj._generated.models."):
            imported.update(alias.name for alias in node.names)
    assert imported == set(real_ir.types_by_name)
    exported = next(
        ast.literal_eval(node.value)
        for node in tree.body
        if isinstance(node, ast.Assign) and any(getattr(target, "id", "") == "__all__" for target in node.targets)
    )
    assert sorted(exported) == sorted(imported)


def test_models_import_and_parse_fixtures() -> None:
    assert len(models.__all__) == 267

    repository = models.Repository.model_validate(
        {
            "id": 1,
            "name": "pyfj",
            "created_at": "2026-01-02T03:04:05Z",
            "owner": {"login": "erdem"},
            "extra_server_field": {"nested": True},
        }
    )
    assert repository.id == 1
    assert repository.created_at is not None
    assert repository.owner is not None
    assert repository.owner.login == "erdem"
    assert repository.model_extra == {"extra_server_field": {"nested": True}}

    activitypub = models.ActivityPub.model_validate({"@context": "https://www.w3.org/ns/activitystreams"})
    assert activitypub.context == "https://www.w3.org/ns/activitystreams"
    assert activitypub.model_dump(by_alias=True, exclude_none=True) == {
        "@context": "https://www.w3.org/ns/activitystreams"
    }

    contents = models.ContentsResponse.model_validate({"_links": {"self": "https://example.test/contents"}})
    assert contents.links is not None
    assert contents.links.self == "https://example.test/contents"

    merge = models.MergePullRequestOption.model_validate({"Do": "rebase-merge"})
    assert merge.do == models.MergePullRequestOptionDo.REBASE_MERGE
    assert merge.model_dump(by_alias=True, exclude_none=True) == {"Do": "rebase-merge"}

    attachment = models.QuotaUsedAttachment.model_validate({"contained_in": {"api_url": "https://example.test"}})
    assert attachment.contained_in is not None
    assert attachment.contained_in.api_url == "https://example.test"

    labels = models.IssueLabelsOption.model_validate({"labels": [1, "bug"]})
    assert labels.labels == [1, "bug"]

    hook = models.Hook.model_validate({"config": {"a": "b"}, "metadata": {"anything": 1}})
    assert hook.config == {"a": "b"}
    assert hook.metadata == {"anything": 1}


def test_required_fields_are_enforced() -> None:
    with pytest.raises(ValidationError):
        models.MergePullRequestOption.model_validate({})
    with pytest.raises(ValidationError):
        models.CreateHookOption.model_validate({})


def test_model_config_matches_the_architecture_rule() -> None:
    assert issubclass(models.Repository, BaseModel)
    assert models.Repository.model_config["extra"] == "allow"
    assert models.Repository.model_config["populate_by_name"] is True
