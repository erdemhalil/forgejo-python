"""Generated resource namespaces for the ``notifications`` group. Do not edit by hand.

Regenerate with ``python -m codegen``; see docs/development/codegen.md.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from pyfj._generated.models.notification_count import NotificationCount
from pyfj._generated.models.notification_thread import NotificationThread
from pyfj._runtime import decode

if TYPE_CHECKING:
    import builtins
    from datetime import datetime
    from typing import Literal

    from pyfj._runtime import AsyncForgejo as _RuntimeAsyncForgejo
    from pyfj._runtime import AsyncPaginated, Paginated
    from pyfj._runtime import Forgejo as _RuntimeForgejo


class Notifications:
    """The ``notifications`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client
        self.threads: NotificationsThreads = NotificationsThreads(client)

    def list(
        self,
        *,
        all: bool | None = None,
        status_types: builtins.list[str] | None = None,
        subject_type: builtins.list[Literal["issue", "pull", "repository"]] | None = None,
        since: datetime | None = None,
        before: datetime | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> Paginated[NotificationThread]:
        """
        List users's notification threads.

        Args:
            all: If true, show notifications marked as read. Default value is false
            status_types: Show notifications with the provided status types. Options are: unread, read and/or pinned.
                Defaults to unread & pinned.
            subject_type: filter notifications by subject type
            since: Only show notifications updated after the given time. This is a timestamp in RFC 3339 format
            before: Only show notifications updated before the given time. This is a timestamp in RFC 3339 format
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            NotificationThreadList.

        Operation ID: notifyGetList
        """
        _query: dict[str, object] = {
            "all": all,
            "status-types": status_types,
            "subject-type": subject_type,
            "since": None if since is None else since.isoformat(),
            "before": None if before is None else before.isoformat(),
        }

        return self._client._paginate(
            "GET", "/notifications", model=NotificationThread, params=_query, page=page, limit=limit
        )

    def update(
        self,
        *,
        last_read_at: datetime | None = None,
        all: bool | None = None,
        status_types: builtins.list[str] | None = None,
        to_status: str | None = None,
    ) -> None:
        """
        Mark notification threads as read, pinned or unread.

        Args:
            last_read_at: Describes the last point that notifications were checked. Anything updated since this time
                will not be updated.
            all: If true, mark all notifications on this repo. Default value is false
            status_types: Mark notifications with the provided status types. Options are: unread, read and/or pinned.
                Defaults to unread.
            to_status: Status to mark notifications as, Defaults to read.

        Returns:
            No content.

        Operation ID: notifyReadList
        """
        _query: dict[str, object] = {
            "last_read_at": None if last_read_at is None else last_read_at.isoformat(),
            "all": all,
            "status-types": status_types,
            "to-status": to_status,
        }

        _response = self._client._request("PUT", "/notifications", params=_query)
        return decode(_response, None)

    def new_count(self) -> NotificationCount:
        """
        Check if unread notifications exist.

        Returns:
            Number of unread notifications.

        Operation ID: notifyNewAvailable
        """
        _response = self._client._request("GET", "/notifications/new")
        return decode(_response, NotificationCount)


class AsyncNotifications:
    """The ``notifications`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client
        self.threads: AsyncNotificationsThreads = AsyncNotificationsThreads(client)

    async def list(
        self,
        *,
        all: bool | None = None,
        status_types: builtins.list[str] | None = None,
        subject_type: builtins.list[Literal["issue", "pull", "repository"]] | None = None,
        since: datetime | None = None,
        before: datetime | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> AsyncPaginated[NotificationThread]:
        """
        List users's notification threads.

        Args:
            all: If true, show notifications marked as read. Default value is false
            status_types: Show notifications with the provided status types. Options are: unread, read and/or pinned.
                Defaults to unread & pinned.
            subject_type: filter notifications by subject type
            since: Only show notifications updated after the given time. This is a timestamp in RFC 3339 format
            before: Only show notifications updated before the given time. This is a timestamp in RFC 3339 format
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            NotificationThreadList.

        Operation ID: notifyGetList
        """
        _query: dict[str, object] = {
            "all": all,
            "status-types": status_types,
            "subject-type": subject_type,
            "since": None if since is None else since.isoformat(),
            "before": None if before is None else before.isoformat(),
        }

        return await self._client._paginate(
            "GET", "/notifications", model=NotificationThread, params=_query, page=page, limit=limit
        )

    async def update(
        self,
        *,
        last_read_at: datetime | None = None,
        all: bool | None = None,
        status_types: builtins.list[str] | None = None,
        to_status: str | None = None,
    ) -> None:
        """
        Mark notification threads as read, pinned or unread.

        Args:
            last_read_at: Describes the last point that notifications were checked. Anything updated since this time
                will not be updated.
            all: If true, mark all notifications on this repo. Default value is false
            status_types: Mark notifications with the provided status types. Options are: unread, read and/or pinned.
                Defaults to unread.
            to_status: Status to mark notifications as, Defaults to read.

        Returns:
            No content.

        Operation ID: notifyReadList
        """
        _query: dict[str, object] = {
            "last_read_at": None if last_read_at is None else last_read_at.isoformat(),
            "all": all,
            "status-types": status_types,
            "to-status": to_status,
        }

        _response = await self._client._request("PUT", "/notifications", params=_query)
        return decode(_response, None)

    async def new_count(self) -> NotificationCount:
        """
        Check if unread notifications exist.

        Returns:
            Number of unread notifications.

        Operation ID: notifyNewAvailable
        """
        _response = await self._client._request("GET", "/notifications/new")
        return decode(_response, NotificationCount)


class NotificationsThreads:
    """The ``notifications.threads`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def get(self, id: int) -> NotificationThread:
        """
        Get notification thread by ID.

        Args:
            id: id of notification thread

        Returns:
            NotificationThread.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: notifyGetThread
        """
        _response = self._client._request("GET", f"/notifications/threads/{id}")
        return decode(_response, NotificationThread)

    def update(self, id: int, *, to_status: str | None = None) -> None:
        """
        Mark notification thread as read by ID.

        Args:
            id: id of notification thread
            to_status: Status to mark notifications as

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: notifyReadThread
        """
        _query: dict[str, object] = {"to-status": to_status}

        _response = self._client._request("PATCH", f"/notifications/threads/{id}", params=_query)
        return decode(_response, None)


class AsyncNotificationsThreads:
    """The ``notifications.threads`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def get(self, id: int) -> NotificationThread:
        """
        Get notification thread by ID.

        Args:
            id: id of notification thread

        Returns:
            NotificationThread.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: notifyGetThread
        """
        _response = await self._client._request("GET", f"/notifications/threads/{id}")
        return decode(_response, NotificationThread)

    async def update(self, id: int, *, to_status: str | None = None) -> None:
        """
        Mark notification thread as read by ID.

        Args:
            id: id of notification thread
            to_status: Status to mark notifications as

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: notifyReadThread
        """
        _query: dict[str, object] = {"to-status": to_status}

        _response = await self._client._request("PATCH", f"/notifications/threads/{id}", params=_query)
        return decode(_response, None)
