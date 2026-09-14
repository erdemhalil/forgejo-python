"""Generated resource namespaces for the ``misc`` group. Do not edit by hand.

Regenerate with ``python -m codegen``; see docs/development/codegen.md.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from pyfj._generated.models.create_thing_options import CreateThingOptions
from pyfj._generated.models.edit_thing_options import EditThingOptions
from pyfj._generated.models.thing import Thing
from pyfj._runtime import decode

if TYPE_CHECKING:
    import builtins
    from collections.abc import Mapping
    from datetime import datetime
    from typing import Literal

    from pyfj._generated.models.free_form_thing import FreeFormThing
    from pyfj._runtime import AsyncForgejo as _RuntimeAsyncForgejo
    from pyfj._runtime import AsyncPaginated, Paginated
    from pyfj._runtime import Forgejo as _RuntimeForgejo

    FileContent = bytes | str
    FilePart = (
        FileContent
        | tuple[str | None, FileContent]
        | tuple[str | None, FileContent, str | None]
        | tuple[str | None, FileContent, str | None, Mapping[str, str]]
    )


class Misc:
    """The ``misc`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client
        self.widgets: MiscWidgets = MiscWidgets(client)

    def version(self) -> str:
        """
        Read the version.

        Returns:
            Version text.

        Operation ID: getVersion
        """
        _response = self._client._request("GET", "/version")
        return decode(_response, str)


class AsyncMisc:
    """The ``misc`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client
        self.widgets: AsyncMiscWidgets = AsyncMiscWidgets(client)

    async def version(self) -> str:
        """
        Read the version.

        Returns:
            Version text.

        Operation ID: getVersion
        """
        _response = await self._client._request("GET", "/version")
        return decode(_response, str)


class MiscWidgets:
    """The ``misc.widgets`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(
        self,
        *,
        state: Literal["open", "closed"] | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> Paginated[Thing]:
        """
        List widgets.

        Args:
            state:
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            A page of things.

        Operation ID: widgetList
        """
        _query: dict[str, object] = {"state": state}

        return self._client._paginate("GET", "/widgets", model=Thing, params=_query, page=page, limit=limit)

    def create(self, *, name: str, description: str | None = None, owner: str | None = None) -> Thing:
        """
        Create a widget.

        Args:
            name: Name.
            description: Description.
            owner: Optional owner; collides with a path parameter.

        Returns:
            Created.

        Raises:
            UnprocessableEntityError: 422. Validation failed.

        Operation ID: widgetCreate
        """
        _payload = CreateThingOptions(
            name=name,
            description=description,
            owner=owner,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("POST", "/widgets", json=_payload)
        return decode(_response, Thing)

    def fork(self) -> Thing:
        """
        Fork a widget.

        Returns:
            Forked.

        Operation ID: widgetFork
        """
        _response = self._client._request("POST", "/widgets/fork")
        return decode(_response, Thing)

    def update(self, id: int, *, name: str | None = None, description: str | None = None) -> Thing:
        """
        Edit a widget.

        Args:
            id: Thing id.
            name: New name.
            description: New description.

        Returns:
            Edited.

        Operation ID: widgetEdit
        """
        if name is not None or description is not None:
            _payload = EditThingOptions(name=name, description=description).model_dump(
                mode="json", by_alias=True, exclude_none=True
            )
        else:
            _payload = None

        _response = self._client._request("PUT", f"/widgets/{id}", json=_payload)
        return decode(_response, Thing)

    def delete(self, id: int) -> None:
        """
        Delete a widget.

        Args:
            id: Thing id.

        Returns:
            No content.

        Operation ID: widgetDelete
        """
        _response = self._client._request("DELETE", f"/widgets/{id}")
        return decode(_response, None)

    def get(self, id: int, format: Literal["raw", "diff"]) -> bytes:
        """
        Download a widget rendering.

        Args:
            id:
            format:

        Returns:
            Rendered bytes.

        Operation ID: widgetDownload
        """
        _response = self._client._request("GET", f"/widgets/{id}.{format}")
        return decode(_response, bytes)

    def archive(self, id: int) -> bytes:
        """
        Download a widget archive.

        Args:
            id:

        Returns:
            The archive.

        Operation ID: widgetArchive
        """
        _response = self._client._request("GET", f"/widgets/{id}/archive")
        return decode(_response, bytes)

    def attachment(
        self,
        id: int,
        *,
        name: str | None = None,
        updated_at: datetime | None = None,
        attachment: FilePart,
        external_url: str | None = None,
    ) -> Thing:
        """
        Upload a widget attachment.

        Args:
            id:
            name: Attachment name.
            updated_at:
            attachment:
            external_url: External URL.

        Returns:
            Uploaded.

        Operation ID: widgetUploadAttachment
        """
        _query: dict[str, object] = {"name": name, "updated_at": None if updated_at is None else updated_at.isoformat()}

        _files: dict[str, object] = {}
        _files["attachment"] = attachment
        _form: dict[str, object] = {}
        if external_url is not None:
            _form["external_url"] = external_url

        _response = self._client._request("POST", f"/widgets/{id}/attachment", params=_query, files=_files, data=_form)
        return decode(_response, Thing)

    def free(self, id: int, *, body: FreeFormThing | None = None) -> None:
        """
        Post a free-form body.

        Args:
            id:
            body: Full request body; the Spec declares no fields, so extra fields are allowed.

        Returns:
            No content.

        Operation ID: widgetFreeForm
        """
        _payload = None if body is None else body.model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("POST", f"/widgets/{id}/free", json=_payload)
        return decode(_response, None)

    def info(self, id: int) -> builtins.list[Thing]:
        """
        List widget info.

        Args:
            id:

        Returns:
            Info entries.

        Operation ID: widgetInfo
        """
        _response = self._client._request("GET", f"/widgets/{id}/info")
        return decode(_response, list[Thing])

    def log(self, id: int) -> str:
        """
        Read a widget log.

        Args:
            id:

        Returns:
            Full log.

        Operation ID: widgetLog
        """
        _response = self._client._request("GET", f"/widgets/{id}/log")
        return decode(_response, str)

    def member(self, id: int) -> None:
        """
        Check widget membership.

        Args:
            id:

        Returns:
            No content.

        Raises:
            APIError: 303. Redirect to the public member.
            NotFoundError: 404. Not a member.

        Operation ID: widgetIsMember
        """
        _response = self._client._request("GET", f"/widgets/{id}/member")
        return decode(_response, None)

    def refresh(self, id: int) -> Thing | None:
        """
        Refresh a widget.

        Args:
            id:

        Returns:
            Refreshed.

        Operation ID: widgetRefresh
        """
        _response = self._client._request("POST", f"/widgets/{id}/refresh")
        return decode(_response, Thing)

    def report(self, id: int) -> str:
        """
        Render a widget report.

        Args:
            id:

        Returns:
            Plain text report.

        Operation ID: widgetReport
        """
        _response = self._client._request("GET", f"/widgets/{id}/report")
        return decode(_response, str)

    def status(self, id: int) -> None:
        """
        Read a widget status.

        Args:
            id:

        Returns:
            No content.

        Operation ID: widgetStatus
        """
        _response = self._client._request("GET", f"/widgets/{id}/status")
        return decode(_response, None)


class AsyncMiscWidgets:
    """The ``misc.widgets`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(
        self,
        *,
        state: Literal["open", "closed"] | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> AsyncPaginated[Thing]:
        """
        List widgets.

        Args:
            state:
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            A page of things.

        Operation ID: widgetList
        """
        _query: dict[str, object] = {"state": state}

        return await self._client._paginate("GET", "/widgets", model=Thing, params=_query, page=page, limit=limit)

    async def create(self, *, name: str, description: str | None = None, owner: str | None = None) -> Thing:
        """
        Create a widget.

        Args:
            name: Name.
            description: Description.
            owner: Optional owner; collides with a path parameter.

        Returns:
            Created.

        Raises:
            UnprocessableEntityError: 422. Validation failed.

        Operation ID: widgetCreate
        """
        _payload = CreateThingOptions(
            name=name,
            description=description,
            owner=owner,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request("POST", "/widgets", json=_payload)
        return decode(_response, Thing)

    async def fork(self) -> Thing:
        """
        Fork a widget.

        Returns:
            Forked.

        Operation ID: widgetFork
        """
        _response = await self._client._request("POST", "/widgets/fork")
        return decode(_response, Thing)

    async def update(self, id: int, *, name: str | None = None, description: str | None = None) -> Thing:
        """
        Edit a widget.

        Args:
            id: Thing id.
            name: New name.
            description: New description.

        Returns:
            Edited.

        Operation ID: widgetEdit
        """
        if name is not None or description is not None:
            _payload = EditThingOptions(name=name, description=description).model_dump(
                mode="json", by_alias=True, exclude_none=True
            )
        else:
            _payload = None

        _response = await self._client._request("PUT", f"/widgets/{id}", json=_payload)
        return decode(_response, Thing)

    async def delete(self, id: int) -> None:
        """
        Delete a widget.

        Args:
            id: Thing id.

        Returns:
            No content.

        Operation ID: widgetDelete
        """
        _response = await self._client._request("DELETE", f"/widgets/{id}")
        return decode(_response, None)

    async def get(self, id: int, format: Literal["raw", "diff"]) -> bytes:
        """
        Download a widget rendering.

        Args:
            id:
            format:

        Returns:
            Rendered bytes.

        Operation ID: widgetDownload
        """
        _response = await self._client._request("GET", f"/widgets/{id}.{format}")
        return decode(_response, bytes)

    async def archive(self, id: int) -> bytes:
        """
        Download a widget archive.

        Args:
            id:

        Returns:
            The archive.

        Operation ID: widgetArchive
        """
        _response = await self._client._request("GET", f"/widgets/{id}/archive")
        return decode(_response, bytes)

    async def attachment(
        self,
        id: int,
        *,
        name: str | None = None,
        updated_at: datetime | None = None,
        attachment: FilePart,
        external_url: str | None = None,
    ) -> Thing:
        """
        Upload a widget attachment.

        Args:
            id:
            name: Attachment name.
            updated_at:
            attachment:
            external_url: External URL.

        Returns:
            Uploaded.

        Operation ID: widgetUploadAttachment
        """
        _query: dict[str, object] = {"name": name, "updated_at": None if updated_at is None else updated_at.isoformat()}

        _files: dict[str, object] = {}
        _files["attachment"] = attachment
        _form: dict[str, object] = {}
        if external_url is not None:
            _form["external_url"] = external_url

        _response = await self._client._request(
            "POST", f"/widgets/{id}/attachment", params=_query, files=_files, data=_form
        )
        return decode(_response, Thing)

    async def free(self, id: int, *, body: FreeFormThing | None = None) -> None:
        """
        Post a free-form body.

        Args:
            id:
            body: Full request body; the Spec declares no fields, so extra fields are allowed.

        Returns:
            No content.

        Operation ID: widgetFreeForm
        """
        _payload = None if body is None else body.model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request("POST", f"/widgets/{id}/free", json=_payload)
        return decode(_response, None)

    async def info(self, id: int) -> builtins.list[Thing]:
        """
        List widget info.

        Args:
            id:

        Returns:
            Info entries.

        Operation ID: widgetInfo
        """
        _response = await self._client._request("GET", f"/widgets/{id}/info")
        return decode(_response, list[Thing])

    async def log(self, id: int) -> str:
        """
        Read a widget log.

        Args:
            id:

        Returns:
            Full log.

        Operation ID: widgetLog
        """
        _response = await self._client._request("GET", f"/widgets/{id}/log")
        return decode(_response, str)

    async def member(self, id: int) -> None:
        """
        Check widget membership.

        Args:
            id:

        Returns:
            No content.

        Raises:
            APIError: 303. Redirect to the public member.
            NotFoundError: 404. Not a member.

        Operation ID: widgetIsMember
        """
        _response = await self._client._request("GET", f"/widgets/{id}/member")
        return decode(_response, None)

    async def refresh(self, id: int) -> Thing | None:
        """
        Refresh a widget.

        Args:
            id:

        Returns:
            Refreshed.

        Operation ID: widgetRefresh
        """
        _response = await self._client._request("POST", f"/widgets/{id}/refresh")
        return decode(_response, Thing)

    async def report(self, id: int) -> str:
        """
        Render a widget report.

        Args:
            id:

        Returns:
            Plain text report.

        Operation ID: widgetReport
        """
        _response = await self._client._request("GET", f"/widgets/{id}/report")
        return decode(_response, str)

    async def status(self, id: int) -> None:
        """
        Read a widget status.

        Args:
            id:

        Returns:
            No content.

        Operation ID: widgetStatus
        """
        _response = await self._client._request("GET", f"/widgets/{id}/status")
        return decode(_response, None)
