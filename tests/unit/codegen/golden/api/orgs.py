"""Generated resource namespaces for the ``orgs`` group. Do not edit by hand.

Regenerate with ``python -m codegen``; see docs/development/codegen.md.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from pyfj._generated.models.create_thing_options import CreateThingOptions
from pyfj._generated.models.thing import Thing
from pyfj._runtime import decode

if TYPE_CHECKING:
    from pyfj._runtime import AsyncForgejo as _RuntimeAsyncForgejo
    from pyfj._runtime import Forgejo as _RuntimeForgejo


class Orgs:
    """The ``orgs`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client
        self.things: OrgsThings = OrgsThings(client)


class AsyncOrgs:
    """The ``orgs`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client
        self.things: AsyncOrgsThings = AsyncOrgsThings(client)


class OrgsThings:
    """The ``orgs.things`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def create(self, owner: str, *, name: str, description: str | None = None, body_owner: str | None = None) -> Thing:
        """
        Create a thing for an owner.

        Args:
            owner:
            name: Name.
            description: Description.
            body_owner: Optional owner; collides with a path parameter. Wire field ``owner``.

        Returns:
            Created.

        Operation ID: thingCreateInOrg
        """
        _payload = CreateThingOptions(
            name=name,
            description=description,
            owner=body_owner,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("POST", f"/orgs/{owner}/things", json=_payload)
        return decode(_response, Thing)

    def update(
        self,
        owner: str,
        id: int,
        *,
        name: str,
        description: str | None = None,
        body_owner: str | None = None,
    ) -> Thing:
        """
        Edit a thing for an owner.

        Args:
            owner:
            id:
            name: Name.
            description: Description.
            body_owner: Optional owner; collides with a path parameter. Wire field ``owner``.

        Returns:
            Edited.

        Operation ID: thingEditInOrg
        """
        _payload = CreateThingOptions(
            name=name,
            description=description,
            owner=body_owner,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("PATCH", f"/orgs/{owner}/things/{id}", json=_payload)
        return decode(_response, Thing)


class AsyncOrgsThings:
    """The ``orgs.things`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def create(
        self,
        owner: str,
        *,
        name: str,
        description: str | None = None,
        body_owner: str | None = None,
    ) -> Thing:
        """
        Create a thing for an owner.

        Args:
            owner:
            name: Name.
            description: Description.
            body_owner: Optional owner; collides with a path parameter. Wire field ``owner``.

        Returns:
            Created.

        Operation ID: thingCreateInOrg
        """
        _payload = CreateThingOptions(
            name=name,
            description=description,
            owner=body_owner,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request("POST", f"/orgs/{owner}/things", json=_payload)
        return decode(_response, Thing)

    async def update(
        self,
        owner: str,
        id: int,
        *,
        name: str,
        description: str | None = None,
        body_owner: str | None = None,
    ) -> Thing:
        """
        Edit a thing for an owner.

        Args:
            owner:
            id:
            name: Name.
            description: Description.
            body_owner: Optional owner; collides with a path parameter. Wire field ``owner``.

        Returns:
            Edited.

        Operation ID: thingEditInOrg
        """
        _payload = CreateThingOptions(
            name=name,
            description=description,
            owner=body_owner,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request("PATCH", f"/orgs/{owner}/things/{id}", json=_payload)
        return decode(_response, Thing)
