"""Acceptance tests against the committed API tree and public exports.

Pins the API-generation criteria: every operation is generated (or excluded with a
reason), the committed ``_generated/api`` tree matches the generator, every
method docstring carries its operationId, and ``pyfj`` re-exports the
clients, errors, and every model.
"""

from __future__ import annotations

import ast
import inspect
import re
from typing import TYPE_CHECKING

import pyfj
from codegen.__main__ import generate
from pyfj import models
from pyfj._generated.api import AsyncForgejo, Forgejo

if TYPE_CHECKING:
    from collections.abc import Callable
    from pathlib import Path

    from codegen.ir import IR
    from codegen.naming import Naming
    from codegen.spec import Spec

_API_DIR_PARTS = ("src", "pyfj", "_generated", "api")
_OPERATION_ID = re.compile(r"Operation ID: (\S+)")
_DOC_ENTRY = re.compile(r"^ {4}\w[\w_]*:")


def _api_dir(repo_root: Path) -> Path:
    return repo_root.joinpath(*_API_DIR_PARTS)


def test_completeness_over_the_real_spec(real_naming: Naming, real_spec: Spec) -> None:
    expected = {operation.operation_id for path in real_spec.paths for operation in path.operations}
    generated = {endpoint.operation.operation_id for endpoint in real_naming.endpoints}
    excluded = {operation.operation_id for operation, _ in real_naming.exclusions}
    assert len(expected) == 506
    assert generated | excluded == expected
    assert generated & excluded == set()
    assert len(generated) == 505
    assert excluded == {"getActionsRun"}


def test_top_level_namespace_counts(real_naming: Naming) -> None:
    counts: dict[str, int] = {}
    for endpoint in real_naming.endpoints:
        counts[endpoint.namespace[0]] = counts.get(endpoint.namespace[0], 0) + 1
    assert counts == {
        "repos": 264,
        "user": 66,
        "users": 17,
        "orgs": 53,
        "teams": 12,
        "admin": 51,
        "notifications": 5,
        "packages": 6,
        "settings": 4,
        "activitypub": 11,
        "misc": 16,
    }


def test_committed_api_tree_matches_the_generator(
    real_ir: IR, repo_root: Path, tmp_path: Path, read_modules: Callable[[Path], dict[str, bytes]]
) -> None:
    generate(
        root=repo_root,
        models_dir=tmp_path / "models",
        api_dir=tmp_path / "api",
        report_path=tmp_path / "naming-report.md",
    )
    assert read_modules(tmp_path / "api") == read_modules(_api_dir(repo_root))


def test_every_method_docstring_binds_its_operation_id(real_naming: Naming, repo_root: Path) -> None:
    expected = {endpoint.operation.operation_id for endpoint in real_naming.endpoints}
    found: set[str] = set()
    for path in sorted(_api_dir(repo_root).glob("*.py")):
        tree = ast.parse(path.read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            docstring = ast.get_docstring(node)
            if docstring is None:
                continue
            match = _OPERATION_ID.search(docstring)
            if match is not None:
                found.add(match.group(1))
    assert found == expected


def test_docstring_omits_returns_when_the_spec_has_no_description(repo_root: Path) -> None:
    """repoCompareDiff's response has no Spec description, so there is no type-only Returns line."""
    found = False
    for path in sorted(_api_dir(repo_root).glob("*.py")):
        tree = ast.parse(path.read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            docstring = ast.get_docstring(node)
            if docstring is not None and "Operation ID: repoCompareDiff" in docstring:
                found = True
                assert "Returns:" not in docstring
    assert found


def test_docstring_entry_continuations_are_indented_below_the_entry(repo_root: Path) -> None:
    """A wrapped ``Args``/``Raises`` continuation at entry indent is read as a new entry, then dropped."""
    headers = {"Args:", "Returns:", "Raises:", "Deprecated:"}
    checked = 0
    for path in sorted(_api_dir(repo_root).glob("*.py")):
        tree = ast.parse(path.read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            docstring = ast.get_docstring(node)
            if docstring is None:
                continue
            section = ""
            for line in inspect.cleandoc(docstring).splitlines():
                if line in headers:
                    section = line
                    continue
                if section not in {"Args:", "Raises:"} or not line:
                    continue
                if line.startswith("Operation ID:"):
                    section = ""
                    continue
                if _DOC_ENTRY.match(line):
                    checked += 1
                    continue
                leading = len(line) - len(line.lstrip(" "))
                assert leading > 4, (path, node.name, line)
    assert checked > 0


def test_generated_api_never_imports_httpx2(repo_root: Path) -> None:
    for path in _api_dir(repo_root).glob("*.py"):
        text = path.read_text(encoding="utf-8")
        assert "import httpx2" not in text
        assert "import httpx" not in text


def test_generated_api_needs_no_casts_or_ty_ignores(repo_root: Path) -> None:
    """Requiredness is carried by the signature, so bodies need no `cast(...)`."""
    for path in _api_dir(repo_root).glob("*.py"):
        text = path.read_text(encoding="utf-8")
        assert "cast(" not in text, path
        assert "ty: ignore" not in text, path


def test_sync_and_async_clients_build_namespaces() -> None:
    client = pyfj.Forgejo("https://example.test")
    try:
        assert client.repos.issues is not None
        assert client.repos.issues.comments is not None
        assert client.user.emails is not None
        assert callable(client.repos.issues.comments.list)
    finally:
        client.close()


async def test_async_client_builds_namespaces() -> None:
    client = pyfj.AsyncForgejo("https://example.test")
    try:
        assert client.repos.issues is not None
        assert callable(client.repos.issues.comments.list)
        assert callable(client.admin.users.list)
    finally:
        await client.aclose()


def test_every_model_is_exported_from_pyfj_and_pyfj_models() -> None:
    assert models.__all__
    for name in models.__all__:
        assert name in pyfj.__all__
        assert hasattr(pyfj, name)
        assert getattr(pyfj.models, name) is getattr(models, name)
    # One deliberate shadow: the Spec has an ``APIError`` model, but the
    # documented ``pyfj.APIError`` is the runtime exception.
    assert pyfj.APIError is not models.APIError
    assert pyfj.models.APIError is models.APIError


def test_public_exports_are_unique() -> None:
    assert len(pyfj.__all__) == len(set(pyfj.__all__))
    assert pyfj.__all__.count("APIError") == 1


def test_runtime_exports_are_public() -> None:
    for name in ("APIError", "AsyncForgejo", "AsyncPaginated", "Forgejo", "ForgejoError", "Paginated"):
        assert name in pyfj.__all__
        assert hasattr(pyfj, name)


def test_clients_are_the_generated_subclasses() -> None:
    assert pyfj.Forgejo is Forgejo
    assert pyfj.AsyncForgejo is AsyncForgejo
