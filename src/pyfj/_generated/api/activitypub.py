"""Generated resource namespaces for the ``activitypub`` group. Do not edit by hand.

Regenerate with ``python -m codegen``; see docs/development/codegen.md.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from pyfj._generated.models.activity_pub import ActivityPub
from pyfj._generated.models.forge_outbox import ForgeOutbox
from pyfj._runtime import decode

if TYPE_CHECKING:
    from pyfj._generated.models.forge_like import ForgeLike
    from pyfj._runtime import AsyncForgejo as _RuntimeAsyncForgejo
    from pyfj._runtime import Forgejo as _RuntimeForgejo


class Activitypub:
    """The ``activitypub`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client
        self.actor: ActivitypubActor = ActivitypubActor(client)
        self.person: ActivitypubPerson = ActivitypubPerson(client)
        self.repository: ActivitypubRepository = ActivitypubRepository(client)


class AsyncActivitypub:
    """The ``activitypub`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client
        self.actor: AsyncActivitypubActor = AsyncActivitypubActor(client)
        self.person: AsyncActivitypubPerson = AsyncActivitypubPerson(client)
        self.repository: AsyncActivitypubRepository = AsyncActivitypubRepository(client)


class ActivitypubActor:
    """The ``activitypub.actor`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def get(self) -> ActivityPub:
        """
        Returns the instance's Actor.

        Returns:
            ActivityPub.

        Operation ID: activitypubInstanceActor
        """
        _response = self._client._request("GET", "/activitypub/actor")
        return decode(_response, ActivityPub)

    def inbox(self) -> None:
        """
        Send to the inbox.

        Returns:
            No content.

        Operation ID: activitypubInstanceActorInbox
        """
        _response = self._client._request("POST", "/activitypub/actor/inbox")
        return decode(_response, None)

    def outbox(self) -> ForgeOutbox:
        """
        Display the outbox (always empty).

        Returns:
            Outbox.

        Operation ID: activitypubInstanceActorOutbox
        """
        _response = self._client._request("POST", "/activitypub/actor/outbox")
        return decode(_response, ForgeOutbox)


class AsyncActivitypubActor:
    """The ``activitypub.actor`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def get(self) -> ActivityPub:
        """
        Returns the instance's Actor.

        Returns:
            ActivityPub.

        Operation ID: activitypubInstanceActor
        """
        _response = await self._client._request("GET", "/activitypub/actor")
        return decode(_response, ActivityPub)

    async def inbox(self) -> None:
        """
        Send to the inbox.

        Returns:
            No content.

        Operation ID: activitypubInstanceActorInbox
        """
        _response = await self._client._request("POST", "/activitypub/actor/inbox")
        return decode(_response, None)

    async def outbox(self) -> ForgeOutbox:
        """
        Display the outbox (always empty).

        Returns:
            Outbox.

        Operation ID: activitypubInstanceActorOutbox
        """
        _response = await self._client._request("POST", "/activitypub/actor/outbox")
        return decode(_response, ForgeOutbox)


class ActivitypubPerson:
    """The ``activitypub.person`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client
        self.activities: ActivitypubPersonActivities = ActivitypubPersonActivities(client)

    def get(self, user_id: int) -> ActivityPub:
        """
        Returns the Person actor for a user.

        Args:
            user_id: user ID of the user

        Returns:
            ActivityPub.

        Operation ID: activitypubPerson
        """
        _response = self._client._request("GET", f"/activitypub/user-id/{user_id}")
        return decode(_response, ActivityPub)

    def inbox(self, user_id: int) -> None:
        """
        Send to the inbox.

        Args:
            user_id: user ID of the user

        Returns:
            No content.

        Operation ID: activitypubPersonInbox
        """
        _response = self._client._request("POST", f"/activitypub/user-id/{user_id}/inbox")
        return decode(_response, None)

    def outbox(self, user_id: int) -> ForgeOutbox:
        """
        List the user's recorded activity.

        Args:
            user_id: user ID of the user

        Returns:
            Outbox.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: activitypubPersonFeed
        """
        _response = self._client._request("GET", f"/activitypub/user-id/{user_id}/outbox")
        return decode(_response, ForgeOutbox)


class AsyncActivitypubPerson:
    """The ``activitypub.person`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client
        self.activities: AsyncActivitypubPersonActivities = AsyncActivitypubPersonActivities(client)

    async def get(self, user_id: int) -> ActivityPub:
        """
        Returns the Person actor for a user.

        Args:
            user_id: user ID of the user

        Returns:
            ActivityPub.

        Operation ID: activitypubPerson
        """
        _response = await self._client._request("GET", f"/activitypub/user-id/{user_id}")
        return decode(_response, ActivityPub)

    async def inbox(self, user_id: int) -> None:
        """
        Send to the inbox.

        Args:
            user_id: user ID of the user

        Returns:
            No content.

        Operation ID: activitypubPersonInbox
        """
        _response = await self._client._request("POST", f"/activitypub/user-id/{user_id}/inbox")
        return decode(_response, None)

    async def outbox(self, user_id: int) -> ForgeOutbox:
        """
        List the user's recorded activity.

        Args:
            user_id: user ID of the user

        Returns:
            Outbox.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: activitypubPersonFeed
        """
        _response = await self._client._request("GET", f"/activitypub/user-id/{user_id}/outbox")
        return decode(_response, ForgeOutbox)


class ActivitypubPersonActivities:
    """The ``activitypub.person.activities`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def get(self, user_id: int, activity_id: int) -> ActivityPub:
        """
        Get a specific activity object of the user.

        Args:
            user_id: user ID of the user
            activity_id: activity ID of the sought activity

        Returns:
            ActivityPub.

        Operation ID: activitypubPersonActivityNote
        """
        _response = self._client._request("GET", f"/activitypub/user-id/{user_id}/activities/{activity_id}")
        return decode(_response, ActivityPub)

    def activity(self, user_id: int, activity_id: int) -> ActivityPub:
        """
        Get a specific activity of the user.

        Args:
            user_id: user ID of the user
            activity_id: activity ID of the sought activity

        Returns:
            ActivityPub.

        Operation ID: activitypubPersonActivity
        """
        _response = self._client._request("GET", f"/activitypub/user-id/{user_id}/activities/{activity_id}/activity")
        return decode(_response, ActivityPub)


class AsyncActivitypubPersonActivities:
    """The ``activitypub.person.activities`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def get(self, user_id: int, activity_id: int) -> ActivityPub:
        """
        Get a specific activity object of the user.

        Args:
            user_id: user ID of the user
            activity_id: activity ID of the sought activity

        Returns:
            ActivityPub.

        Operation ID: activitypubPersonActivityNote
        """
        _response = await self._client._request("GET", f"/activitypub/user-id/{user_id}/activities/{activity_id}")
        return decode(_response, ActivityPub)

    async def activity(self, user_id: int, activity_id: int) -> ActivityPub:
        """
        Get a specific activity of the user.

        Args:
            user_id: user ID of the user
            activity_id: activity ID of the sought activity

        Returns:
            ActivityPub.

        Operation ID: activitypubPersonActivity
        """
        _response = await self._client._request(
            "GET", f"/activitypub/user-id/{user_id}/activities/{activity_id}/activity"
        )
        return decode(_response, ActivityPub)


class ActivitypubRepository:
    """The ``activitypub.repository`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def get(self, repository_id: int) -> ActivityPub:
        """
        Returns the Repository actor for a repo.

        Args:
            repository_id: repository ID of the repo

        Returns:
            ActivityPub.

        Operation ID: activitypubRepository
        """
        _response = self._client._request("GET", f"/activitypub/repository-id/{repository_id}")
        return decode(_response, ActivityPub)

    def inbox(self, repository_id: int, *, body: ForgeLike | None = None) -> None:
        """
        Send to the inbox.

        Args:
            repository_id: repository ID of the repo
            body: Full request body; the Spec declares no fields, so extra fields are allowed.

        Returns:
            No content.

        Operation ID: activitypubRepositoryInbox
        """
        _payload = None if body is None else body.model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("POST", f"/activitypub/repository-id/{repository_id}/inbox", json=_payload)
        return decode(_response, None)

    def outbox(self, repository_id: int) -> ForgeOutbox:
        """
        Display the outbox.

        Args:
            repository_id: repository ID of the repo

        Returns:
            Outbox.

        Operation ID: activitypubRepositoryOutbox
        """
        _response = self._client._request("POST", f"/activitypub/repository-id/{repository_id}/outbox")
        return decode(_response, ForgeOutbox)


class AsyncActivitypubRepository:
    """The ``activitypub.repository`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def get(self, repository_id: int) -> ActivityPub:
        """
        Returns the Repository actor for a repo.

        Args:
            repository_id: repository ID of the repo

        Returns:
            ActivityPub.

        Operation ID: activitypubRepository
        """
        _response = await self._client._request("GET", f"/activitypub/repository-id/{repository_id}")
        return decode(_response, ActivityPub)

    async def inbox(self, repository_id: int, *, body: ForgeLike | None = None) -> None:
        """
        Send to the inbox.

        Args:
            repository_id: repository ID of the repo
            body: Full request body; the Spec declares no fields, so extra fields are allowed.

        Returns:
            No content.

        Operation ID: activitypubRepositoryInbox
        """
        _payload = None if body is None else body.model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request(
            "POST", f"/activitypub/repository-id/{repository_id}/inbox", json=_payload
        )
        return decode(_response, None)

    async def outbox(self, repository_id: int) -> ForgeOutbox:
        """
        Display the outbox.

        Args:
            repository_id: repository ID of the repo

        Returns:
            Outbox.

        Operation ID: activitypubRepositoryOutbox
        """
        _response = await self._client._request("POST", f"/activitypub/repository-id/{repository_id}/outbox")
        return decode(_response, ForgeOutbox)
