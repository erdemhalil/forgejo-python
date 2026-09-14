"""Shared helpers for runtime unit tests (mock transport only, no network)."""

from __future__ import annotations

from collections.abc import Callable

import httpx2
from pydantic import BaseModel

from pyfj._runtime import AsyncForgejo, Forgejo

Handler = Callable[[httpx2.Request], httpx2.Response]


class Issue(BaseModel):
    """Minimal stand-in for a generated model."""

    id: int
    title: str


def record_requests() -> tuple[list[httpx2.Request], Handler]:
    """A handler that records each request and answers ``200`` with no body."""
    seen: list[httpx2.Request] = []

    def handler(request: httpx2.Request) -> httpx2.Response:
        seen.append(request)
        return httpx2.Response(200, request=request)

    return seen, handler


def sync_client(
    handler: Handler,
    *,
    token: str | None = None,
    auth: tuple[str, str] | None = None,
    otp: str | None = None,
    sudo: str | None = None,
) -> Forgejo:
    """A ``Forgejo`` against ``https://forgejo.test`` wired to ``handler``."""
    return Forgejo(
        "https://forgejo.test",
        token=token,
        auth=auth,
        otp=otp,
        sudo=sudo,
        client=httpx2.Client(transport=httpx2.MockTransport(handler)),
    )


def async_client(
    handler: Handler,
    *,
    token: str | None = None,
    auth: tuple[str, str] | None = None,
    otp: str | None = None,
    sudo: str | None = None,
) -> AsyncForgejo:
    """An ``AsyncForgejo`` against ``https://forgejo.test`` wired to ``handler``."""
    return AsyncForgejo(
        "https://forgejo.test",
        token=token,
        auth=auth,
        otp=otp,
        sudo=sudo,
        client=httpx2.AsyncClient(transport=httpx2.MockTransport(handler)),
    )
