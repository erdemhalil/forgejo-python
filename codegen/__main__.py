"""``python -m codegen``: regenerate pyfj's generated surface from the Spec.

The runner locates the repository root, loads ``spec/openapi.json``, builds
the IR from ``mapping.toml``'s model overrides, and emits the generated tree
(models, API namespaces, and the naming report) before formatting everything
with ruff. It is deterministic: the same Spec and overrides produce
byte-identical output.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path
from typing import TYPE_CHECKING

from codegen.emit_api import emit_api
from codegen.emit_models import emit_models
from codegen.ir import build_ir
from codegen.naming import load_mapping, load_registry
from codegen.spec import load_spec

if TYPE_CHECKING:
    from collections.abc import Sequence

__all__ = ["find_root", "format_paths", "generate", "main"]

SPEC_PATH = Path("spec") / "openapi.json"
MODELS_PATH = Path("src") / "pyfj" / "_generated" / "models"
API_PATH = Path("src") / "pyfj" / "_generated" / "api"
MAPPING_PATH = Path("codegen") / "mapping.toml"
REGISTRY_PATH = Path("codegen") / "registry.toml"
REPORT_PATH = Path("codegen") / "naming-report.md"


def find_root(start: Path | None = None) -> Path:
    """Return the repository root by walking up from ``start`` (or this file) to a ``pyproject.toml``."""
    current = (start or Path(__file__)).resolve()
    if current.is_file():
        current = current.parent
    for candidate in (current, *current.parents):
        if (candidate / "pyproject.toml").is_file():
            return candidate
    message = f"could not locate the pyfj repository root from {current}: no pyproject.toml found"
    raise FileNotFoundError(message)


def generate(
    *,
    root: Path | None = None,
    spec_path: Path | None = None,
    models_dir: Path | None = None,
    api_dir: Path | None = None,
    mapping_path: Path | None = None,
    registry_path: Path | None = None,
    report_path: Path | None = None,
) -> list[Path]:
    """Regenerate the models, API, and naming-report trees.

    Returns the written Python module paths (the naming report is written but
    not formatted or returned). ``root`` defaults to the located repository
    root and anchors the ruff configuration; the other paths default to their
    repository locations and are overridable for tests.
    """
    repository = (root or find_root()).resolve()
    spec = load_spec(spec_path or repository / SPEC_PATH)
    mapping = load_mapping(mapping_path or repository / MAPPING_PATH)
    registry = load_registry(registry_path or repository / REGISTRY_PATH)
    ir = build_ir(spec, model_names=mapping.models)
    written = emit_models(ir, models_dir or repository / MODELS_PATH)
    written.extend(
        emit_api(
            ir,
            api_dir or repository / API_PATH,
            mapping=mapping,
            registry=registry,
            report_path=report_path or repository / REPORT_PATH,
        )
    )
    format_paths(written, root=repository)
    return written


def format_paths(paths: Sequence[Path], *, root: Path) -> None:
    """Format generated files with the repository's ruff configuration."""
    if not paths:
        return
    command = [
        sys.executable,
        "-m",
        "ruff",
        "format",
        "--config",
        str(root / "pyproject.toml"),
        *(str(path) for path in paths),
    ]
    subprocess.run(command, cwd=root, check=True, shell=False)  # noqa: S603 - fixed argument list, no shell


def main(argv: Sequence[str] | None = None) -> int:
    """CLI entry point; reports progress on stdout (the library itself never prints)."""
    parser = argparse.ArgumentParser(
        prog="python -m codegen",
        description="Regenerate pyfj's models and API surface from spec/openapi.json.",
    )
    parser.parse_args(argv)
    repository = find_root()
    written = generate(root=repository)
    sys.stdout.write(f"generated {len(written)} files\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
