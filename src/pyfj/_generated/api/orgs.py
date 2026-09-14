"""Generated resource namespaces for the ``orgs`` group. Do not edit by hand.

Regenerate with ``python -m codegen``; see docs/development/codegen.md.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from pyfj._generated.models.action_run_job import ActionRunJob
from pyfj._generated.models.action_runner import ActionRunner
from pyfj._generated.models.action_variable import ActionVariable
from pyfj._generated.models.activity import Activity
from pyfj._generated.models.blocked_user import BlockedUser
from pyfj._generated.models.create_hook_option import CreateHookOption
from pyfj._generated.models.create_label_option import CreateLabelOption
from pyfj._generated.models.create_or_update_secret_option import CreateOrUpdateSecretOption
from pyfj._generated.models.create_org_option import CreateOrgOption
from pyfj._generated.models.create_repo_option import CreateRepoOption
from pyfj._generated.models.create_team_option import CreateTeamOption
from pyfj._generated.models.create_variable_option import CreateVariableOption
from pyfj._generated.models.edit_hook_option import EditHookOption
from pyfj._generated.models.edit_label_option import EditLabelOption
from pyfj._generated.models.edit_org_option import EditOrgOption
from pyfj._generated.models.hook import Hook
from pyfj._generated.models.label import Label
from pyfj._generated.models.organization import Organization
from pyfj._generated.models.quota_info import QuotaInfo
from pyfj._generated.models.quota_used_artifact import QuotaUsedArtifact
from pyfj._generated.models.quota_used_attachment import QuotaUsedAttachment
from pyfj._generated.models.quota_used_package import QuotaUsedPackage
from pyfj._generated.models.register_runner_options import RegisterRunnerOptions
from pyfj._generated.models.register_runner_response import RegisterRunnerResponse
from pyfj._generated.models.registration_token import RegistrationToken
from pyfj._generated.models.rename_org_option import RenameOrgOption
from pyfj._generated.models.repository import Repository
from pyfj._generated.models.secret import Secret
from pyfj._generated.models.team import Team
from pyfj._generated.models.team_search_results import TeamSearchResults
from pyfj._generated.models.update_user_avatar_option import UpdateUserAvatarOption
from pyfj._generated.models.update_variable_option import UpdateVariableOption
from pyfj._generated.models.user import User
from pyfj._runtime import decode

if TYPE_CHECKING:
    import builtins
    from datetime import date
    from typing import Literal

    from pyfj._generated.models.create_hook_option import CreateHookOptionType
    from pyfj._generated.models.create_hook_option_config import CreateHookOptionConfig
    from pyfj._generated.models.create_org_option import CreateOrgOptionVisibility
    from pyfj._generated.models.create_repo_option import CreateRepoOptionObjectFormatName, CreateRepoOptionTrustModel
    from pyfj._generated.models.create_team_option import CreateTeamOptionPermission
    from pyfj._generated.models.edit_org_option import EditOrgOptionVisibility
    from pyfj._runtime import AsyncForgejo as _RuntimeAsyncForgejo
    from pyfj._runtime import AsyncPaginated, Paginated
    from pyfj._runtime import Forgejo as _RuntimeForgejo


class Orgs:
    """The ``orgs`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client
        self.actions: OrgsActions = OrgsActions(client)
        self.activities: OrgsActivities = OrgsActivities(client)
        self.avatar: OrgsAvatar = OrgsAvatar(client)
        self.hooks: OrgsHooks = OrgsHooks(client)
        self.labels: OrgsLabels = OrgsLabels(client)
        self.members: OrgsMembers = OrgsMembers(client)
        self.public_members: OrgsPublicMembers = OrgsPublicMembers(client)
        self.quota: OrgsQuota = OrgsQuota(client)
        self.repos: OrgsRepos = OrgsRepos(client)
        self.teams: OrgsTeams = OrgsTeams(client)

    def list(self, *, page: int | None = None, limit: int | None = None) -> Paginated[Organization]:
        """
        List all organizations.

        Args:
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            OrganizationList.

        Operation ID: orgGetAll
        """
        return self._client._paginate("GET", "/orgs", model=Organization, page=page, limit=limit)

    def create(
        self,
        *,
        description: str | None = None,
        email: str | None = None,
        full_name: str | None = None,
        location: str | None = None,
        repo_admin_change_team_access: bool | None = None,
        username: str,
        visibility: CreateOrgOptionVisibility | None = None,
        website: str | None = None,
    ) -> Organization:
        """
        Create an organization.

        Args:
            description:
            email:
            full_name:
            location:
            repo_admin_change_team_access:
            username:
            visibility: possible values are `public` (default), `limited` or `private`
            website:

        Returns:
            Organization.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: orgCreate
        """
        _payload = CreateOrgOption(
            description=description,
            email=email,
            full_name=full_name,
            location=location,
            repo_admin_change_team_access=repo_admin_change_team_access,
            username=username,
            visibility=visibility,
            website=website,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("POST", "/orgs", json=_payload)
        return decode(_response, Organization)

    def get(self, org: str) -> Organization:
        """
        Get an organization.

        Args:
            org: name of the organization to get

        Returns:
            Organization.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgGet
        """
        _response = self._client._request("GET", f"/orgs/{org}")
        return decode(_response, Organization)

    def update(
        self,
        org: str,
        *,
        description: str | None = None,
        email: str | None = None,
        full_name: str | None = None,
        location: str | None = None,
        repo_admin_change_team_access: bool | None = None,
        visibility: EditOrgOptionVisibility | None = None,
        website: str | None = None,
    ) -> Organization:
        """
        Edit an organization.

        Args:
            org: name of the organization to edit
            description:
            email:
            full_name:
            location:
            repo_admin_change_team_access:
            visibility: possible values are `public`, `limited` or `private`
            website:

        Returns:
            Organization.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIError is error format response.

        Operation ID: orgEdit
        """
        _payload = EditOrgOption(
            description=description,
            email=email,
            full_name=full_name,
            location=location,
            repo_admin_change_team_access=repo_admin_change_team_access,
            visibility=visibility,
            website=website,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("PATCH", f"/orgs/{org}", json=_payload)
        return decode(_response, Organization)

    def delete(self, org: str) -> None:
        """
        Delete an organization.

        Args:
            org: organization that is to be deleted

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgDelete
        """
        _response = self._client._request("DELETE", f"/orgs/{org}")
        return decode(_response, None)

    def block(self, org: str, username: str) -> None:
        """
        Blocks a user from the organization.

        Args:
            org: name of the org
            username: username of the user

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: orgBlockUser
        """
        _response = self._client._request("PUT", f"/orgs/{org}/block/{username}")
        return decode(_response, None)

    def list_blocked(self, org: str, *, page: int | None = None, limit: int | None = None) -> Paginated[BlockedUser]:
        """
        List the organization's blocked users.

        Args:
            org: name of the org
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            BlockedUserList.

        Operation ID: orgListBlockedUsers
        """
        return self._client._paginate("GET", f"/orgs/{org}/list_blocked", model=BlockedUser, page=page, limit=limit)

    def rename(self, org: str, *, new_name: str) -> None:
        """
        Rename an organization.

        Args:
            org: existing org name
            new_name: New username for this org. This name cannot be in use yet by any other user.

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: renameOrg
        """
        _payload = RenameOrgOption(
            new_name=new_name,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("POST", f"/orgs/{org}/rename", json=_payload)
        return decode(_response, None)

    def unblock(self, org: str, username: str) -> None:
        """
        Unblock a user from the organization.

        Args:
            org: name of the org
            username: username of the user

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: orgUnblockUser
        """
        _response = self._client._request("PUT", f"/orgs/{org}/unblock/{username}")
        return decode(_response, None)


class AsyncOrgs:
    """The ``orgs`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client
        self.actions: AsyncOrgsActions = AsyncOrgsActions(client)
        self.activities: AsyncOrgsActivities = AsyncOrgsActivities(client)
        self.avatar: AsyncOrgsAvatar = AsyncOrgsAvatar(client)
        self.hooks: AsyncOrgsHooks = AsyncOrgsHooks(client)
        self.labels: AsyncOrgsLabels = AsyncOrgsLabels(client)
        self.members: AsyncOrgsMembers = AsyncOrgsMembers(client)
        self.public_members: AsyncOrgsPublicMembers = AsyncOrgsPublicMembers(client)
        self.quota: AsyncOrgsQuota = AsyncOrgsQuota(client)
        self.repos: AsyncOrgsRepos = AsyncOrgsRepos(client)
        self.teams: AsyncOrgsTeams = AsyncOrgsTeams(client)

    async def list(self, *, page: int | None = None, limit: int | None = None) -> AsyncPaginated[Organization]:
        """
        List all organizations.

        Args:
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            OrganizationList.

        Operation ID: orgGetAll
        """
        return await self._client._paginate("GET", "/orgs", model=Organization, page=page, limit=limit)

    async def create(
        self,
        *,
        description: str | None = None,
        email: str | None = None,
        full_name: str | None = None,
        location: str | None = None,
        repo_admin_change_team_access: bool | None = None,
        username: str,
        visibility: CreateOrgOptionVisibility | None = None,
        website: str | None = None,
    ) -> Organization:
        """
        Create an organization.

        Args:
            description:
            email:
            full_name:
            location:
            repo_admin_change_team_access:
            username:
            visibility: possible values are `public` (default), `limited` or `private`
            website:

        Returns:
            Organization.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: orgCreate
        """
        _payload = CreateOrgOption(
            description=description,
            email=email,
            full_name=full_name,
            location=location,
            repo_admin_change_team_access=repo_admin_change_team_access,
            username=username,
            visibility=visibility,
            website=website,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request("POST", "/orgs", json=_payload)
        return decode(_response, Organization)

    async def get(self, org: str) -> Organization:
        """
        Get an organization.

        Args:
            org: name of the organization to get

        Returns:
            Organization.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgGet
        """
        _response = await self._client._request("GET", f"/orgs/{org}")
        return decode(_response, Organization)

    async def update(
        self,
        org: str,
        *,
        description: str | None = None,
        email: str | None = None,
        full_name: str | None = None,
        location: str | None = None,
        repo_admin_change_team_access: bool | None = None,
        visibility: EditOrgOptionVisibility | None = None,
        website: str | None = None,
    ) -> Organization:
        """
        Edit an organization.

        Args:
            org: name of the organization to edit
            description:
            email:
            full_name:
            location:
            repo_admin_change_team_access:
            visibility: possible values are `public`, `limited` or `private`
            website:

        Returns:
            Organization.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIError is error format response.

        Operation ID: orgEdit
        """
        _payload = EditOrgOption(
            description=description,
            email=email,
            full_name=full_name,
            location=location,
            repo_admin_change_team_access=repo_admin_change_team_access,
            visibility=visibility,
            website=website,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request("PATCH", f"/orgs/{org}", json=_payload)
        return decode(_response, Organization)

    async def delete(self, org: str) -> None:
        """
        Delete an organization.

        Args:
            org: organization that is to be deleted

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgDelete
        """
        _response = await self._client._request("DELETE", f"/orgs/{org}")
        return decode(_response, None)

    async def block(self, org: str, username: str) -> None:
        """
        Blocks a user from the organization.

        Args:
            org: name of the org
            username: username of the user

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: orgBlockUser
        """
        _response = await self._client._request("PUT", f"/orgs/{org}/block/{username}")
        return decode(_response, None)

    async def list_blocked(
        self,
        org: str,
        *,
        page: int | None = None,
        limit: int | None = None,
    ) -> AsyncPaginated[BlockedUser]:
        """
        List the organization's blocked users.

        Args:
            org: name of the org
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            BlockedUserList.

        Operation ID: orgListBlockedUsers
        """
        return await self._client._paginate(
            "GET", f"/orgs/{org}/list_blocked", model=BlockedUser, page=page, limit=limit
        )

    async def rename(self, org: str, *, new_name: str) -> None:
        """
        Rename an organization.

        Args:
            org: existing org name
            new_name: New username for this org. This name cannot be in use yet by any other user.

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: renameOrg
        """
        _payload = RenameOrgOption(
            new_name=new_name,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request("POST", f"/orgs/{org}/rename", json=_payload)
        return decode(_response, None)

    async def unblock(self, org: str, username: str) -> None:
        """
        Unblock a user from the organization.

        Args:
            org: name of the org
            username: username of the user

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: orgUnblockUser
        """
        _response = await self._client._request("PUT", f"/orgs/{org}/unblock/{username}")
        return decode(_response, None)


class OrgsActions:
    """The ``orgs.actions`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client
        self.runners: OrgsActionsRunners = OrgsActionsRunners(client)
        self.secrets: OrgsActionsSecrets = OrgsActionsSecrets(client)
        self.variables: OrgsActionsVariables = OrgsActionsVariables(client)


class AsyncOrgsActions:
    """The ``orgs.actions`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client
        self.runners: AsyncOrgsActionsRunners = AsyncOrgsActionsRunners(client)
        self.secrets: AsyncOrgsActionsSecrets = AsyncOrgsActionsSecrets(client)
        self.variables: AsyncOrgsActionsVariables = AsyncOrgsActionsVariables(client)


class OrgsActionsRunners:
    """The ``orgs.actions.runners`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(
        self,
        org: str,
        *,
        visible: bool | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> Paginated[ActionRunner]:
        """
        Get the organization's runners.

        Args:
            org: name of the organization
            visible: whether to include all visible runners (true) or only those that are directly owned by the
                organization (false)
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            ActionRunnerList is a list of Forgejo Action runners.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: getOrgRunners
        """
        _query: dict[str, object] = {"visible": visible}

        return self._client._paginate(
            "GET", f"/orgs/{org}/actions/runners", model=ActionRunner, params=_query, page=page, limit=limit
        )

    def register(
        self,
        org: str,
        *,
        description: str | None = None,
        ephemeral: bool | None = None,
        name: str,
    ) -> RegisterRunnerResponse:
        """
        Register a new organization-level runner.

        Args:
            org: name of the organization
            description: Description of the runner to register.
            ephemeral: Register as ephemeral runner
                https://forgejo.org/docs/latest/admin/actions/security/#ephemeral-runner
            name: Name of the runner to register. The name of the runner does not have to be unique.

        Returns:
            RegisterRunnerResponse contains the details of the just registered runner.

        Raises:
            BadRequestError: 400. APIError is error format response.
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: registerOrgRunner
        """
        _payload = RegisterRunnerOptions(
            description=description,
            ephemeral=ephemeral,
            name=name,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("POST", f"/orgs/{org}/actions/runners", json=_payload)
        return decode(_response, RegisterRunnerResponse)

    def jobs(self, org: str, *, labels: str | None = None) -> builtins.list[ActionRunJob]:
        """
        Search for organization's action jobs according filter conditions.

        Args:
            org: name of the organization
            labels: a comma separated list of run job labels to search for

        Returns:
            RunJobList is a list of action run jobs.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: orgSearchRunJobs
        """
        _query: dict[str, object] = {"labels": labels}

        _response = self._client._request("GET", f"/orgs/{org}/actions/runners/jobs", params=_query)
        return decode(_response, list[ActionRunJob])

    def registration_token(self, org: str) -> RegistrationToken:
        """
        Get the organization's runner registration token.

        This operation has been deprecated in Forgejo 15. Use the web UI or
        [`/orgs/{org}/actions/runners`](#/organization/registerOrgRunner) instead.

        Args:
            org: name of the organization

        Returns:
            RegistrationToken is a string used to register a runner with a server.

        Deprecated:
            Deprecated in the vendored Spec; generated for compatibility.

        Operation ID: orgGetRunnerRegistrationToken
        """
        _response = self._client._request("GET", f"/orgs/{org}/actions/runners/registration-token")
        return decode(_response, RegistrationToken)

    def get(self, org: str, runner_id: str) -> ActionRunner:
        """
        Get a particular runner that belongs to the organization.

        Args:
            org: name of the organization
            runner_id: ID of the runner

        Returns:
            ActionRunner represents a runner.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: getOrgRunner
        """
        _response = self._client._request("GET", f"/orgs/{org}/actions/runners/{runner_id}")
        return decode(_response, ActionRunner)

    def delete(self, org: str, runner_id: str) -> None:
        """
        Delete a particular runner that belongs to the organization.

        Args:
            org: name of the organization
            runner_id: ID of the runner

        Returns:
            No content.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: deleteOrgRunner
        """
        _response = self._client._request("DELETE", f"/orgs/{org}/actions/runners/{runner_id}")
        return decode(_response, None)


class AsyncOrgsActionsRunners:
    """The ``orgs.actions.runners`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(
        self,
        org: str,
        *,
        visible: bool | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> AsyncPaginated[ActionRunner]:
        """
        Get the organization's runners.

        Args:
            org: name of the organization
            visible: whether to include all visible runners (true) or only those that are directly owned by the
                organization (false)
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            ActionRunnerList is a list of Forgejo Action runners.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: getOrgRunners
        """
        _query: dict[str, object] = {"visible": visible}

        return await self._client._paginate(
            "GET", f"/orgs/{org}/actions/runners", model=ActionRunner, params=_query, page=page, limit=limit
        )

    async def register(
        self,
        org: str,
        *,
        description: str | None = None,
        ephemeral: bool | None = None,
        name: str,
    ) -> RegisterRunnerResponse:
        """
        Register a new organization-level runner.

        Args:
            org: name of the organization
            description: Description of the runner to register.
            ephemeral: Register as ephemeral runner
                https://forgejo.org/docs/latest/admin/actions/security/#ephemeral-runner
            name: Name of the runner to register. The name of the runner does not have to be unique.

        Returns:
            RegisterRunnerResponse contains the details of the just registered runner.

        Raises:
            BadRequestError: 400. APIError is error format response.
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: registerOrgRunner
        """
        _payload = RegisterRunnerOptions(
            description=description,
            ephemeral=ephemeral,
            name=name,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request("POST", f"/orgs/{org}/actions/runners", json=_payload)
        return decode(_response, RegisterRunnerResponse)

    async def jobs(self, org: str, *, labels: str | None = None) -> builtins.list[ActionRunJob]:
        """
        Search for organization's action jobs according filter conditions.

        Args:
            org: name of the organization
            labels: a comma separated list of run job labels to search for

        Returns:
            RunJobList is a list of action run jobs.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: orgSearchRunJobs
        """
        _query: dict[str, object] = {"labels": labels}

        _response = await self._client._request("GET", f"/orgs/{org}/actions/runners/jobs", params=_query)
        return decode(_response, list[ActionRunJob])

    async def registration_token(self, org: str) -> RegistrationToken:
        """
        Get the organization's runner registration token.

        This operation has been deprecated in Forgejo 15. Use the web UI or
        [`/orgs/{org}/actions/runners`](#/organization/registerOrgRunner) instead.

        Args:
            org: name of the organization

        Returns:
            RegistrationToken is a string used to register a runner with a server.

        Deprecated:
            Deprecated in the vendored Spec; generated for compatibility.

        Operation ID: orgGetRunnerRegistrationToken
        """
        _response = await self._client._request("GET", f"/orgs/{org}/actions/runners/registration-token")
        return decode(_response, RegistrationToken)

    async def get(self, org: str, runner_id: str) -> ActionRunner:
        """
        Get a particular runner that belongs to the organization.

        Args:
            org: name of the organization
            runner_id: ID of the runner

        Returns:
            ActionRunner represents a runner.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: getOrgRunner
        """
        _response = await self._client._request("GET", f"/orgs/{org}/actions/runners/{runner_id}")
        return decode(_response, ActionRunner)

    async def delete(self, org: str, runner_id: str) -> None:
        """
        Delete a particular runner that belongs to the organization.

        Args:
            org: name of the organization
            runner_id: ID of the runner

        Returns:
            No content.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: deleteOrgRunner
        """
        _response = await self._client._request("DELETE", f"/orgs/{org}/actions/runners/{runner_id}")
        return decode(_response, None)


class OrgsActionsSecrets:
    """The ``orgs.actions.secrets`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(self, org: str, *, page: int | None = None, limit: int | None = None) -> Paginated[Secret]:
        """
        List actions secrets of an organization.

        Args:
            org: name of the organization
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            SecretList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgListActionsSecrets
        """
        return self._client._paginate("GET", f"/orgs/{org}/actions/secrets", model=Secret, page=page, limit=limit)

    def update(self, org: str, secretname: str, *, data: str) -> None:
        """
        Create or Update a secret value in an organization.

        Args:
            org: name of organization
            secretname: name of the secret
            data: Data of the secret. Special characters will be retained. Line endings will be normalized to LF to
                match the behaviour of browsers. Encode the data with Base64 if line endings should be retained.

        Returns:
            No content.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: updateOrgSecret
        """
        _payload = CreateOrUpdateSecretOption(
            data=data,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("PUT", f"/orgs/{org}/actions/secrets/{secretname}", json=_payload)
        return decode(_response, None)

    def delete(self, org: str, secretname: str) -> None:
        """
        Delete a secret in an organization.

        Args:
            org: name of organization
            secretname: name of the secret

        Returns:
            No content.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: deleteOrgSecret
        """
        _response = self._client._request("DELETE", f"/orgs/{org}/actions/secrets/{secretname}")
        return decode(_response, None)


class AsyncOrgsActionsSecrets:
    """The ``orgs.actions.secrets`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(self, org: str, *, page: int | None = None, limit: int | None = None) -> AsyncPaginated[Secret]:
        """
        List actions secrets of an organization.

        Args:
            org: name of the organization
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            SecretList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgListActionsSecrets
        """
        return await self._client._paginate("GET", f"/orgs/{org}/actions/secrets", model=Secret, page=page, limit=limit)

    async def update(self, org: str, secretname: str, *, data: str) -> None:
        """
        Create or Update a secret value in an organization.

        Args:
            org: name of organization
            secretname: name of the secret
            data: Data of the secret. Special characters will be retained. Line endings will be normalized to LF to
                match the behaviour of browsers. Encode the data with Base64 if line endings should be retained.

        Returns:
            No content.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: updateOrgSecret
        """
        _payload = CreateOrUpdateSecretOption(
            data=data,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request("PUT", f"/orgs/{org}/actions/secrets/{secretname}", json=_payload)
        return decode(_response, None)

    async def delete(self, org: str, secretname: str) -> None:
        """
        Delete a secret in an organization.

        Args:
            org: name of organization
            secretname: name of the secret

        Returns:
            No content.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: deleteOrgSecret
        """
        _response = await self._client._request("DELETE", f"/orgs/{org}/actions/secrets/{secretname}")
        return decode(_response, None)


class OrgsActionsVariables:
    """The ``orgs.actions.variables`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(self, org: str, *, page: int | None = None, limit: int | None = None) -> Paginated[ActionVariable]:
        """
        List variables of an organization.

        Args:
            org: name of the organization
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            VariableList.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: getOrgVariablesList
        """
        return self._client._paginate(
            "GET", f"/orgs/{org}/actions/variables", model=ActionVariable, page=page, limit=limit
        )

    def get(self, org: str, variablename: str) -> ActionVariable:
        """
        Get organization's variable by name.

        Args:
            org: name of the organization
            variablename: name of the variable

        Returns:
            ActionVariable.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: getOrgVariable
        """
        _response = self._client._request("GET", f"/orgs/{org}/actions/variables/{variablename}")
        return decode(_response, ActionVariable)

    def create(self, org: str, variablename: str, *, value: str) -> None:
        """
        Create a new variable in organization.

        Args:
            org: name of the organization
            variablename: name of the variable
            value: Value of the variable to create. Special characters will be retained. Line endings will be normalized
                to LF to match the behaviour of browsers. Encode the data with Base64 if line endings should be
                retained.

        Returns:
            No content.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: createOrgVariable
        """
        _payload = CreateVariableOption(
            value=value,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("POST", f"/orgs/{org}/actions/variables/{variablename}", json=_payload)
        return decode(_response, None)

    def update(self, org: str, variablename: str, *, name: str | None = None, value: str) -> None:
        """
        Update variable in organization.

        Args:
            org: name of the organization
            variablename: name of the variable
            name: New name for the variable. If the field is empty, the variable name won't be updated. Forgejo will
                convert it to uppercase.
            value: Value of the variable to update. Special characters will be retained. Line endings will be normalized
                to LF to match the behaviour of browsers. Encode the data with Base64 if line endings should be
                retained.

        Returns:
            No content.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: updateOrgVariable
        """
        _payload = UpdateVariableOption(
            name=name,
            value=value,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("PUT", f"/orgs/{org}/actions/variables/{variablename}", json=_payload)
        return decode(_response, None)

    def delete(self, org: str, variablename: str) -> None:
        """
        Delete organization's variable by name.

        Args:
            org: name of the organization
            variablename: name of the variable

        Returns:
            No content.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: deleteOrgVariable
        """
        _response = self._client._request("DELETE", f"/orgs/{org}/actions/variables/{variablename}")
        return decode(_response, None)


class AsyncOrgsActionsVariables:
    """The ``orgs.actions.variables`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(
        self,
        org: str,
        *,
        page: int | None = None,
        limit: int | None = None,
    ) -> AsyncPaginated[ActionVariable]:
        """
        List variables of an organization.

        Args:
            org: name of the organization
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            VariableList.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: getOrgVariablesList
        """
        return await self._client._paginate(
            "GET", f"/orgs/{org}/actions/variables", model=ActionVariable, page=page, limit=limit
        )

    async def get(self, org: str, variablename: str) -> ActionVariable:
        """
        Get organization's variable by name.

        Args:
            org: name of the organization
            variablename: name of the variable

        Returns:
            ActionVariable.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: getOrgVariable
        """
        _response = await self._client._request("GET", f"/orgs/{org}/actions/variables/{variablename}")
        return decode(_response, ActionVariable)

    async def create(self, org: str, variablename: str, *, value: str) -> None:
        """
        Create a new variable in organization.

        Args:
            org: name of the organization
            variablename: name of the variable
            value: Value of the variable to create. Special characters will be retained. Line endings will be normalized
                to LF to match the behaviour of browsers. Encode the data with Base64 if line endings should be
                retained.

        Returns:
            No content.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: createOrgVariable
        """
        _payload = CreateVariableOption(
            value=value,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request("POST", f"/orgs/{org}/actions/variables/{variablename}", json=_payload)
        return decode(_response, None)

    async def update(self, org: str, variablename: str, *, name: str | None = None, value: str) -> None:
        """
        Update variable in organization.

        Args:
            org: name of the organization
            variablename: name of the variable
            name: New name for the variable. If the field is empty, the variable name won't be updated. Forgejo will
                convert it to uppercase.
            value: Value of the variable to update. Special characters will be retained. Line endings will be normalized
                to LF to match the behaviour of browsers. Encode the data with Base64 if line endings should be
                retained.

        Returns:
            No content.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: updateOrgVariable
        """
        _payload = UpdateVariableOption(
            name=name,
            value=value,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request("PUT", f"/orgs/{org}/actions/variables/{variablename}", json=_payload)
        return decode(_response, None)

    async def delete(self, org: str, variablename: str) -> None:
        """
        Delete organization's variable by name.

        Args:
            org: name of the organization
            variablename: name of the variable

        Returns:
            No content.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: deleteOrgVariable
        """
        _response = await self._client._request("DELETE", f"/orgs/{org}/actions/variables/{variablename}")
        return decode(_response, None)


class OrgsActivities:
    """The ``orgs.activities`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def feeds(
        self,
        org: str,
        *,
        date: date | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> Paginated[Activity]:
        """
        List an organization's activity feeds.

        Args:
            org: name of the org
            date: the date of the activities to be found
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            ActivityFeedsList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgListActivityFeeds
        """
        _query: dict[str, object] = {"date": None if date is None else date.isoformat()}

        return self._client._paginate(
            "GET", f"/orgs/{org}/activities/feeds", model=Activity, params=_query, page=page, limit=limit
        )


class AsyncOrgsActivities:
    """The ``orgs.activities`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def feeds(
        self,
        org: str,
        *,
        date: date | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> AsyncPaginated[Activity]:
        """
        List an organization's activity feeds.

        Args:
            org: name of the org
            date: the date of the activities to be found
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            ActivityFeedsList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgListActivityFeeds
        """
        _query: dict[str, object] = {"date": None if date is None else date.isoformat()}

        return await self._client._paginate(
            "GET", f"/orgs/{org}/activities/feeds", model=Activity, params=_query, page=page, limit=limit
        )


class OrgsAvatar:
    """The ``orgs.avatar`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def update(self, org: str, *, image: str | None = None) -> None:
        """
        Update an organization's avatar.

        Args:
            org: name of the organization
            image: image must be base64 encoded

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgUpdateAvatar
        """
        if image is not None:
            _payload = UpdateUserAvatarOption(image=image).model_dump(mode="json", by_alias=True, exclude_none=True)
        else:
            _payload = None

        _response = self._client._request("POST", f"/orgs/{org}/avatar", json=_payload)
        return decode(_response, None)

    def delete(self, org: str) -> None:
        """
        Delete an organization's avatar. It will be replaced by a default one.

        Args:
            org: name of the organization

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgDeleteAvatar
        """
        _response = self._client._request("DELETE", f"/orgs/{org}/avatar")
        return decode(_response, None)


class AsyncOrgsAvatar:
    """The ``orgs.avatar`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def update(self, org: str, *, image: str | None = None) -> None:
        """
        Update an organization's avatar.

        Args:
            org: name of the organization
            image: image must be base64 encoded

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgUpdateAvatar
        """
        if image is not None:
            _payload = UpdateUserAvatarOption(image=image).model_dump(mode="json", by_alias=True, exclude_none=True)
        else:
            _payload = None

        _response = await self._client._request("POST", f"/orgs/{org}/avatar", json=_payload)
        return decode(_response, None)

    async def delete(self, org: str) -> None:
        """
        Delete an organization's avatar. It will be replaced by a default one.

        Args:
            org: name of the organization

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgDeleteAvatar
        """
        _response = await self._client._request("DELETE", f"/orgs/{org}/avatar")
        return decode(_response, None)


class OrgsHooks:
    """The ``orgs.hooks`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(self, org: str, *, page: int | None = None, limit: int | None = None) -> Paginated[Hook]:
        """
        List an organization's webhooks.

        Args:
            org: name of the organization
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            HookListWithoutPagination - Hooks without pagination headers.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgListHooks
        """
        return self._client._paginate("GET", f"/orgs/{org}/hooks", model=Hook, page=page, limit=limit)

    def create(
        self,
        org: str,
        *,
        active: bool | None = None,
        authorization_header: str | None = None,
        branch_filter: str | None = None,
        config: CreateHookOptionConfig,
        events: builtins.list[str] | None = None,
        type: CreateHookOptionType,
    ) -> Hook:
        """
        Create a hook.

        Args:
            org: name of the organization
            active:
            authorization_header:
            branch_filter:
            config:
            events:
            type:

        Returns:
            Hook.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgCreateHook
        """
        _payload = CreateHookOption(
            active=active,
            authorization_header=authorization_header,
            branch_filter=branch_filter,
            config=config,
            events=events,
            type=type,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("POST", f"/orgs/{org}/hooks", json=_payload)
        return decode(_response, Hook)

    def get(self, org: str, id: int) -> Hook:
        """
        Get a hook.

        Args:
            org: name of the organization
            id: id of the hook to get

        Returns:
            Hook.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgGetHook
        """
        _response = self._client._request("GET", f"/orgs/{org}/hooks/{id}")
        return decode(_response, Hook)

    def update(
        self,
        org: str,
        id: int,
        *,
        active: bool | None = None,
        authorization_header: str | None = None,
        branch_filter: str | None = None,
        config: dict[str, str] | None = None,
        events: builtins.list[str] | None = None,
    ) -> Hook:
        """
        Update a hook.

        Args:
            org: name of the organization
            id: id of the hook to update
            active:
            authorization_header:
            branch_filter:
            config:
            events:

        Returns:
            Hook.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgEditHook
        """
        if (
            active is not None
            or authorization_header is not None
            or branch_filter is not None
            or config is not None
            or events is not None
        ):
            _payload = EditHookOption(
                active=active,
                authorization_header=authorization_header,
                branch_filter=branch_filter,
                config=config,
                events=events,
            ).model_dump(mode="json", by_alias=True, exclude_none=True)
        else:
            _payload = None

        _response = self._client._request("PATCH", f"/orgs/{org}/hooks/{id}", json=_payload)
        return decode(_response, Hook)

    def delete(self, org: str, id: int) -> None:
        """
        Delete a hook.

        Args:
            org: name of the organization
            id: id of the hook to delete

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgDeleteHook
        """
        _response = self._client._request("DELETE", f"/orgs/{org}/hooks/{id}")
        return decode(_response, None)


class AsyncOrgsHooks:
    """The ``orgs.hooks`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(self, org: str, *, page: int | None = None, limit: int | None = None) -> AsyncPaginated[Hook]:
        """
        List an organization's webhooks.

        Args:
            org: name of the organization
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            HookListWithoutPagination - Hooks without pagination headers.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgListHooks
        """
        return await self._client._paginate("GET", f"/orgs/{org}/hooks", model=Hook, page=page, limit=limit)

    async def create(
        self,
        org: str,
        *,
        active: bool | None = None,
        authorization_header: str | None = None,
        branch_filter: str | None = None,
        config: CreateHookOptionConfig,
        events: builtins.list[str] | None = None,
        type: CreateHookOptionType,
    ) -> Hook:
        """
        Create a hook.

        Args:
            org: name of the organization
            active:
            authorization_header:
            branch_filter:
            config:
            events:
            type:

        Returns:
            Hook.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgCreateHook
        """
        _payload = CreateHookOption(
            active=active,
            authorization_header=authorization_header,
            branch_filter=branch_filter,
            config=config,
            events=events,
            type=type,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request("POST", f"/orgs/{org}/hooks", json=_payload)
        return decode(_response, Hook)

    async def get(self, org: str, id: int) -> Hook:
        """
        Get a hook.

        Args:
            org: name of the organization
            id: id of the hook to get

        Returns:
            Hook.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgGetHook
        """
        _response = await self._client._request("GET", f"/orgs/{org}/hooks/{id}")
        return decode(_response, Hook)

    async def update(
        self,
        org: str,
        id: int,
        *,
        active: bool | None = None,
        authorization_header: str | None = None,
        branch_filter: str | None = None,
        config: dict[str, str] | None = None,
        events: builtins.list[str] | None = None,
    ) -> Hook:
        """
        Update a hook.

        Args:
            org: name of the organization
            id: id of the hook to update
            active:
            authorization_header:
            branch_filter:
            config:
            events:

        Returns:
            Hook.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgEditHook
        """
        if (
            active is not None
            or authorization_header is not None
            or branch_filter is not None
            or config is not None
            or events is not None
        ):
            _payload = EditHookOption(
                active=active,
                authorization_header=authorization_header,
                branch_filter=branch_filter,
                config=config,
                events=events,
            ).model_dump(mode="json", by_alias=True, exclude_none=True)
        else:
            _payload = None

        _response = await self._client._request("PATCH", f"/orgs/{org}/hooks/{id}", json=_payload)
        return decode(_response, Hook)

    async def delete(self, org: str, id: int) -> None:
        """
        Delete a hook.

        Args:
            org: name of the organization
            id: id of the hook to delete

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgDeleteHook
        """
        _response = await self._client._request("DELETE", f"/orgs/{org}/hooks/{id}")
        return decode(_response, None)


class OrgsLabels:
    """The ``orgs.labels`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(
        self,
        org: str,
        *,
        sort: Literal["mostissues", "leastissues", "reversealphabetically"] | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> Paginated[Label]:
        """
        List an organization's labels.

        Args:
            org: name of the organization
            sort: Specifies the sorting method: mostissues, leastissues, or reversealphabetically.
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            LabelList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgListLabels
        """
        _query: dict[str, object] = {"sort": sort}

        return self._client._paginate("GET", f"/orgs/{org}/labels", model=Label, params=_query, page=page, limit=limit)

    def create(
        self,
        org: str,
        *,
        color: str,
        description: str | None = None,
        exclusive: bool | None = None,
        is_archived: bool | None = None,
        name: str,
    ) -> Label:
        """
        Create a label for an organization.

        Args:
            org: name of the organization
            color:
            description:
            exclusive:
            is_archived:
            name:

        Returns:
            Label.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: orgCreateLabel
        """
        _payload = CreateLabelOption(
            color=color,
            description=description,
            exclusive=exclusive,
            is_archived=is_archived,
            name=name,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("POST", f"/orgs/{org}/labels", json=_payload)
        return decode(_response, Label)

    def get(self, org: str, id: int) -> Label:
        """
        Get a single label.

        Args:
            org: name of the organization
            id: id of the label to get

        Returns:
            Label.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgGetLabel
        """
        _response = self._client._request("GET", f"/orgs/{org}/labels/{id}")
        return decode(_response, Label)

    def update(
        self,
        org: str,
        id: int,
        *,
        color: str | None = None,
        description: str | None = None,
        exclusive: bool | None = None,
        is_archived: bool | None = None,
        name: str | None = None,
    ) -> Label:
        """
        Update a label.

        Args:
            org: name of the organization
            id: id of the label to edit
            color:
            description:
            exclusive:
            is_archived:
            name:

        Returns:
            Label.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: orgEditLabel
        """
        if (
            color is not None
            or description is not None
            or exclusive is not None
            or is_archived is not None
            or name is not None
        ):
            _payload = EditLabelOption(
                color=color, description=description, exclusive=exclusive, is_archived=is_archived, name=name
            ).model_dump(mode="json", by_alias=True, exclude_none=True)
        else:
            _payload = None

        _response = self._client._request("PATCH", f"/orgs/{org}/labels/{id}", json=_payload)
        return decode(_response, Label)

    def delete(self, org: str, id: int) -> None:
        """
        Delete a label.

        Args:
            org: name of the organization
            id: id of the label to delete

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgDeleteLabel
        """
        _response = self._client._request("DELETE", f"/orgs/{org}/labels/{id}")
        return decode(_response, None)


class AsyncOrgsLabels:
    """The ``orgs.labels`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(
        self,
        org: str,
        *,
        sort: Literal["mostissues", "leastissues", "reversealphabetically"] | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> AsyncPaginated[Label]:
        """
        List an organization's labels.

        Args:
            org: name of the organization
            sort: Specifies the sorting method: mostissues, leastissues, or reversealphabetically.
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            LabelList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgListLabels
        """
        _query: dict[str, object] = {"sort": sort}

        return await self._client._paginate(
            "GET", f"/orgs/{org}/labels", model=Label, params=_query, page=page, limit=limit
        )

    async def create(
        self,
        org: str,
        *,
        color: str,
        description: str | None = None,
        exclusive: bool | None = None,
        is_archived: bool | None = None,
        name: str,
    ) -> Label:
        """
        Create a label for an organization.

        Args:
            org: name of the organization
            color:
            description:
            exclusive:
            is_archived:
            name:

        Returns:
            Label.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: orgCreateLabel
        """
        _payload = CreateLabelOption(
            color=color,
            description=description,
            exclusive=exclusive,
            is_archived=is_archived,
            name=name,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request("POST", f"/orgs/{org}/labels", json=_payload)
        return decode(_response, Label)

    async def get(self, org: str, id: int) -> Label:
        """
        Get a single label.

        Args:
            org: name of the organization
            id: id of the label to get

        Returns:
            Label.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgGetLabel
        """
        _response = await self._client._request("GET", f"/orgs/{org}/labels/{id}")
        return decode(_response, Label)

    async def update(
        self,
        org: str,
        id: int,
        *,
        color: str | None = None,
        description: str | None = None,
        exclusive: bool | None = None,
        is_archived: bool | None = None,
        name: str | None = None,
    ) -> Label:
        """
        Update a label.

        Args:
            org: name of the organization
            id: id of the label to edit
            color:
            description:
            exclusive:
            is_archived:
            name:

        Returns:
            Label.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: orgEditLabel
        """
        if (
            color is not None
            or description is not None
            or exclusive is not None
            or is_archived is not None
            or name is not None
        ):
            _payload = EditLabelOption(
                color=color, description=description, exclusive=exclusive, is_archived=is_archived, name=name
            ).model_dump(mode="json", by_alias=True, exclude_none=True)
        else:
            _payload = None

        _response = await self._client._request("PATCH", f"/orgs/{org}/labels/{id}", json=_payload)
        return decode(_response, Label)

    async def delete(self, org: str, id: int) -> None:
        """
        Delete a label.

        Args:
            org: name of the organization
            id: id of the label to delete

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgDeleteLabel
        """
        _response = await self._client._request("DELETE", f"/orgs/{org}/labels/{id}")
        return decode(_response, None)


class OrgsMembers:
    """The ``orgs.members`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(self, org: str, *, page: int | None = None, limit: int | None = None) -> Paginated[User]:
        """
        List an organization's members.

        Args:
            org: name of the organization
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            UserList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgListMembers
        """
        return self._client._paginate("GET", f"/orgs/{org}/members", model=User, page=page, limit=limit)

    def get(self, org: str, username: str) -> None:
        """
        Check if a user is a member of an organization.

        Args:
            org: name of the organization
            username: username of the user

        Returns:
            No content.

        Raises:
            APIError: 303. redirection to /orgs/{org}/public_members/{username}.
            NotFoundError: 404. user is not a member.

        Operation ID: orgIsMember
        """
        _response = self._client._request("GET", f"/orgs/{org}/members/{username}")
        return decode(_response, None)

    def delete(self, org: str, username: str) -> None:
        """
        Remove a member from an organization.

        Args:
            org: name of the organization
            username: username of the user

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgDeleteMember
        """
        _response = self._client._request("DELETE", f"/orgs/{org}/members/{username}")
        return decode(_response, None)


class AsyncOrgsMembers:
    """The ``orgs.members`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(self, org: str, *, page: int | None = None, limit: int | None = None) -> AsyncPaginated[User]:
        """
        List an organization's members.

        Args:
            org: name of the organization
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            UserList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgListMembers
        """
        return await self._client._paginate("GET", f"/orgs/{org}/members", model=User, page=page, limit=limit)

    async def get(self, org: str, username: str) -> None:
        """
        Check if a user is a member of an organization.

        Args:
            org: name of the organization
            username: username of the user

        Returns:
            No content.

        Raises:
            APIError: 303. redirection to /orgs/{org}/public_members/{username}.
            NotFoundError: 404. user is not a member.

        Operation ID: orgIsMember
        """
        _response = await self._client._request("GET", f"/orgs/{org}/members/{username}")
        return decode(_response, None)

    async def delete(self, org: str, username: str) -> None:
        """
        Remove a member from an organization.

        Args:
            org: name of the organization
            username: username of the user

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgDeleteMember
        """
        _response = await self._client._request("DELETE", f"/orgs/{org}/members/{username}")
        return decode(_response, None)


class OrgsPublicMembers:
    """The ``orgs.public_members`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(self, org: str, *, page: int | None = None, limit: int | None = None) -> Paginated[User]:
        """
        List an organization's public members.

        Args:
            org: name of the organization
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            UserList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgListPublicMembers
        """
        return self._client._paginate("GET", f"/orgs/{org}/public_members", model=User, page=page, limit=limit)

    def get(self, org: str, username: str) -> None:
        """
        Check if a user is a public member of an organization.

        Args:
            org: name of the organization
            username: username of the user

        Returns:
            No content.

        Raises:
            NotFoundError: 404. user is not a public member.

        Operation ID: orgIsPublicMember
        """
        _response = self._client._request("GET", f"/orgs/{org}/public_members/{username}")
        return decode(_response, None)

    def publicize(self, org: str, username: str) -> None:
        """
        Publicize a user's membership.

        Args:
            org: name of the organization
            username: username of the user

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgPublicizeMember
        """
        _response = self._client._request("PUT", f"/orgs/{org}/public_members/{username}")
        return decode(_response, None)

    def conceal(self, org: str, username: str) -> None:
        """
        Conceal a user's membership.

        Args:
            org: name of the organization
            username: username of the user

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgConcealMember
        """
        _response = self._client._request("DELETE", f"/orgs/{org}/public_members/{username}")
        return decode(_response, None)


class AsyncOrgsPublicMembers:
    """The ``orgs.public_members`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(self, org: str, *, page: int | None = None, limit: int | None = None) -> AsyncPaginated[User]:
        """
        List an organization's public members.

        Args:
            org: name of the organization
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            UserList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgListPublicMembers
        """
        return await self._client._paginate("GET", f"/orgs/{org}/public_members", model=User, page=page, limit=limit)

    async def get(self, org: str, username: str) -> None:
        """
        Check if a user is a public member of an organization.

        Args:
            org: name of the organization
            username: username of the user

        Returns:
            No content.

        Raises:
            NotFoundError: 404. user is not a public member.

        Operation ID: orgIsPublicMember
        """
        _response = await self._client._request("GET", f"/orgs/{org}/public_members/{username}")
        return decode(_response, None)

    async def publicize(self, org: str, username: str) -> None:
        """
        Publicize a user's membership.

        Args:
            org: name of the organization
            username: username of the user

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgPublicizeMember
        """
        _response = await self._client._request("PUT", f"/orgs/{org}/public_members/{username}")
        return decode(_response, None)

    async def conceal(self, org: str, username: str) -> None:
        """
        Conceal a user's membership.

        Args:
            org: name of the organization
            username: username of the user

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgConcealMember
        """
        _response = await self._client._request("DELETE", f"/orgs/{org}/public_members/{username}")
        return decode(_response, None)


class OrgsQuota:
    """The ``orgs.quota`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def get(self, org: str) -> QuotaInfo:
        """
        Get quota information for an organization.

        Args:
            org: name of the organization

        Returns:
            QuotaInfo.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgGetQuota
        """
        _response = self._client._request("GET", f"/orgs/{org}/quota")
        return decode(_response, QuotaInfo)

    def artifacts(self, org: str, *, page: int | None = None, limit: int | None = None) -> Paginated[QuotaUsedArtifact]:
        """
        List the artifacts affecting the organization's quota.

        Args:
            org: name of the organization
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            QuotaUsedArtifactList.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgListQuotaArtifacts
        """
        return self._client._paginate(
            "GET", f"/orgs/{org}/quota/artifacts", model=QuotaUsedArtifact, page=page, limit=limit
        )

    def attachments(
        self,
        org: str,
        *,
        page: int | None = None,
        limit: int | None = None,
    ) -> Paginated[QuotaUsedAttachment]:
        """
        List the attachments affecting the organization's quota.

        Args:
            org: name of the organization
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            QuotaUsedAttachmentList.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgListQuotaAttachments
        """
        return self._client._paginate(
            "GET", f"/orgs/{org}/quota/attachments", model=QuotaUsedAttachment, page=page, limit=limit
        )

    def check(self, org: str, *, subject: str) -> bool:
        """
        Check if the organization is over quota for a given subject.

        Args:
            org: name of the organization
            subject: subject of the quota

        Returns:
            Returns true if the action is accepted.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: orgCheckQuota
        """
        _query: dict[str, object] = {"subject": subject}

        _response = self._client._request("GET", f"/orgs/{org}/quota/check", params=_query)
        return decode(_response, bool)

    def packages(self, org: str, *, page: int | None = None, limit: int | None = None) -> Paginated[QuotaUsedPackage]:
        """
        List the packages affecting the organization's quota.

        Args:
            org: name of the organization
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            QuotaUsedPackageList.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgListQuotaPackages
        """
        return self._client._paginate(
            "GET", f"/orgs/{org}/quota/packages", model=QuotaUsedPackage, page=page, limit=limit
        )


class AsyncOrgsQuota:
    """The ``orgs.quota`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def get(self, org: str) -> QuotaInfo:
        """
        Get quota information for an organization.

        Args:
            org: name of the organization

        Returns:
            QuotaInfo.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgGetQuota
        """
        _response = await self._client._request("GET", f"/orgs/{org}/quota")
        return decode(_response, QuotaInfo)

    async def artifacts(
        self,
        org: str,
        *,
        page: int | None = None,
        limit: int | None = None,
    ) -> AsyncPaginated[QuotaUsedArtifact]:
        """
        List the artifacts affecting the organization's quota.

        Args:
            org: name of the organization
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            QuotaUsedArtifactList.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgListQuotaArtifacts
        """
        return await self._client._paginate(
            "GET", f"/orgs/{org}/quota/artifacts", model=QuotaUsedArtifact, page=page, limit=limit
        )

    async def attachments(
        self,
        org: str,
        *,
        page: int | None = None,
        limit: int | None = None,
    ) -> AsyncPaginated[QuotaUsedAttachment]:
        """
        List the attachments affecting the organization's quota.

        Args:
            org: name of the organization
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            QuotaUsedAttachmentList.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgListQuotaAttachments
        """
        return await self._client._paginate(
            "GET", f"/orgs/{org}/quota/attachments", model=QuotaUsedAttachment, page=page, limit=limit
        )

    async def check(self, org: str, *, subject: str) -> bool:
        """
        Check if the organization is over quota for a given subject.

        Args:
            org: name of the organization
            subject: subject of the quota

        Returns:
            Returns true if the action is accepted.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: orgCheckQuota
        """
        _query: dict[str, object] = {"subject": subject}

        _response = await self._client._request("GET", f"/orgs/{org}/quota/check", params=_query)
        return decode(_response, bool)

    async def packages(
        self,
        org: str,
        *,
        page: int | None = None,
        limit: int | None = None,
    ) -> AsyncPaginated[QuotaUsedPackage]:
        """
        List the packages affecting the organization's quota.

        Args:
            org: name of the organization
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            QuotaUsedPackageList.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgListQuotaPackages
        """
        return await self._client._paginate(
            "GET", f"/orgs/{org}/quota/packages", model=QuotaUsedPackage, page=page, limit=limit
        )


class OrgsRepos:
    """The ``orgs.repos`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(self, org: str, *, page: int | None = None, limit: int | None = None) -> Paginated[Repository]:
        """
        List an organization's repos.

        Args:
            org: name of the organization
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            RepositoryList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgListRepos
        """
        return self._client._paginate("GET", f"/orgs/{org}/repos", model=Repository, page=page, limit=limit)

    def create(
        self,
        org: str,
        *,
        auto_init: bool | None = None,
        default_branch: str | None = None,
        description: str | None = None,
        gitignores: str | None = None,
        issue_labels: str | None = None,
        license: str | None = None,
        name: str,
        object_format_name: CreateRepoOptionObjectFormatName | None = None,
        private: bool | None = None,
        readme: str | None = None,
        template: bool | None = None,
        trust_model: CreateRepoOptionTrustModel | None = None,
    ) -> Repository:
        """
        Create a repository in an organization.

        Args:
            org: name of organization
            auto_init: Whether the repository should be auto-initialized?
            default_branch: DefaultBranch of the repository (used when initializes and in template)
            description: Description of the repository to create
            gitignores: Gitignores to use, separated by commas
            issue_labels: Label-Set to use
            license: License to use
            name: Name of the repository to create
            object_format_name: ObjectFormatName of the underlying git repository
            private: Whether the repository is private
            readme: Readme of the repository to create
            template: Whether the repository is template
            trust_model: TrustModel of the repository

        Returns:
            Repository.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: createOrgRepo
        """
        _payload = CreateRepoOption(
            auto_init=auto_init,
            default_branch=default_branch,
            description=description,
            gitignores=gitignores,
            issue_labels=issue_labels,
            license=license,
            name=name,
            object_format_name=object_format_name,
            private=private,
            readme=readme,
            template=template,
            trust_model=trust_model,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("POST", f"/orgs/{org}/repos", json=_payload)
        return decode(_response, Repository)


class AsyncOrgsRepos:
    """The ``orgs.repos`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(self, org: str, *, page: int | None = None, limit: int | None = None) -> AsyncPaginated[Repository]:
        """
        List an organization's repos.

        Args:
            org: name of the organization
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            RepositoryList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgListRepos
        """
        return await self._client._paginate("GET", f"/orgs/{org}/repos", model=Repository, page=page, limit=limit)

    async def create(
        self,
        org: str,
        *,
        auto_init: bool | None = None,
        default_branch: str | None = None,
        description: str | None = None,
        gitignores: str | None = None,
        issue_labels: str | None = None,
        license: str | None = None,
        name: str,
        object_format_name: CreateRepoOptionObjectFormatName | None = None,
        private: bool | None = None,
        readme: str | None = None,
        template: bool | None = None,
        trust_model: CreateRepoOptionTrustModel | None = None,
    ) -> Repository:
        """
        Create a repository in an organization.

        Args:
            org: name of organization
            auto_init: Whether the repository should be auto-initialized?
            default_branch: DefaultBranch of the repository (used when initializes and in template)
            description: Description of the repository to create
            gitignores: Gitignores to use, separated by commas
            issue_labels: Label-Set to use
            license: License to use
            name: Name of the repository to create
            object_format_name: ObjectFormatName of the underlying git repository
            private: Whether the repository is private
            readme: Readme of the repository to create
            template: Whether the repository is template
            trust_model: TrustModel of the repository

        Returns:
            Repository.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: createOrgRepo
        """
        _payload = CreateRepoOption(
            auto_init=auto_init,
            default_branch=default_branch,
            description=description,
            gitignores=gitignores,
            issue_labels=issue_labels,
            license=license,
            name=name,
            object_format_name=object_format_name,
            private=private,
            readme=readme,
            template=template,
            trust_model=trust_model,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request("POST", f"/orgs/{org}/repos", json=_payload)
        return decode(_response, Repository)


class OrgsTeams:
    """The ``orgs.teams`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(self, org: str, *, page: int | None = None, limit: int | None = None) -> Paginated[Team]:
        """
        List an organization's teams.

        Args:
            org: name of the organization
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            TeamList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgListTeams
        """
        return self._client._paginate("GET", f"/orgs/{org}/teams", model=Team, page=page, limit=limit)

    def create(
        self,
        org: str,
        *,
        can_create_org_repo: bool | None = None,
        description: str | None = None,
        includes_all_repositories: bool | None = None,
        name: str,
        permission: CreateTeamOptionPermission | None = None,
        units: builtins.list[str] | None = None,
        units_map: dict[str, str] | None = None,
    ) -> Team:
        """
        Create a team.

        Args:
            org: name of the organization
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
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: orgCreateTeam
        """
        _payload = CreateTeamOption(
            can_create_org_repo=can_create_org_repo,
            description=description,
            includes_all_repositories=includes_all_repositories,
            name=name,
            permission=permission,
            units=units,
            units_map=units_map,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("POST", f"/orgs/{org}/teams", json=_payload)
        return decode(_response, Team)

    def search(
        self,
        org: str,
        *,
        q: str | None = None,
        include_desc: bool | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> TeamSearchResults:
        """
        Search for teams within an organization.

        Args:
            org: name of the organization
            q: keywords to search
            include_desc: include search within team description (defaults to true)
            page: page number of results to return (1-based)
            limit: page size of results

        Returns:
            SearchResults of a successful search.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: teamSearch
        """
        _query: dict[str, object] = {"q": q, "include_desc": include_desc, "page": page, "limit": limit}

        _response = self._client._request("GET", f"/orgs/{org}/teams/search", params=_query)
        return decode(_response, TeamSearchResults)


class AsyncOrgsTeams:
    """The ``orgs.teams`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(self, org: str, *, page: int | None = None, limit: int | None = None) -> AsyncPaginated[Team]:
        """
        List an organization's teams.

        Args:
            org: name of the organization
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            TeamList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgListTeams
        """
        return await self._client._paginate("GET", f"/orgs/{org}/teams", model=Team, page=page, limit=limit)

    async def create(
        self,
        org: str,
        *,
        can_create_org_repo: bool | None = None,
        description: str | None = None,
        includes_all_repositories: bool | None = None,
        name: str,
        permission: CreateTeamOptionPermission | None = None,
        units: builtins.list[str] | None = None,
        units_map: dict[str, str] | None = None,
    ) -> Team:
        """
        Create a team.

        Args:
            org: name of the organization
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
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: orgCreateTeam
        """
        _payload = CreateTeamOption(
            can_create_org_repo=can_create_org_repo,
            description=description,
            includes_all_repositories=includes_all_repositories,
            name=name,
            permission=permission,
            units=units,
            units_map=units_map,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request("POST", f"/orgs/{org}/teams", json=_payload)
        return decode(_response, Team)

    async def search(
        self,
        org: str,
        *,
        q: str | None = None,
        include_desc: bool | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> TeamSearchResults:
        """
        Search for teams within an organization.

        Args:
            org: name of the organization
            q: keywords to search
            include_desc: include search within team description (defaults to true)
            page: page number of results to return (1-based)
            limit: page size of results

        Returns:
            SearchResults of a successful search.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: teamSearch
        """
        _query: dict[str, object] = {"q": q, "include_desc": include_desc, "page": page, "limit": limit}

        _response = await self._client._request("GET", f"/orgs/{org}/teams/search", params=_query)
        return decode(_response, TeamSearchResults)
