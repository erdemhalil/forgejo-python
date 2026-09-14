"""Completeness without Docker: every Spec Operation is accounted for.

The Spec's operations must each be exactly one of:

* exercised by the smoke registry (``smoke.EXERCISES``),
* skipped with a written reason (``tests/integration/skips.toml``),
* excluded from generation with a reason (``codegen/registry.toml``).

This file deliberately carries no ``integration`` marker, so the default
``uv run pytest`` run enforces it without Docker.
"""

from __future__ import annotations

import json
import tomllib
from pathlib import Path

from harness import build_method_index
from smoke import EXERCISES

import pyfj

REPO_ROOT = Path(__file__).resolve().parents[2]
SPEC_PATH = REPO_ROOT / "spec" / "openapi.json"
EXCLUSIONS_PATH = REPO_ROOT / "codegen" / "registry.toml"
SKIPS_PATH = Path(__file__).with_name("skips.toml")

EXPECTED_SPEC_OPERATIONS = 506
EXPECTED_GENERATED_OPERATIONS = 505
EXPECTED_EXCLUSIONS = frozenset({"getActionsRun"})

_HTTP_METHODS = ("get", "post", "put", "patch", "delete")


def spec_operations() -> set[str]:
    """Every operationId in the vendored Spec."""
    document = json.loads(SPEC_PATH.read_text(encoding="utf-8"))
    operations: set[str] = set()
    for path in document["paths"].values():
        for method, operation in path.items():
            if method in _HTTP_METHODS and isinstance(operation, dict) and "operationId" in operation:
                operations.add(operation["operationId"])
    return operations


def skipped_operations() -> dict[str, dict[str, str]]:
    """The skips.toml entries keyed by operationId."""
    document = tomllib.loads(SKIPS_PATH.read_text(encoding="utf-8"))
    return {entry["operation"]: entry for entry in document["skips"]}


def excluded_operations() -> set[str]:
    """The excluded operations from the generator's registry."""
    document = tomllib.loads(EXCLUSIONS_PATH.read_text(encoding="utf-8"))
    return {entry["operation"] for entry in document["exclusions"]}


def test_the_spec_still_has_the_expected_operation_count() -> None:
    assert len(spec_operations()) == EXPECTED_SPEC_OPERATIONS


def test_generated_plus_excluded_is_the_whole_spec() -> None:
    spec = spec_operations()
    excluded = excluded_operations()
    assert excluded == EXPECTED_EXCLUSIONS
    assert len(spec - excluded) == EXPECTED_GENERATED_OPERATIONS


def test_every_generated_operation_is_exercised_or_skipped() -> None:
    generated = spec_operations() - excluded_operations()
    exercised = set(EXERCISES)
    skipped = set(skipped_operations())
    assert exercised & skipped == set(), f"both exercised and skipped: {sorted(exercised & skipped)}"
    assert exercised | skipped == generated, f"unaccounted: {sorted(generated - exercised - skipped)}"


def test_exercise_and_skip_keys_are_generated_operations() -> None:
    generated = spec_operations() - excluded_operations()
    assert set(EXERCISES) <= generated
    assert set(skipped_operations()) <= generated


def test_every_skip_has_a_kind_and_a_reason() -> None:
    for operation, entry in skipped_operations().items():
        assert entry.get("kind") in {"infrastructure", "pending"}, operation
        reason = entry.get("reason", "")
        assert len(reason) >= 20, f"{operation}: reason is too short to be meaningful: {reason!r}"


def test_every_exercise_binds_to_a_generated_method() -> None:
    """The docstring index must cover every generated operation and registry key."""
    generated = spec_operations() - excluded_operations()
    client = pyfj.Forgejo("https://example.test")
    try:
        index = build_method_index(client)
    finally:
        client.close()
    assert len(index) == EXPECTED_GENERATED_OPERATIONS, (
        f"docstring binding found {len(index)} operations, expected {EXPECTED_GENERATED_OPERATIONS}"
    )
    assert set(index) == generated, f"docstring binding mismatch: {sorted(set(index) ^ generated)}"
    missing = set(EXERCISES) - set(index)
    assert missing == set(), f"smoke entries not bound to a method: {sorted(missing)}"


def test_counts_add_up() -> None:
    exercised = len(EXERCISES)
    skipped = len(skipped_operations())
    excluded = len(excluded_operations())
    assert exercised + skipped + excluded == EXPECTED_SPEC_OPERATIONS
