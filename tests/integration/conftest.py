"""Integration-tier fixtures: a booted Forgejo container and seeded clients.

Integration tests are marker-gated (``integration``): locally they skip — never
fail — when no Docker daemon answers, but in CI (``CI`` set) a missing daemon
aborts the run instead of silently skipping the whole tier. The container is
session-scoped; resources that smoke and scenario tests share are seeded lazily
through :class:`harness.Seed`.
"""

from __future__ import annotations

import os
from typing import TYPE_CHECKING

import pytest
from harness import (
    ADMIN_PASSWORD,
    ADMIN_USERNAME,
    CLIENT_TIMEOUT,
    Seed,
    build_method_index,
    docker_available,
    start_forgejo,
)

import pyfj

if TYPE_CHECKING:
    from collections.abc import AsyncIterator, Callable, Iterator

    from harness import ForgejoServer

DOCKER_SKIP_REASON = "Docker is not available; start Docker Desktop (or another daemon) and re-run with -m integration."


def _is_integration(item: pytest.Item) -> bool:
    """Whether the item carries the explicit ``integration`` marker.

    Checking ``item.keywords`` would also match the ``tests/integration`` path
    component, which would treat the Docker-free completeness test as an
    integration test.
    """
    return item.get_closest_marker("integration") is not None


@pytest.hookimpl(trylast=True)
def pytest_collection_modifyitems(config: pytest.Config, items: list[pytest.Item]) -> None:
    """Mark integration tests skipped when Docker cannot be reached.

    ``trylast`` makes this run after pytest's own ``-m`` deselection, so a
    default unit run (``-m 'not integration'``, from addopts) never probes the
    Docker daemon: the return below happens before ``docker_available()``.
    """
    del config
    integration_items = [item for item in items if _is_integration(item)]
    if not integration_items or docker_available():
        return
    if os.environ.get("CI"):
        message = (
            "Docker is unavailable but integration tests were selected in CI; refusing to skip the whole tier. "
            "Check the Docker daemon and the image pre-pull step."
        )
        raise pytest.UsageError(message)
    marker = pytest.mark.skip(reason=DOCKER_SKIP_REASON)
    for item in integration_items:
        item.add_marker(marker)


@pytest.fixture(scope="session")
def server() -> Iterator[ForgejoServer]:
    """A booted, seeded Forgejo container shared by the whole session."""
    if not docker_available():
        pytest.skip(DOCKER_SKIP_REASON)
    booted = start_forgejo()
    try:
        yield booted
    finally:
        booted.stop()


@pytest.fixture(scope="session")
def admin_client(server: ForgejoServer) -> Iterator[pyfj.Forgejo]:
    """An authenticated sync client for the seeded admin user."""
    with pyfj.Forgejo(server.base_url, token=server.admin_token, timeout=CLIENT_TIMEOUT) as client:
        yield client


@pytest.fixture(scope="session")
def user_client(server: ForgejoServer) -> Iterator[pyfj.Forgejo]:
    """An authenticated sync client for the seeded regular user."""
    with pyfj.Forgejo(server.base_url, token=server.user_token, timeout=CLIENT_TIMEOUT) as client:
        yield client


@pytest.fixture(scope="session")
def seed(server: ForgejoServer, admin_client: pyfj.Forgejo) -> Iterator[Seed]:
    """The lazily-seeded resource model shared across the session."""
    seeded = Seed(server, admin_client)
    try:
        yield seeded
    finally:
        seeded.close()


@pytest.fixture(scope="session")
def methods(admin_client: pyfj.Forgejo) -> dict[str, Callable[..., object]]:
    """Every generated sync operation, bound by its ``Operation ID`` docstring."""
    return build_method_index(admin_client)


@pytest.fixture
def anonymous_client(server: ForgejoServer) -> Iterator[pyfj.Forgejo]:
    """A credential-less client (public surface only)."""
    with pyfj.Forgejo(server.base_url, timeout=CLIENT_TIMEOUT) as client:
        yield client


@pytest.fixture
def basic_client(server: ForgejoServer) -> Iterator[pyfj.Forgejo]:
    """A client using the admin's username/password via Basic auth."""
    with pyfj.Forgejo(server.base_url, auth=(ADMIN_USERNAME, ADMIN_PASSWORD), timeout=CLIENT_TIMEOUT) as client:
        yield client


@pytest.fixture
async def async_admin_client(server: ForgejoServer) -> AsyncIterator[pyfj.AsyncForgejo]:
    """An authenticated async client for the seeded admin user."""
    async with pyfj.AsyncForgejo(server.base_url, token=server.admin_token, timeout=CLIENT_TIMEOUT) as client:
        yield client


@pytest.fixture
async def async_user_client(server: ForgejoServer) -> AsyncIterator[pyfj.AsyncForgejo]:
    """An authenticated async client for the seeded regular user."""
    async with pyfj.AsyncForgejo(server.base_url, token=server.user_token, timeout=CLIENT_TIMEOUT) as client:
        yield client
