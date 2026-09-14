"""Generated resource namespaces for the ``users`` group. Do not edit by hand.

Regenerate with ``python -m codegen``; see docs/development/codegen.md.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from pyfj._generated.models.access_token import AccessToken
from pyfj._generated.models.activity import Activity
from pyfj._generated.models.create_access_token_option import CreateAccessTokenOption
from pyfj._generated.models.gpg_key import GPGKey
from pyfj._generated.models.organization import Organization
from pyfj._generated.models.organization_permissions import OrganizationPermissions
from pyfj._generated.models.public_key import PublicKey
from pyfj._generated.models.repository import Repository
from pyfj._generated.models.user import User
from pyfj._generated.models.user_heatmap_data import UserHeatmapData
from pyfj._generated.models.user_search_results import UserSearchResults
from pyfj._runtime import decode

if TYPE_CHECKING:
    import builtins
    from datetime import date
    from typing import Literal

    from pyfj._generated.models.repo_target_option import RepoTargetOption
    from pyfj._runtime import AsyncForgejo as _RuntimeAsyncForgejo
    from pyfj._runtime import AsyncPaginated, Paginated
    from pyfj._runtime import Forgejo as _RuntimeForgejo


class Users:
    """The ``users`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client
        self.activities: UsersActivities = UsersActivities(client)
        self.following: UsersFollowing = UsersFollowing(client)
        self.orgs: UsersOrgs = UsersOrgs(client)
        self.tokens: UsersTokens = UsersTokens(client)

    def search(
        self,
        *,
        q: str | None = None,
        uid: int | None = None,
        sort: Literal["oldest", "newest", "alphabetically", "reversealphabetically", "recentupdate", "leastupdate"]
        | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> UserSearchResults:
        """
        Search for users.

        Args:
            q: keyword
            uid: ID of the user to search for
            sort: sort order of results
            page: page number of results to return (1-based)
            limit: page size of results

        Returns:
            SearchResults of a successful search.

        Operation ID: userSearch
        """
        _query: dict[str, object] = {"q": q, "uid": uid, "sort": sort, "page": page, "limit": limit}

        _response = self._client._request("GET", "/users/search", params=_query)
        return decode(_response, UserSearchResults)

    def get(self, username: str) -> User:
        """
        Get a user.

        Args:
            username: username of user to get

        Returns:
            User.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: userGet
        """
        _response = self._client._request("GET", f"/users/{username}")
        return decode(_response, User)

    def followers(self, username: str, *, page: int | None = None, limit: int | None = None) -> Paginated[User]:
        """
        List the given user's followers.

        Args:
            username: username of user
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            UserList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: userListFollowers
        """
        return self._client._paginate("GET", f"/users/{username}/followers", model=User, page=page, limit=limit)

    def gpg_keys(self, username: str, *, page: int | None = None, limit: int | None = None) -> Paginated[GPGKey]:
        """
        List the given user's GPG keys.

        Args:
            username: username of user
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            GPGKeyList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: userListGPGKeys
        """
        return self._client._paginate("GET", f"/users/{username}/gpg_keys", model=GPGKey, page=page, limit=limit)

    def heatmap(self, username: str) -> builtins.list[UserHeatmapData]:
        """
        Get a user's heatmap.

        Args:
            username: username of user to get

        Returns:
            UserHeatmapData.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: userGetHeatmapData
        """
        _response = self._client._request("GET", f"/users/{username}/heatmap")
        return decode(_response, list[UserHeatmapData])

    def keys(
        self,
        username: str,
        *,
        fingerprint: str | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> Paginated[PublicKey]:
        """
        List the given user's public keys.

        Args:
            username: username of user
            fingerprint: fingerprint of the key
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            PublicKeyList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: userListKeys
        """
        _query: dict[str, object] = {"fingerprint": fingerprint}

        return self._client._paginate(
            "GET", f"/users/{username}/keys", model=PublicKey, params=_query, page=page, limit=limit
        )

    def repos(self, username: str, *, page: int | None = None, limit: int | None = None) -> Paginated[Repository]:
        """
        List the repos owned by the given user.

        Args:
            username: username of user
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            RepositoryList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: userListRepos
        """
        return self._client._paginate("GET", f"/users/{username}/repos", model=Repository, page=page, limit=limit)

    def starred(self, username: str, *, page: int | None = None, limit: int | None = None) -> Paginated[Repository]:
        """
        The repos that the given user has starred.

        Args:
            username: username of user
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            RepositoryList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: userListStarred
        """
        return self._client._paginate("GET", f"/users/{username}/starred", model=Repository, page=page, limit=limit)

    def subscriptions(
        self,
        username: str,
        *,
        page: int | None = None,
        limit: int | None = None,
    ) -> Paginated[Repository]:
        """
        List the repositories watched by a user.

        Args:
            username: username of the user
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            RepositoryList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: userListSubscriptions
        """
        return self._client._paginate(
            "GET", f"/users/{username}/subscriptions", model=Repository, page=page, limit=limit
        )


class AsyncUsers:
    """The ``users`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client
        self.activities: AsyncUsersActivities = AsyncUsersActivities(client)
        self.following: AsyncUsersFollowing = AsyncUsersFollowing(client)
        self.orgs: AsyncUsersOrgs = AsyncUsersOrgs(client)
        self.tokens: AsyncUsersTokens = AsyncUsersTokens(client)

    async def search(
        self,
        *,
        q: str | None = None,
        uid: int | None = None,
        sort: Literal["oldest", "newest", "alphabetically", "reversealphabetically", "recentupdate", "leastupdate"]
        | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> UserSearchResults:
        """
        Search for users.

        Args:
            q: keyword
            uid: ID of the user to search for
            sort: sort order of results
            page: page number of results to return (1-based)
            limit: page size of results

        Returns:
            SearchResults of a successful search.

        Operation ID: userSearch
        """
        _query: dict[str, object] = {"q": q, "uid": uid, "sort": sort, "page": page, "limit": limit}

        _response = await self._client._request("GET", "/users/search", params=_query)
        return decode(_response, UserSearchResults)

    async def get(self, username: str) -> User:
        """
        Get a user.

        Args:
            username: username of user to get

        Returns:
            User.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: userGet
        """
        _response = await self._client._request("GET", f"/users/{username}")
        return decode(_response, User)

    async def followers(
        self,
        username: str,
        *,
        page: int | None = None,
        limit: int | None = None,
    ) -> AsyncPaginated[User]:
        """
        List the given user's followers.

        Args:
            username: username of user
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            UserList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: userListFollowers
        """
        return await self._client._paginate("GET", f"/users/{username}/followers", model=User, page=page, limit=limit)

    async def gpg_keys(
        self,
        username: str,
        *,
        page: int | None = None,
        limit: int | None = None,
    ) -> AsyncPaginated[GPGKey]:
        """
        List the given user's GPG keys.

        Args:
            username: username of user
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            GPGKeyList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: userListGPGKeys
        """
        return await self._client._paginate("GET", f"/users/{username}/gpg_keys", model=GPGKey, page=page, limit=limit)

    async def heatmap(self, username: str) -> builtins.list[UserHeatmapData]:
        """
        Get a user's heatmap.

        Args:
            username: username of user to get

        Returns:
            UserHeatmapData.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: userGetHeatmapData
        """
        _response = await self._client._request("GET", f"/users/{username}/heatmap")
        return decode(_response, list[UserHeatmapData])

    async def keys(
        self,
        username: str,
        *,
        fingerprint: str | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> AsyncPaginated[PublicKey]:
        """
        List the given user's public keys.

        Args:
            username: username of user
            fingerprint: fingerprint of the key
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            PublicKeyList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: userListKeys
        """
        _query: dict[str, object] = {"fingerprint": fingerprint}

        return await self._client._paginate(
            "GET", f"/users/{username}/keys", model=PublicKey, params=_query, page=page, limit=limit
        )

    async def repos(
        self,
        username: str,
        *,
        page: int | None = None,
        limit: int | None = None,
    ) -> AsyncPaginated[Repository]:
        """
        List the repos owned by the given user.

        Args:
            username: username of user
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            RepositoryList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: userListRepos
        """
        return await self._client._paginate("GET", f"/users/{username}/repos", model=Repository, page=page, limit=limit)

    async def starred(
        self,
        username: str,
        *,
        page: int | None = None,
        limit: int | None = None,
    ) -> AsyncPaginated[Repository]:
        """
        The repos that the given user has starred.

        Args:
            username: username of user
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            RepositoryList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: userListStarred
        """
        return await self._client._paginate(
            "GET", f"/users/{username}/starred", model=Repository, page=page, limit=limit
        )

    async def subscriptions(
        self,
        username: str,
        *,
        page: int | None = None,
        limit: int | None = None,
    ) -> AsyncPaginated[Repository]:
        """
        List the repositories watched by a user.

        Args:
            username: username of the user
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            RepositoryList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: userListSubscriptions
        """
        return await self._client._paginate(
            "GET", f"/users/{username}/subscriptions", model=Repository, page=page, limit=limit
        )


class UsersActivities:
    """The ``users.activities`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def feeds(
        self,
        username: str,
        *,
        only_performed_by: bool | None = None,
        date: date | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> Paginated[Activity]:
        """
        List a user's activity feeds.

        Args:
            username: username of user
            only_performed_by: if true, only show actions performed by the requested user
            date: the date of the activities to be found
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            ActivityFeedsList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: userListActivityFeeds
        """
        _query: dict[str, object] = {
            "only-performed-by": only_performed_by,
            "date": None if date is None else date.isoformat(),
        }

        return self._client._paginate(
            "GET", f"/users/{username}/activities/feeds", model=Activity, params=_query, page=page, limit=limit
        )


class AsyncUsersActivities:
    """The ``users.activities`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def feeds(
        self,
        username: str,
        *,
        only_performed_by: bool | None = None,
        date: date | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> AsyncPaginated[Activity]:
        """
        List a user's activity feeds.

        Args:
            username: username of user
            only_performed_by: if true, only show actions performed by the requested user
            date: the date of the activities to be found
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            ActivityFeedsList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: userListActivityFeeds
        """
        _query: dict[str, object] = {
            "only-performed-by": only_performed_by,
            "date": None if date is None else date.isoformat(),
        }

        return await self._client._paginate(
            "GET", f"/users/{username}/activities/feeds", model=Activity, params=_query, page=page, limit=limit
        )


class UsersFollowing:
    """The ``users.following`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(self, username: str, *, page: int | None = None, limit: int | None = None) -> Paginated[User]:
        """
        List the users that the given user is following.

        Args:
            username: username of user
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            UserList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: userListFollowing
        """
        return self._client._paginate("GET", f"/users/{username}/following", model=User, page=page, limit=limit)

    def get(self, username: str, target: str) -> None:
        """
        Check if one user is following another user.

        Args:
            username: username of following user
            target: username of followed user

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: userCheckFollowing
        """
        _response = self._client._request("GET", f"/users/{username}/following/{target}")
        return decode(_response, None)


class AsyncUsersFollowing:
    """The ``users.following`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(self, username: str, *, page: int | None = None, limit: int | None = None) -> AsyncPaginated[User]:
        """
        List the users that the given user is following.

        Args:
            username: username of user
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            UserList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: userListFollowing
        """
        return await self._client._paginate("GET", f"/users/{username}/following", model=User, page=page, limit=limit)

    async def get(self, username: str, target: str) -> None:
        """
        Check if one user is following another user.

        Args:
            username: username of following user
            target: username of followed user

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: userCheckFollowing
        """
        _response = await self._client._request("GET", f"/users/{username}/following/{target}")
        return decode(_response, None)


class UsersOrgs:
    """The ``users.orgs`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(self, username: str, *, page: int | None = None, limit: int | None = None) -> Paginated[Organization]:
        """
        List a user's organizations.

        Args:
            username: username of user
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            OrganizationListWithoutPagination - Organizations without pagination headers.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgListUserOrgs
        """
        return self._client._paginate("GET", f"/users/{username}/orgs", model=Organization, page=page, limit=limit)

    def permissions(self, username: str, org: str) -> OrganizationPermissions:
        """
        Get user permissions in organization.

        Args:
            username: username of user
            org: name of the organization

        Returns:
            OrganizationPermissions.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgGetUserPermissions
        """
        _response = self._client._request("GET", f"/users/{username}/orgs/{org}/permissions")
        return decode(_response, OrganizationPermissions)


class AsyncUsersOrgs:
    """The ``users.orgs`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(
        self,
        username: str,
        *,
        page: int | None = None,
        limit: int | None = None,
    ) -> AsyncPaginated[Organization]:
        """
        List a user's organizations.

        Args:
            username: username of user
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            OrganizationListWithoutPagination - Organizations without pagination headers.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgListUserOrgs
        """
        return await self._client._paginate(
            "GET", f"/users/{username}/orgs", model=Organization, page=page, limit=limit
        )

    async def permissions(self, username: str, org: str) -> OrganizationPermissions:
        """
        Get user permissions in organization.

        Args:
            username: username of user
            org: name of the organization

        Returns:
            OrganizationPermissions.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgGetUserPermissions
        """
        _response = await self._client._request("GET", f"/users/{username}/orgs/{org}/permissions")
        return decode(_response, OrganizationPermissions)


class UsersTokens:
    """The ``users.tokens`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(self, username: str, *, page: int | None = None, limit: int | None = None) -> Paginated[AccessToken]:
        """
        List the specified user's access tokens.

        Args:
            username: username of user
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            AccessTokenList.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: userGetTokens
        """
        return self._client._paginate("GET", f"/users/{username}/tokens", model=AccessToken, page=page, limit=limit)

    def create(
        self,
        username: str,
        *,
        name: str,
        repositories: builtins.list[RepoTargetOption] | None = None,
        scopes: builtins.list[str] | None = None,
    ) -> AccessToken:
        """
        Generate an access token for the specified user.

        Args:
            username: username of user
            name:
            repositories: If provided and not-empty, creates an access token with access only to specified repositories.
            scopes:

        Returns:
            AccessToken represents an API access token.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: userCreateToken
        """
        _payload = CreateAccessTokenOption(
            name=name,
            repositories=repositories,
            scopes=scopes,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("POST", f"/users/{username}/tokens", json=_payload)
        return decode(_response, AccessToken)

    def delete(self, username: str, token: str) -> None:
        """
        Delete an access token from the specified user's account.

        Args:
            username: username of user
            token: token to be deleted, identified by ID and if not available by name

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIError is error format response.

        Operation ID: userDeleteAccessToken
        """
        _response = self._client._request("DELETE", f"/users/{username}/tokens/{token}")
        return decode(_response, None)


class AsyncUsersTokens:
    """The ``users.tokens`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(
        self,
        username: str,
        *,
        page: int | None = None,
        limit: int | None = None,
    ) -> AsyncPaginated[AccessToken]:
        """
        List the specified user's access tokens.

        Args:
            username: username of user
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            AccessTokenList.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: userGetTokens
        """
        return await self._client._paginate(
            "GET", f"/users/{username}/tokens", model=AccessToken, page=page, limit=limit
        )

    async def create(
        self,
        username: str,
        *,
        name: str,
        repositories: builtins.list[RepoTargetOption] | None = None,
        scopes: builtins.list[str] | None = None,
    ) -> AccessToken:
        """
        Generate an access token for the specified user.

        Args:
            username: username of user
            name:
            repositories: If provided and not-empty, creates an access token with access only to specified repositories.
            scopes:

        Returns:
            AccessToken represents an API access token.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: userCreateToken
        """
        _payload = CreateAccessTokenOption(
            name=name,
            repositories=repositories,
            scopes=scopes,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request("POST", f"/users/{username}/tokens", json=_payload)
        return decode(_response, AccessToken)

    async def delete(self, username: str, token: str) -> None:
        """
        Delete an access token from the specified user's account.

        Args:
            username: username of user
            token: token to be deleted, identified by ID and if not available by name

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIError is error format response.

        Operation ID: userDeleteAccessToken
        """
        _response = await self._client._request("DELETE", f"/users/{username}/tokens/{token}")
        return decode(_response, None)
