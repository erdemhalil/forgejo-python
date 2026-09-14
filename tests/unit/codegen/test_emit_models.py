"""Golden-file, determinism, and hygiene tests for the model emitter."""

from __future__ import annotations

import ast
from pathlib import Path
from typing import TYPE_CHECKING

from codegen.__main__ import generate
from codegen.emit_models import emit_models, render_init, render_module

if TYPE_CHECKING:
    from collections.abc import Callable

    from codegen.ir import IR

MINI_SPEC_PATH = Path(__file__).parent / "data" / "mini_spec.json"
MINI_MAPPING_PATH = Path(__file__).parent / "data" / "mini_mapping.toml"
GOLDEN_DIR = Path(__file__).parent / "golden"


def _golden_modules() -> dict[str, bytes]:
    files = sorted(GOLDEN_DIR.glob("*.py"))
    return {path.name: path.read_bytes() for path in files}


def test_golden_files(
    mini_ir: IR, tmp_path: Path, repo_root: Path, read_modules: Callable[[Path], dict[str, bytes]]
) -> None:
    models_dir = tmp_path / "models"
    written = generate(
        root=repo_root,
        spec_path=MINI_SPEC_PATH,
        models_dir=models_dir,
        api_dir=tmp_path / "api",
        mapping_path=MINI_MAPPING_PATH,
        registry_path=tmp_path / "registry.toml",
        report_path=tmp_path / "naming-report.md",
    )
    generated = read_modules(models_dir)
    golden = _golden_modules()
    assert set(generated) == set(golden)
    assert [name for name in sorted(golden) if generated[name] != golden[name]] == []
    models_written = [path for path in written if path.parent == models_dir]
    assert len(models_written) == len(mini_ir.types) + 1  # one module per type plus __init__


def test_generation_is_deterministic(
    tmp_path: Path, repo_root: Path, read_modules: Callable[[Path], dict[str, bytes]]
) -> None:
    first = generate(
        root=repo_root,
        spec_path=MINI_SPEC_PATH,
        models_dir=tmp_path / "first",
        api_dir=tmp_path / "first_api",
        mapping_path=MINI_MAPPING_PATH,
        registry_path=tmp_path / "first_registry.toml",
        report_path=tmp_path / "first_report.md",
    )
    second = generate(
        root=repo_root,
        spec_path=MINI_SPEC_PATH,
        models_dir=tmp_path / "second",
        api_dir=tmp_path / "second_api",
        mapping_path=MINI_MAPPING_PATH,
        registry_path=tmp_path / "second_registry.toml",
        report_path=tmp_path / "second_report.md",
    )
    assert read_modules(first[0].parent) == read_modules(second[0].parent)


def test_stale_modules_are_removed(tmp_path: Path, repo_root: Path) -> None:
    models_dir = tmp_path / "models"
    models_dir.mkdir()
    stale = models_dir / "stale.py"
    stale.write_text("STALE = True\n", encoding="utf-8")
    generate(
        root=repo_root,
        spec_path=MINI_SPEC_PATH,
        models_dir=models_dir,
        api_dir=tmp_path / "api",
        mapping_path=MINI_MAPPING_PATH,
        registry_path=tmp_path / "registry.toml",
        report_path=tmp_path / "naming-report.md",
    )
    assert not stale.exists()


def test_written_modules_never_import_the_api(mini_ir: IR, tmp_path: Path) -> None:
    for path in emit_models(mini_ir, tmp_path):
        text = path.read_text(encoding="utf-8")
        assert "_generated.api" not in text
        assert "from pyfj._generated import api" not in text


def test_init_reexports_every_generated_type(mini_ir: IR, tmp_path: Path) -> None:
    emit_models(mini_ir, tmp_path)
    init = (tmp_path / "__init__.py").read_text(encoding="utf-8")
    for name in mini_ir.types_by_name:
        assert f'"{name}"' in init


def test_render_module_is_pure(mini_ir: IR) -> None:
    for type_def in mini_ir.types:
        first = render_module(type_def)
        assert first == render_module(type_def)
        assert first.endswith("\n")


def test_render_init_is_deterministic(mini_ir: IR) -> None:
    assert render_init(mini_ir) == render_init(mini_ir)


def test_render_module_has_no_api_imports(mini_ir: IR) -> None:
    for type_def in mini_ir.types:
        assert "_generated.api" not in render_module(type_def)


def test_wrapped_docstrings_keep_every_word(mini_ir: IR) -> None:
    type_def = mini_ir.types_by_name["WrappedDoc"]
    assert type_def.description is not None
    tree = ast.parse(render_module(type_def))
    class_node = next(node for node in tree.body if isinstance(node, ast.ClassDef) and node.name == "WrappedDoc")
    docstring = ast.get_docstring(class_node)
    assert docstring is not None
    assert " ".join(docstring.split()) == " ".join(type_def.description.split())
    for field in type_def.fields:
        if field.description is None:
            continue
        statement = next(
            node
            for node in class_node.body
            if isinstance(node, ast.AnnAssign) and getattr(node.target, "id", "") == field.name
        )
        assert isinstance(statement.value, ast.Call)
        keyword = next(keyword for keyword in statement.value.keywords if keyword.arg == "description")
        assert ast.literal_eval(keyword.value) == " ".join(field.description.split())
