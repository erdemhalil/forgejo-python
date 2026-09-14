"""Client behaviour: URLs, session defaults, injection, hooks, and lifecycles."""

from __future__ import annotations

import importlib.metadata
import ssl
from typing import cast

import httpx2
import pytest
from _helpers import async_client, record_requests, sync_client

from pyfj._runtime import AsyncForgejo, Forgejo, NotFoundError


@pytest.mark.parametrize(
    ("instance_url", "expected"),
    [
        ("https://codeberg.org", "https://codeberg.org/api/v1/version"),
        ("https://codeberg.org/", "https://codeberg.org/api/v1/version"),
        ("https://codeberg.org/api/v1", "https://codeberg.org/api/v1/version"),
        ("https://codeberg.org/api/v1/", "https://codeberg.org/api/v1/version"),
        ("https://codeberg.org/forgejo", "https://codeberg.org/forgejo/api/v1/version"),
        ("https://codeberg.org/forgejo/", "https://codeberg.org/forgejo/api/v1/version"),
        ("https://codeberg.org/forgejo/api/v1", "https://codeberg.org/forgejo/api/v1/version"),
        ("https://codeberg.org/forgejo/api/v1/", "https://codeberg.org/forgejo/api/v1/version"),
    ],
)
def test_base_url_normalisation(instance_url: str, expected: str) -> None:
    seen, handler = record_requests()
    with Forgejo(instance_url, client=httpx2.Client(transport=httpx2.MockTransport(handler))) as client:
        client.request("GET", "/version")
    assert str(seen[0].url) == expected


@pytest.mark.parametrize(
    "instance_url",
    ["", "codeberg.org", "ftp://codeberg.org", "https://", "https://codeberg.org?x=1", "https://codeberg.org#frag"],
)
def test_invalid_instance_urls_raise_immediately(instance_url: str) -> None:
    with pytest.raises(ValueError, match="invalid instance URL"):
        Forgejo(instance_url)


def test_path_without_leading_slash_is_accepted() -> None:
    seen, handler = record_requests()
    with sync_client(handler) as client:
        client.request("GET", "version")
    assert str(seen[0].url) == "https://forgejo.test/api/v1/version"


def test_user_agent_is_pyfj_version() -> None:
    seen, handler = record_requests()
    version = importlib.metadata.version("forgejo-python")
    with sync_client(handler) as client:
        client.request("GET", "/version")
    assert seen[0].headers["User-Agent"] == f"pyfj/{version}"


def test_session_defaults(monkeypatch: pytest.MonkeyPatch) -> None:
    captured: dict[str, object] = {}

    class FakeClient:
        def __init__(self, **kwargs: object) -> None:
            captured.update(kwargs)

        def close(self) -> None:
            pass

    monkeypatch.setattr(httpx2, "Client", FakeClient)
    with Forgejo("https://forgejo.test"):
        pass
    assert captured["timeout"] == 30.0
    assert captured["follow_redirects"] is False
    assert captured["verify"] is True


def test_verify_accepts_ssl_context(monkeypatch: pytest.MonkeyPatch) -> None:
    captured: dict[str, object] = {}

    class FakeClient:
        def __init__(self, **kwargs: object) -> None:
            captured.update(kwargs)

        def close(self) -> None:
            pass

    context = ssl.create_default_context()
    monkeypatch.setattr(httpx2, "Client", FakeClient)
    with Forgejo("https://forgejo.test", verify=context):
        pass
    assert captured["verify"] is context


async def test_async_session_defaults(monkeypatch: pytest.MonkeyPatch) -> None:
    captured: dict[str, object] = {}

    class FakeAsyncClient:
        def __init__(self, **kwargs: object) -> None:
            captured.update(kwargs)

        async def aclose(self) -> None:
            pass

    monkeypatch.setattr(httpx2, "AsyncClient", FakeAsyncClient)
    async with AsyncForgejo("https://forgejo.test"):
        pass
    assert captured["timeout"] == 30.0
    assert captured["follow_redirects"] is False
    assert captured["verify"] is True


def test_timeout_rejected_with_injected_client() -> None:
    with httpx2.Client() as http_client, pytest.raises(TypeError, match="timeout"):
        Forgejo("https://forgejo.test", client=http_client, timeout=5.0)


def test_follow_redirects_rejected_with_injected_client() -> None:
    with httpx2.Client() as http_client, pytest.raises(TypeError, match="follow_redirects"):
        Forgejo("https://forgejo.test", client=http_client, follow_redirects=True)


def test_verify_rejected_with_injected_client() -> None:
    with httpx2.Client() as http_client, pytest.raises(TypeError, match="verify"):
        Forgejo("https://forgejo.test", client=http_client, verify=False)


def test_wrong_httpx2_client_type_is_rejected() -> None:
    with pytest.raises(TypeError, match=r"httpx2\.Client"):
        Forgejo("https://forgejo.test", client=cast("httpx2.Client", httpx2.AsyncClient()))


async def test_async_wrong_httpx2_client_type_is_rejected() -> None:
    with httpx2.Client() as http_client, pytest.raises(TypeError, match=r"httpx2\.AsyncClient"):
        AsyncForgejo("https://forgejo.test", client=cast("httpx2.AsyncClient", http_client))


def test_request_escape_hatch_skips_error_mapping() -> None:
    def handler(request: httpx2.Request) -> httpx2.Response:
        return httpx2.Response(404, json={"message": "not found"}, request=request)

    with sync_client(handler) as client:
        response = client.request("GET", "/missing")
    assert response.status_code == 404


def test_request_hook_maps_errors() -> None:
    def handler(request: httpx2.Request) -> httpx2.Response:
        return httpx2.Response(404, json={"message": "not found"}, request=request)

    with sync_client(handler) as client, pytest.raises(NotFoundError):
        client._request("GET", "/missing")


def test_request_escape_hatch_does_not_wrap_transport_errors() -> None:
    def handler(request: httpx2.Request) -> httpx2.Response:
        message = "connection refused"
        raise httpx2.ConnectError(message, request=request)

    with sync_client(handler) as client, pytest.raises(httpx2.ConnectError):
        client.request("GET", "/version")


def test_escape_hatch_applies_credentials() -> None:
    seen, handler = record_requests()
    with sync_client(handler, token="abc") as client:
        client.request("GET", "/version")
    assert seen[0].headers["Authorization"] == "token abc"


def test_none_query_parameters_are_dropped() -> None:
    seen, handler = record_requests()
    with sync_client(handler) as client:
        client._request("GET", "/issues", params={"state": "open", "labels": None, "page": 2})
    params = seen[0].url.params
    assert params["state"] == "open"
    assert params["page"] == "2"
    assert "labels" not in params


def test_sequence_query_parameters_are_preserved() -> None:
    seen, handler = record_requests()
    with sync_client(handler) as client:
        client._request("GET", "/issues", params={"labels": ["bug", "docs"]})
    assert seen[0].url.params.get_list("labels") == ["bug", "docs"]


def test_extra_headers_are_merged() -> None:
    seen, handler = record_requests()
    with sync_client(handler) as client:
        client._request("GET", "/version", headers={"Accept": "text/plain"})
    assert seen[0].headers["Accept"] == "text/plain"


def test_pyfj_credentials_win_over_injected_client_auth() -> None:
    seen, handler = record_requests()
    http_client = httpx2.Client(transport=httpx2.MockTransport(handler), auth=("client", "secret"))
    with Forgejo("https://forgejo.test", token="abc", client=http_client) as client:
        client._request("GET", "/version")
    assert seen[0].headers["Authorization"] == "token abc"


def test_injected_client_auth_is_used_without_pyfj_credentials() -> None:
    seen, handler = record_requests()
    http_client = httpx2.Client(transport=httpx2.MockTransport(handler), auth=("client", "secret"))
    with Forgejo("https://forgejo.test", client=http_client) as client:
        client._request("GET", "/version")
    assert seen[0].headers["Authorization"].startswith("Basic ")


def test_context_manager_closes_injected_client() -> None:
    _, handler = record_requests()
    http_client = httpx2.Client(transport=httpx2.MockTransport(handler))
    with Forgejo("https://forgejo.test", client=http_client):
        assert http_client.is_closed is False
    assert http_client.is_closed is True


def test_context_manager_closes_owned_client() -> None:
    with Forgejo("https://forgejo.test") as client:
        inner = client._client
        assert inner.is_closed is False
    assert inner.is_closed is True


async def test_async_client_requests_and_closes() -> None:
    seen, handler = record_requests()
    http_client = httpx2.AsyncClient(transport=httpx2.MockTransport(handler))
    async with AsyncForgejo("https://forgejo.test", client=http_client) as client:
        response = await client.request("GET", "/version")
        assert response.status_code == 200
        assert http_client.is_closed is False
    assert str(seen[0].url) == "https://forgejo.test/api/v1/version"
    assert http_client.is_closed is True


async def test_async_request_hook_maps_errors() -> None:
    def handler(request: httpx2.Request) -> httpx2.Response:
        return httpx2.Response(404, json={"message": "not found"}, request=request)

    async with async_client(handler) as client:
        with pytest.raises(NotFoundError):
            await client._request("GET", "/missing")
