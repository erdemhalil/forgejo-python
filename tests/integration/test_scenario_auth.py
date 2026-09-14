"""Authentication modes: token, Basic auth, sudo, anonymous, and client rules."""

from __future__ import annotations

from typing import TYPE_CHECKING

import httpx2
import pytest
from harness import ADMIN_PASSWORD, ADMIN_USERNAME, USER_USERNAME

import pyfj

if TYPE_CHECKING:
    from harness import ForgejoServer, Seed

pytestmark = pytest.mark.integration


def test_token_auth_reaches_the_seeded_admin(admin_client: pyfj.Forgejo) -> None:
    current = admin_client.user.get()
    assert current.login == ADMIN_USERNAME
    assert current.is_admin is True


def test_basic_auth_reaches_the_seeded_admin(basic_client: pyfj.Forgejo) -> None:
    current = basic_client.user.get()
    assert current.login == ADMIN_USERNAME


def test_anonymous_client_can_read_public_surface(anonymous_client: pyfj.Forgejo) -> None:
    version = anonymous_client.misc.version()
    assert version.version
    with pytest.raises(pyfj.UnauthorizedError):
        anonymous_client.user.get()


def test_sudo_as_switches_the_actor(admin_client: pyfj.Forgejo, seed: Seed) -> None:
    name = seed.name("repo", "sudo-as")
    with admin_client.sudo_as(USER_USERNAME):
        assert admin_client.user.get().login == USER_USERNAME
        # Impersonation is real: the repository is created under the user.
        repo = admin_client.user.repos.create(name=name, auto_init=False)
    assert repo.owner is not None
    assert repo.owner.login == USER_USERNAME
    # The override is context-local and restored outside the scope.
    assert admin_client.user.get().login == ADMIN_USERNAME
    admin_client.repos.delete(USER_USERNAME, name)


def test_client_level_sudo_applies_to_every_request(server: ForgejoServer) -> None:
    with pyfj.Forgejo(server.base_url, token=server.admin_token, sudo=USER_USERNAME) as client:
        assert client.user.get().login == USER_USERNAME
        # The property overrides the client default, and clearing restores it.
        client.sudo = ADMIN_USERNAME
        assert client.user.get().login == ADMIN_USERNAME
        client.sudo = None
        assert client.user.get().login == USER_USERNAME
        # The context manager scopes the same override to a block.
        with client.sudo_as(ADMIN_USERNAME):
            assert client.user.get().login == ADMIN_USERNAME
        assert client.user.get().login == USER_USERNAME


def test_token_and_basic_auth_are_mutually_exclusive(server: ForgejoServer) -> None:
    with pytest.raises(ValueError, match="mutually exclusive"):
        pyfj.Forgejo(server.base_url, token=server.admin_token, auth=(ADMIN_USERNAME, ADMIN_PASSWORD))


def test_injected_httpx2_client_rejects_transport_arguments(server: ForgejoServer) -> None:
    with httpx2.Client() as injected, pytest.raises(TypeError, match="injected httpx2 client"):
        pyfj.Forgejo(server.base_url, client=injected, timeout=5.0)


def test_injected_httpx2_client_is_used(server: ForgejoServer) -> None:
    with httpx2.Client() as injected:
        client = pyfj.Forgejo(server.base_url, token=server.admin_token, client=injected)
        try:
            assert client.user.get().login == ADMIN_USERNAME
        finally:
            client.close()


def test_escape_hatch_returns_raw_responses(admin_client: pyfj.Forgejo) -> None:
    response = admin_client.request("GET", "/version")
    assert response.status_code == 200
    assert "version" in response.json()

    # No error mapping: a missing resource is a plain 404 response.
    missing = admin_client.request("GET", "/repos/does-not/exist")
    assert missing.status_code == 404
