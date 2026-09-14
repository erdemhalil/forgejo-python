"""Package-layout checks: the importable public and generator packages and the shipped ``py.typed`` marker."""

from __future__ import annotations

from pathlib import Path

import codegen
import pyfj


def test_package_is_importable() -> None:
    assert pyfj.__name__ == "pyfj"


def test_py_typed_marker_is_shipped() -> None:
    package_dir = Path(pyfj.__file__ or "").parent
    assert (package_dir / "py.typed").is_file()


def test_codegen_package_is_importable() -> None:
    """`import codegen` works because pyproject points pytest's `pythonpath` at the repo root."""
    assert codegen.__name__ == "codegen"
