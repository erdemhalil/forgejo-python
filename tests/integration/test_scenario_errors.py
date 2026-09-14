"""Error mapping: 401/403/404/409/422, transport failures, and error payloads."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pydantic
import pytest

import pyfj

if TYPE_CHECKING:
    from harness import Seed

pytestmark = pytest.mark.integration


def test_not_found_maps_to_not_found_error(admin_client: pyfj.Forgejo) -> None:
    with pytest.raises(pyfj.NotFoundError) as caught:
        admin_client.repos.get("pyfj-does-not-exist", "pyfj-does-not-exist")
    error = caught.value
    assert isinstance(error, pyfj.APIError)
    assert isinstance(error, pyfj.ForgejoError)
    assert error.status_code == 404
    assert error.response.status_code == 404
    assert isinstance(error.body, dict)


def test_missing_credentials_map_to_unauthorized(anonymous_client: pyfj.Forgejo) -> None:
    with pytest.raises(pyfj.UnauthorizedError) as caught:
        anonymous_client.user.get()
    assert caught.value.status_code == 401


def test_insufficient_permissions_map_to_forbidden(user_client: pyfj.Forgejo) -> None:
    with pytest.raises(pyfj.ForbiddenError) as caught:
        user_client.admin.users.list()
    assert caught.value.status_code == 403


def test_duplicate_creation_maps_to_conflict(admin_client: pyfj.Forgejo, seed: Seed) -> None:
    repo = seed.repo_for("scenario-conflict")
    with pytest.raises(pyfj.ConflictError) as caught:
        admin_client.orgs.repos.create(repo.owner, name=repo.name)
    assert caught.value.status_code == 409


def test_invalid_input_maps_to_unprocessable_entity(admin_client: pyfj.Forgejo, seed: Seed) -> None:
    repo = seed.repo_for("scenario-errors")
    with pytest.raises(pyfj.UnprocessableEntityError) as caught:
        admin_client.repos.labels.create(repo.owner, repo.name, name="bad-color", color="not-a-colour")
    assert caught.value.status_code == 422


def test_unreachable_instance_maps_to_transport_error() -> None:
    with pyfj.Forgejo("http://127.0.0.1:1", timeout=2.0) as client, pytest.raises(pyfj.TransportError) as caught:
        client.misc.version()
    error = caught.value
    assert isinstance(error, pyfj.ForgejoError)
    assert error.method == "GET"
    assert error.url.endswith("/api/v1/version")
    assert error.cause is not None


def test_invalid_model_input_raises_pydantic_validation_error() -> None:
    with pytest.raises(pydantic.ValidationError):
        pyfj.CreateOrgOption.model_validate({})


def test_api_error_body_prefers_json(admin_client: pyfj.Forgejo) -> None:
    with pytest.raises(pyfj.APIError) as caught:
        admin_client.repos.get("pyfj-does-not-exist", "pyfj-does-not-exist")
    assert isinstance(caught.value.body, dict)
    assert "message" in caught.value.body
