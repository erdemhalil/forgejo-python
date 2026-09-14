"""Systematic smoke pass: invoke every registered operation once.

Each test is one ``operationId``. The bound method is located through its
``Operation ID`` docstring (never by namespace path), so the registry and the
generated surface cannot drift silently: the completeness test asserts that the
docstring index covers all 505 generated operations.

The outcome is checked against the documented return category (``None``,
``str``, ``bytes``, ``bool``, list, dict, paginated): a call that starts
answering 204 or changes shape fails instead of passing silently.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from smoke import (
    EXERCISES,
    RETURNS_BOOL,
    RETURNS_BYTES,
    RETURNS_DICT,
    RETURNS_LIST,
    RETURNS_MAYBE_NONE,
    RETURNS_NONE,
    RETURNS_STR,
)

import pyfj

if TYPE_CHECKING:
    from collections.abc import Callable

    from harness import Seed

pytestmark = pytest.mark.integration

SMOKE_IDS = sorted(EXERCISES)


def _assert_documented_outcome(operation_id: str, result: object) -> None:
    """Assert the documented status and a clean parse for one smoke call."""
    if operation_id in RETURNS_NONE:
        assert result is None, f"{operation_id} documented no content but returned {result!r}"
    elif operation_id in RETURNS_MAYBE_NONE:
        pass  # the Spec allows both a value and null here
    else:
        assert result is not None, f"{operation_id} documented a value but returned None"

    if operation_id in RETURNS_STR:
        assert isinstance(result, str)
    elif operation_id in RETURNS_BYTES:
        assert isinstance(result, bytes)
    elif operation_id in RETURNS_BOOL:
        assert isinstance(result, bool)
    elif operation_id in RETURNS_LIST:
        assert isinstance(result, list)
    elif operation_id in RETURNS_DICT:
        assert isinstance(result, dict)
    elif isinstance(result, pyfj.Paginated):
        assert result.total_count is None or isinstance(result.total_count, int)


@pytest.mark.parametrize("operation_id", SMOKE_IDS)
def test_smoke(
    operation_id: str,
    methods: dict[str, Callable[..., object]],
    seed: Seed,
) -> None:
    """Invoke one generated operation with minimal valid inputs."""
    method = methods[operation_id]
    result = EXERCISES[operation_id](method, seed)
    _assert_documented_outcome(operation_id, result)
