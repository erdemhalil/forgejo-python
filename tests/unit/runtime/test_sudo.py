"""Client-scoped sudo: the property, the context manager, and context isolation."""

from __future__ import annotations

import asyncio
from typing import TYPE_CHECKING

import pytest
from _helpers import async_client, record_requests, sync_client

if TYPE_CHECKING:
    import httpx


def _sudo_headers(requests: list[httpx.Request]) -> list[str | None]:
    return [request.headers.get("Sudo") for request in requests]


def test_constructor_default_is_effective_without_an_override() -> None:
    seen, handler = record_requests()
    with sync_client(handler, sudo="alice") as client:
        assert client.sudo == "alice"
        client._request("GET", "/version")
    assert _sudo_headers(seen) == ["alice"]


def test_setter_overrides_and_none_restores_the_default() -> None:
    seen, handler = record_requests()
    with sync_client(handler, sudo="alice") as client:
        client.sudo = "bob"
        assert client.sudo == "bob"
        client._request("GET", "/version")
        client.sudo = None
        assert client.sudo == "alice"
        client._request("GET", "/version")
    assert _sudo_headers(seen) == ["bob", "alice"]


def test_setter_without_a_default() -> None:
    seen, handler = record_requests()
    with sync_client(handler) as client:
        assert client.sudo is None
        client.sudo = "bob"
        client._request("GET", "/version")
        client.sudo = None
        assert client.sudo is None
        client._request("GET", "/version")
    assert _sudo_headers(seen) == ["bob", None]


def test_overrides_are_per_client() -> None:
    seen, handler = record_requests()
    with sync_client(handler) as first, sync_client(handler) as second:
        first.sudo = "alice"
        second.sudo = "bob"
        first._request("GET", "/version")
        second._request("GET", "/version")
    assert _sudo_headers(seen) == ["alice", "bob"]


def test_sudo_as_sets_and_restores() -> None:
    seen, handler = record_requests()
    with sync_client(handler) as client, client.sudo_as("alice"):
        assert client.sudo == "alice"
        client._request("GET", "/version")
    assert client.sudo is None
    assert _sudo_headers(seen) == ["alice"]


def test_sudo_as_nests_and_restores_the_previous_value() -> None:
    seen, handler = record_requests()
    with sync_client(handler, sudo="root") as client:
        with client.sudo_as("alice"):
            assert client.sudo == "alice"
            with client.sudo_as("bob"):
                assert client.sudo == "bob"
                client._request("GET", "/version")
            assert client.sudo == "alice"
            client._request("GET", "/version")
        assert client.sudo == "root"
        client._request("GET", "/version")
    assert _sudo_headers(seen) == ["bob", "alice", "root"]


def test_sudo_as_restores_on_exception() -> None:
    _, handler = record_requests()
    with sync_client(handler, sudo="root") as client:
        with pytest.raises(RuntimeError, match="boom"), client.sudo_as("alice"):
            raise RuntimeError("boom")
        assert client.sudo == "root"


async def test_async_sudo_as_works() -> None:
    seen, handler = record_requests()
    async with async_client(handler, sudo="root") as client:
        async with client.sudo_as("alice"):
            assert client.sudo == "alice"
            await client._request("GET", "/version")
        assert client.sudo == "root"
    assert _sudo_headers(seen) == ["alice"]


async def test_async_client_accepts_the_sync_context_manager() -> None:
    seen, handler = record_requests()
    async with async_client(handler) as client:
        with client.sudo_as("alice"):
            await client._request("GET", "/version")
        assert client.sudo is None
    assert _sudo_headers(seen) == ["alice"]


async def test_child_tasks_inherit_the_value_at_creation() -> None:
    _, handler = record_requests()
    async with async_client(handler, sudo="root") as client, client.sudo_as("alice"):

        async def read() -> str | None:
            return client.sudo

        assert await asyncio.create_task(read()) == "alice"
        assert client.sudo == "alice"


async def test_concurrent_tasks_do_not_leak_sudo() -> None:
    """Two tasks impersonate different users; each request carries its own value.

    The first task enters its scope and blocks; the second enters while the
    first is still inside. A plain instance attribute would leak the second
    value into the first task's request.
    """
    seen, handler = record_requests()
    inside = asyncio.Event()
    release = asyncio.Event()

    async def impersonate(username: str) -> None:
        async with client.sudo_as(username):
            if not inside.is_set():
                inside.set()
                await release.wait()
            assert client.sudo == username
            await client._request("GET", "/version")

    async with async_client(handler, sudo="root") as client:
        first = asyncio.create_task(impersonate("alice"))
        await inside.wait()
        second = asyncio.create_task(impersonate("bob"))
        await asyncio.sleep(0)  # let the second task enter its scope
        release.set()
        await asyncio.gather(first, second)
        assert client.sudo == "root"
        await client._request("GET", "/version")

    assert sorted(request.headers["Sudo"] for request in seen) == ["alice", "bob", "root"]
