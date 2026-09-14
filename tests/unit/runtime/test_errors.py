"""Per-status mapping, error payloads, and hierarchy."""

from __future__ import annotations

import httpx
import pytest

from pyfj._runtime import (
    APIError,
    BadRequestError,
    ConflictError,
    ForbiddenError,
    Forgejo,
    ForgejoError,
    LockedError,
    MethodNotAllowedError,
    NotFoundError,
    PayloadTooLargeError,
    PreconditionFailedError,
    ServerError,
    TransportError,
    UnauthorizedError,
    UnprocessableEntityError,
    api_error,
)

_REQUEST = httpx.Request("GET", "https://forgejo.test/api/v1/repos/alice/demo")


def _response(status: int, *, json: object | None = None, text: str | None = None) -> httpx.Response:
    return httpx.Response(status, json=json, text=text, request=_REQUEST)


@pytest.mark.parametrize(
    ("status", "expected"),
    [
        (400, BadRequestError),
        (401, UnauthorizedError),
        (403, ForbiddenError),
        (404, NotFoundError),
        (405, MethodNotAllowedError),
        (409, ConflictError),
        (412, PreconditionFailedError),
        (413, PayloadTooLargeError),
        (422, UnprocessableEntityError),
        (423, LockedError),
    ],
)
def test_documented_statuses_map_to_subclasses(status: int, expected: type[APIError]) -> None:
    error = api_error(_response(status, json={"message": "nope"}))
    assert type(error) is expected
    assert isinstance(error, APIError)
    assert error.status_code == status


@pytest.mark.parametrize("status", [500, 502, 503, 599])
def test_5xx_maps_to_server_error(status: int) -> None:
    error = api_error(_response(status))
    assert type(error) is ServerError


@pytest.mark.parametrize("status", [301, 302, 304, 418, 429, 451])
def test_unmapped_statuses_map_to_api_error(status: int) -> None:
    error = api_error(_response(status))
    assert type(error) is APIError


def test_body_is_parsed_json_when_possible() -> None:
    body = {"message": "repo not found", "url": "https://forgejo.test/docs"}
    error = api_error(_response(404, json=body))
    assert error.body == body
    assert "repo not found" in str(error)


def test_body_is_text_when_not_json() -> None:
    error = api_error(_response(502, text="<html>bad gateway</html>"))
    assert error.body == "<html>bad gateway</html>"
    assert "bad gateway" in str(error)


def test_empty_body_is_empty_text() -> None:
    error = api_error(_response(500))
    assert error.body == ""


def test_error_carries_the_raw_response() -> None:
    response = _response(404, json={"message": "gone"})
    error = api_error(response)
    assert error.response is response


def test_message_contains_method_url_and_status() -> None:
    error = api_error(_response(409, json={"message": "conflict"}))
    message = str(error)
    assert "GET" in message
    assert "https://forgejo.test/api/v1/repos/alice/demo" in message
    assert "409" in message


def test_hierarchy() -> None:
    assert issubclass(APIError, ForgejoError)
    assert issubclass(TransportError, ForgejoError)
    for subclass in (
        BadRequestError,
        UnauthorizedError,
        ForbiddenError,
        NotFoundError,
        MethodNotAllowedError,
        ConflictError,
        PreconditionFailedError,
        PayloadTooLargeError,
        UnprocessableEntityError,
        LockedError,
        ServerError,
    ):
        assert issubclass(subclass, APIError)


def test_transport_error_wraps_httpx_error() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        message = "connection refused"
        raise httpx.ConnectError(message, request=request)

    transport = httpx.MockTransport(handler)
    http_client = httpx.Client(transport=transport)
    with Forgejo("https://forgejo.test", client=http_client) as client, pytest.raises(TransportError) as caught:
        client._request("GET", "/version")
    error = caught.value
    assert isinstance(error.cause, httpx.ConnectError)
    assert error.method == "GET"
    assert error.url == "https://forgejo.test/api/v1/version"
    assert error.__cause__ is error.cause
