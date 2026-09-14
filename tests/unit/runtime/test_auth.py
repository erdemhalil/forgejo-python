"""Credential assembly: token, basic, OTP, and their combinations."""

from __future__ import annotations

import base64

import pytest
from _helpers import record_requests, sync_client

from pyfj._runtime import Auth, Forgejo


def test_token_is_sent_as_token_scheme() -> None:
    seen, transport = record_requests()
    with sync_client(transport, token="abc123") as client:
        client._request("GET", "/version")
    assert seen[0].headers["Authorization"] == "token abc123"


@pytest.mark.parametrize("token", ["token abc123", "Token abc123", "TOKEN abc123"])
def test_existing_token_prefix_is_not_duplicated(token: str) -> None:
    seen, transport = record_requests()
    with sync_client(transport, token=token) as client:
        client._request("GET", "/version")
    assert seen[0].headers["Authorization"] == "token abc123"


def test_only_one_token_prefix_is_stripped() -> None:
    seen, transport = record_requests()
    with sync_client(transport, token="token token abc123") as client:
        client._request("GET", "/version")
    assert seen[0].headers["Authorization"] == "token token abc123"


def test_basic_auth_is_base64_encoded() -> None:
    seen, transport = record_requests()
    with sync_client(transport, auth=("alice", "s3cr3t")) as client:
        client._request("GET", "/version")
    expected = base64.b64encode(b"alice:s3cr3t").decode("ascii")
    assert seen[0].headers["Authorization"] == f"Basic {expected}"


def test_otp_header() -> None:
    seen, transport = record_requests()
    with sync_client(transport, otp="654321") as client:
        client._request("GET", "/version")
    assert seen[0].headers["X-FORGEJO-OTP"] == "654321"


def test_no_credentials_means_no_authorization_header() -> None:
    seen, transport = record_requests()
    with sync_client(transport) as client:
        client._request("GET", "/version")
    assert "Authorization" not in seen[0].headers
    assert "Sudo" not in seen[0].headers


def test_token_and_basic_are_mutually_exclusive() -> None:
    with pytest.raises(ValueError, match="mutually exclusive"):
        Forgejo("https://forgejo.test", token="abc", auth=("alice", "s3cr3t"))


def test_auth_headers_helper() -> None:
    headers = Auth(token="token abc", otp="1234").headers()
    assert headers == {"Authorization": "token abc", "X-FORGEJO-OTP": "1234"}


def test_auth_headers_helper_without_credentials() -> None:
    assert Auth().headers() == {}
    assert Auth().authorizes_requests is False
    assert Auth(token="abc").authorizes_requests is True
    assert Auth(basic=("a", "b")).authorizes_requests is True
