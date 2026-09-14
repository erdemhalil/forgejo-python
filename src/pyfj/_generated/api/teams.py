"""Generated resource namespaces for the ``teams`` group. Do not edit by hand.

Regenerate with ``python -m codegen``; see docs/development/codegen.md.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from pyfj._generated.models.activity import Activity
from pyfj._generated.models.edit_team_option import EditTeamOption
from pyfj._generated.models.repository import Repository
from pyfj._generated.models.team import Team
from pyfj._generated.models.user import User
from pyfj._runtime import decode

if TYPE_CHECKING:
    import builtins
    from datetime import date

    from pyfj._generated.models.edit_team_option import EditTeamOptionPermission
    from pyfj._runtime import AsyncForgejo as _RuntimeAsyncForgejo
    from pyfj._runtime import AsyncPaginated, Paginated
    from pyfj._runtime import Forgejo as _RuntimeForgejo


class Teams:
    """The ``teams`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client
        self.activities: TeamsActivities = TeamsActivities(client)
        self.members: TeamsMembers = TeamsMembers(client)
        self.repos: TeamsRepos = TeamsRepos(client)

    def get(self, id: int) -> Team:
        """
        Get a team.

        Args:
            id: id of the team to get

        Returns:
            Team.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgGetTeam
        """
        _response = self._client._request("GET", f"/teams/{id}")
        return decode(_response, Team)

    def update(
        self,
        id: int,
        *,
        can_create_org_repo: bool | None = None,
        description: str | None = None,
        includes_all_repositories: bool | None = None,
        name: str,
        permission: EditTeamOptionPermission | None = None,
        units: builtins.list[str] | None = None,
        units_map: dict[str, str] | None = None,
    ) -> Team:
        """
        Edit a team.

        Args:
            id: id of the team to edit
            can_create_org_repo:
            description:
            includes_all_repositories:
            name:
            permission:
            units:
            units_map:

        Returns:
            Team.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgEditTeam
        """
        _payload = EditTeamOption(
            can_create_org_repo=can_create_org_repo,
            description=description,
            includes_all_repositories=includes_all_repositories,
            name=name,
            permission=permission,
            units=units,
            units_map=units_map,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("PATCH", f"/teams/{id}", json=_payload)
        return decode(_response, Team)

    def delete(self, id: int) -> None:
        """
        Delete a team.

        Args:
            id: id of the team to delete

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgDeleteTeam
        """
        _response = self._client._request("DELETE", f"/teams/{id}")
        return decode(_response, None)


class AsyncTeams:
    """The ``teams`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client
        self.activities: AsyncTeamsActivities = AsyncTeamsActivities(client)
        self.members: AsyncTeamsMembers = AsyncTeamsMembers(client)
        self.repos: AsyncTeamsRepos = AsyncTeamsRepos(client)

    async def get(self, id: int) -> Team:
        """
        Get a team.

        Args:
            id: id of the team to get

        Returns:
            Team.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgGetTeam
        """
        _response = await self._client._request("GET", f"/teams/{id}")
        return decode(_response, Team)

    async def update(
        self,
        id: int,
        *,
        can_create_org_repo: bool | None = None,
        description: str | None = None,
        includes_all_repositories: bool | None = None,
        name: str,
        permission: EditTeamOptionPermission | None = None,
        units: builtins.list[str] | None = None,
        units_map: dict[str, str] | None = None,
    ) -> Team:
        """
        Edit a team.

        Args:
            id: id of the team to edit
            can_create_org_repo:
            description:
            includes_all_repositories:
            name:
            permission:
            units:
            units_map:

        Returns:
            Team.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgEditTeam
        """
        _payload = EditTeamOption(
            can_create_org_repo=can_create_org_repo,
            description=description,
            includes_all_repositories=includes_all_repositories,
            name=name,
            permission=permission,
            units=units,
            units_map=units_map,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request("PATCH", f"/teams/{id}", json=_payload)
        return decode(_response, Team)

    async def delete(self, id: int) -> None:
        """
        Delete a team.

        Args:
            id: id of the team to delete

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgDeleteTeam
        """
        _response = await self._client._request("DELETE", f"/teams/{id}")
        return decode(_response, None)


class TeamsActivities:
    """The ``teams.activities`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def feeds(
        self,
        id: int,
        *,
        date: date | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> Paginated[Activity]:
        """
        List a team's activity feeds.

        Args:
            id: id of the team
            date: the date of the activities to be found
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            ActivityFeedsList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgListTeamActivityFeeds
        """
        _query: dict[str, object] = {"date": None if date is None else date.isoformat()}

        return self._client._paginate(
            "GET", f"/teams/{id}/activities/feeds", model=Activity, params=_query, page=page, limit=limit
        )


class AsyncTeamsActivities:
    """The ``teams.activities`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def feeds(
        self,
        id: int,
        *,
        date: date | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> AsyncPaginated[Activity]:
        """
        List a team's activity feeds.

        Args:
            id: id of the team
            date: the date of the activities to be found
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            ActivityFeedsList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgListTeamActivityFeeds
        """
        _query: dict[str, object] = {"date": None if date is None else date.isoformat()}

        return await self._client._paginate(
            "GET", f"/teams/{id}/activities/feeds", model=Activity, params=_query, page=page, limit=limit
        )


class TeamsMembers:
    """The ``teams.members`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(self, id: int, *, page: int | None = None, limit: int | None = None) -> Paginated[User]:
        """
        List a team's members.

        Args:
            id: id of the team
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            UserList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgListTeamMembers
        """
        return self._client._paginate("GET", f"/teams/{id}/members", model=User, page=page, limit=limit)

    def get(self, id: int, username: str) -> User:
        """
        List a particular member of team.

        Args:
            id: id of the team
            username: username of the member to list

        Returns:
            User.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgListTeamMember
        """
        _response = self._client._request("GET", f"/teams/{id}/members/{username}")
        return decode(_response, User)

    def add(self, id: int, username: str) -> None:
        """
        Add a team member.

        Args:
            id: id of the team
            username: username of the user to add

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgAddTeamMember
        """
        _response = self._client._request("PUT", f"/teams/{id}/members/{username}")
        return decode(_response, None)

    def remove(self, id: int, username: str) -> None:
        """
        Remove a team member.

        Args:
            id: id of the team
            username: username of the user to remove

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgRemoveTeamMember
        """
        _response = self._client._request("DELETE", f"/teams/{id}/members/{username}")
        return decode(_response, None)


class AsyncTeamsMembers:
    """The ``teams.members`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(self, id: int, *, page: int | None = None, limit: int | None = None) -> AsyncPaginated[User]:
        """
        List a team's members.

        Args:
            id: id of the team
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            UserList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgListTeamMembers
        """
        return await self._client._paginate("GET", f"/teams/{id}/members", model=User, page=page, limit=limit)

    async def get(self, id: int, username: str) -> User:
        """
        List a particular member of team.

        Args:
            id: id of the team
            username: username of the member to list

        Returns:
            User.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgListTeamMember
        """
        _response = await self._client._request("GET", f"/teams/{id}/members/{username}")
        return decode(_response, User)

    async def add(self, id: int, username: str) -> None:
        """
        Add a team member.

        Args:
            id: id of the team
            username: username of the user to add

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgAddTeamMember
        """
        _response = await self._client._request("PUT", f"/teams/{id}/members/{username}")
        return decode(_response, None)

    async def remove(self, id: int, username: str) -> None:
        """
        Remove a team member.

        Args:
            id: id of the team
            username: username of the user to remove

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgRemoveTeamMember
        """
        _response = await self._client._request("DELETE", f"/teams/{id}/members/{username}")
        return decode(_response, None)


class TeamsRepos:
    """The ``teams.repos`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(self, id: int, *, page: int | None = None, limit: int | None = None) -> Paginated[Repository]:
        """
        List a team's repos.

        Args:
            id: id of the team
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            RepositoryList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgListTeamRepos
        """
        return self._client._paginate("GET", f"/teams/{id}/repos", model=Repository, page=page, limit=limit)

    def get(self, id: int, org: str, repo: str) -> Repository:
        """
        List a particular repo of team.

        Args:
            id: id of the team
            org: organization that owns the repo to list
            repo: name of the repo to list

        Returns:
            Repository.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgListTeamRepo
        """
        _response = self._client._request("GET", f"/teams/{id}/repos/{org}/{repo}")
        return decode(_response, Repository)

    def add(self, id: int, org: str, repo: str) -> None:
        """
        Add a repository to a team.

        Args:
            id: id of the team
            org: organization that owns the repo to add
            repo: name of the repo to add

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgAddTeamRepository
        """
        _response = self._client._request("PUT", f"/teams/{id}/repos/{org}/{repo}")
        return decode(_response, None)

    def remove(self, id: int, org: str, repo: str) -> None:
        """
        Remove a repository from a team.

        This does not delete the repository, it only removes the repository from the team.

        Args:
            id: id of the team
            org: organization that owns the repo to remove
            repo: name of the repo to remove

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgRemoveTeamRepository
        """
        _response = self._client._request("DELETE", f"/teams/{id}/repos/{org}/{repo}")
        return decode(_response, None)


class AsyncTeamsRepos:
    """The ``teams.repos`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(self, id: int, *, page: int | None = None, limit: int | None = None) -> AsyncPaginated[Repository]:
        """
        List a team's repos.

        Args:
            id: id of the team
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            RepositoryList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgListTeamRepos
        """
        return await self._client._paginate("GET", f"/teams/{id}/repos", model=Repository, page=page, limit=limit)

    async def get(self, id: int, org: str, repo: str) -> Repository:
        """
        List a particular repo of team.

        Args:
            id: id of the team
            org: organization that owns the repo to list
            repo: name of the repo to list

        Returns:
            Repository.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgListTeamRepo
        """
        _response = await self._client._request("GET", f"/teams/{id}/repos/{org}/{repo}")
        return decode(_response, Repository)

    async def add(self, id: int, org: str, repo: str) -> None:
        """
        Add a repository to a team.

        Args:
            id: id of the team
            org: organization that owns the repo to add
            repo: name of the repo to add

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgAddTeamRepository
        """
        _response = await self._client._request("PUT", f"/teams/{id}/repos/{org}/{repo}")
        return decode(_response, None)

    async def remove(self, id: int, org: str, repo: str) -> None:
        """
        Remove a repository from a team.

        This does not delete the repository, it only removes the repository from the team.

        Args:
            id: id of the team
            org: organization that owns the repo to remove
            repo: name of the repo to remove

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgRemoveTeamRepository
        """
        _response = await self._client._request("DELETE", f"/teams/{id}/repos/{org}/{repo}")
        return decode(_response, None)
