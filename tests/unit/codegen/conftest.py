"""Shared fixtures for the generator tests."""

from __future__ import annotations

import json
from pathlib import Path
from typing import TYPE_CHECKING, Any

import pytest

from codegen.__main__ import find_root
from codegen.ir import IR, build_ir
from codegen.naming import Naming, Overrides, Registry, assign_names, load_mapping, load_registry
from codegen.spec import Spec, load_spec

if TYPE_CHECKING:
    from collections.abc import Callable

CODEGEN_TESTS_DIR = Path(__file__).parent
MINI_SPEC_PATH = CODEGEN_TESTS_DIR / "data" / "mini_spec.json"
MINI_MAPPING_PATH = CODEGEN_TESTS_DIR / "data" / "mini_mapping.toml"
GOLDEN_DIR = CODEGEN_TESTS_DIR / "golden"

_MINIMAL_SPEC: dict[str, Any] = {
    "swagger": "2.0",
    "info": {"title": "Tiny", "version": "0.0.1"},
    "paths": {
        "/things": {
            "get": {
                "operationId": "thingList",
                "responses": {"200": {"description": "ok"}},
            }
        }
    },
}


@pytest.fixture(scope="session")
def repo_root() -> Path:
    """The repository root (anchors the real Spec and the ruff config)."""
    return find_root(Path(__file__))


@pytest.fixture(scope="session")
def mini_spec() -> Spec:
    """The synthetic mini Spec that exercises every model-emission rule."""
    return load_spec(MINI_SPEC_PATH)


@pytest.fixture(scope="session")
def mini_ir(mini_spec: Spec) -> IR:
    return build_ir(mini_spec)


@pytest.fixture(scope="session")
def real_spec(repo_root: Path) -> Spec:
    return load_spec(repo_root / "spec" / "openapi.json")


@pytest.fixture(scope="session")
def real_ir(real_spec: Spec) -> IR:
    return build_ir(real_spec)


@pytest.fixture(scope="session")
def real_overrides(repo_root: Path) -> Overrides:
    return load_mapping(repo_root / "codegen" / "mapping.toml")


@pytest.fixture(scope="session")
def real_registry(repo_root: Path) -> Registry:
    return load_registry(repo_root / "codegen" / "registry.toml")


@pytest.fixture(scope="session")
def real_naming(real_ir: IR, real_overrides: Overrides, real_registry: Registry) -> Naming:
    return assign_names(real_ir, real_overrides, real_registry)


@pytest.fixture
def minimal_spec_data() -> dict[str, Any]:
    """A fresh copy of the smallest valid Swagger 2.0 document tests mutate."""
    return json.loads(json.dumps(_MINIMAL_SPEC))


@pytest.fixture(scope="session")
def read_modules() -> Callable[[Path], dict[str, bytes]]:
    """A reader returning ``{filename: bytes}`` for every ``*.py`` in a directory."""

    def read(directory: Path) -> dict[str, bytes]:
        return {path.name: path.read_bytes() for path in directory.glob("*.py")}

    return read
