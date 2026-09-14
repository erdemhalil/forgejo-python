"""Generated resource namespaces for the ``users`` group. Do not edit by hand.

Regenerate with ``python -m codegen``; see docs/development/codegen.md.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from pyfj._generated.models.create_org_options import CreateOrgOptions
from pyfj._generated.models.thing import Thing
from pyfj._runtime import decode

if TYPE_CHECKING:
    from pyfj._runtime import AsyncForgejo as _RuntimeAsyncForgejo
    from pyfj._runtime import Forgejo as _RuntimeForgejo


class Users:
    """The ``users`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def old(self, username: str) -> Thing:
        """
        Read a legacy user record.

        Args:
            username:

        Returns:
            The user.

        Deprecated:
            Deprecated in the vendored Spec; generated for compatibility.

        Operation ID: userOld
        """
        _response = self._client._request("GET", f"/users/{username}/old")
        return decode(_response, Thing)

    def orgs(self, username: str, *, body_username: str, description: str | None = None) -> Thing:
        """
        Create an organization for a user.

        Args:
            username:
            body_username: New organization name. Wire field ``username``.
            description: Description.

        Returns:
            Created.

        Operation ID: userCreateOrg
        """
        _payload = CreateOrgOptions(
            username=body_username,
            description=description,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("POST", f"/users/{username}/orgs", json=_payload)
        return decode(_response, Thing)


class AsyncUsers:
    """The ``users`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def old(self, username: str) -> Thing:
        """
        Read a legacy user record.

        Args:
            username:

        Returns:
            The user.

        Deprecated:
            Deprecated in the vendored Spec; generated for compatibility.

        Operation ID: userOld
        """
        _response = await self._client._request("GET", f"/users/{username}/old")
        return decode(_response, Thing)

    async def orgs(self, username: str, *, body_username: str, description: str | None = None) -> Thing:
        """
        Create an organization for a user.

        Args:
            username:
            body_username: New organization name. Wire field ``username``.
            description: Description.

        Returns:
            Created.

        Operation ID: userCreateOrg
        """
        _payload = CreateOrgOptions(
            username=body_username,
            description=description,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request("POST", f"/users/{username}/orgs", json=_payload)
        return decode(_response, Thing)
