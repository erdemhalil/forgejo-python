"""Generated resource namespaces for the ``admin`` group. Do not edit by hand.

Regenerate with ``python -m codegen``; see docs/development/codegen.md.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from pyfj._generated.models.access_token import AccessToken
from pyfj._generated.models.action_run_job import ActionRunJob
from pyfj._generated.models.action_runner import ActionRunner
from pyfj._generated.models.create_access_token_option import CreateAccessTokenOption
from pyfj._generated.models.create_hook_option import CreateHookOption
from pyfj._generated.models.create_key_option import CreateKeyOption
from pyfj._generated.models.create_org_option import CreateOrgOption
from pyfj._generated.models.create_quota_group_options import CreateQuotaGroupOptions
from pyfj._generated.models.create_quota_rule_options import CreateQuotaRuleOptions
from pyfj._generated.models.create_repo_option import CreateRepoOption
from pyfj._generated.models.create_user_option import CreateUserOption
from pyfj._generated.models.cron import Cron
from pyfj._generated.models.delete_email_option import DeleteEmailOption
from pyfj._generated.models.edit_hook_option import EditHookOption
from pyfj._generated.models.edit_quota_rule_options import EditQuotaRuleOptions
from pyfj._generated.models.edit_user_option import EditUserOption
from pyfj._generated.models.email import Email
from pyfj._generated.models.hook import Hook
from pyfj._generated.models.organization import Organization
from pyfj._generated.models.public_key import PublicKey
from pyfj._generated.models.quota_group import QuotaGroup
from pyfj._generated.models.quota_info import QuotaInfo
from pyfj._generated.models.quota_rule_info import QuotaRuleInfo
from pyfj._generated.models.register_runner_options import RegisterRunnerOptions
from pyfj._generated.models.register_runner_response import RegisterRunnerResponse
from pyfj._generated.models.registration_token import RegistrationToken
from pyfj._generated.models.rename_user_option import RenameUserOption
from pyfj._generated.models.repository import Repository
from pyfj._generated.models.set_user_quota_groups_options import SetUserQuotaGroupsOptions
from pyfj._generated.models.user import User
from pyfj._runtime import decode

if TYPE_CHECKING:
    import builtins
    from datetime import datetime
    from typing import Literal

    from pyfj._generated.models.create_hook_option import CreateHookOptionType
    from pyfj._generated.models.create_hook_option_config import CreateHookOptionConfig
    from pyfj._generated.models.create_org_option import CreateOrgOptionVisibility
    from pyfj._generated.models.create_repo_option import CreateRepoOptionObjectFormatName, CreateRepoOptionTrustModel
    from pyfj._generated.models.repo_target_option import RepoTargetOption
    from pyfj._runtime import AsyncForgejo as _RuntimeAsyncForgejo
    from pyfj._runtime import AsyncPaginated, Paginated
    from pyfj._runtime import Forgejo as _RuntimeForgejo


class Admin:
    """The ``admin`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client
        self.actions: AdminActions = AdminActions(client)
        self.cron: AdminCron = AdminCron(client)
        self.emails: AdminEmails = AdminEmails(client)
        self.hooks: AdminHooks = AdminHooks(client)
        self.quota: AdminQuota = AdminQuota(client)
        self.runners: AdminRunners = AdminRunners(client)
        self.unadopted: AdminUnadopted = AdminUnadopted(client)
        self.users: AdminUsers = AdminUsers(client)

    def orgs(self, *, page: int | None = None, limit: int | None = None) -> Paginated[Organization]:
        """
        List all organizations.

        Args:
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            OrganizationList.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: adminGetAllOrgs
        """
        return self._client._paginate("GET", "/admin/orgs", model=Organization, page=page, limit=limit)


class AsyncAdmin:
    """The ``admin`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client
        self.actions: AsyncAdminActions = AsyncAdminActions(client)
        self.cron: AsyncAdminCron = AsyncAdminCron(client)
        self.emails: AsyncAdminEmails = AsyncAdminEmails(client)
        self.hooks: AsyncAdminHooks = AsyncAdminHooks(client)
        self.quota: AsyncAdminQuota = AsyncAdminQuota(client)
        self.runners: AsyncAdminRunners = AsyncAdminRunners(client)
        self.unadopted: AsyncAdminUnadopted = AsyncAdminUnadopted(client)
        self.users: AsyncAdminUsers = AsyncAdminUsers(client)

    async def orgs(self, *, page: int | None = None, limit: int | None = None) -> AsyncPaginated[Organization]:
        """
        List all organizations.

        Args:
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            OrganizationList.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: adminGetAllOrgs
        """
        return await self._client._paginate("GET", "/admin/orgs", model=Organization, page=page, limit=limit)


class AdminActions:
    """The ``admin.actions`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client
        self.runners: AdminActionsRunners = AdminActionsRunners(client)


class AsyncAdminActions:
    """The ``admin.actions`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client
        self.runners: AsyncAdminActionsRunners = AsyncAdminActionsRunners(client)


class AdminActionsRunners:
    """The ``admin.actions.runners`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(
        self,
        *,
        visible: bool | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> Paginated[ActionRunner]:
        """
        Get all runners, no matter whether they are global runners or scoped to an organization, user, or repository.

        Args:
            visible: whether to include all visible runners (true) or only those that are directly owned by the instance
                (false)
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            ActionRunnerList is a list of Forgejo Action runners.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: getAdminRunners
        """
        _query: dict[str, object] = {"visible": visible}

        return self._client._paginate(
            "GET", "/admin/actions/runners", model=ActionRunner, params=_query, page=page, limit=limit
        )

    def register(
        self,
        *,
        description: str | None = None,
        ephemeral: bool | None = None,
        name: str,
    ) -> RegisterRunnerResponse:
        """
        Register a new global runner.

        Args:
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

        Operation ID: registerAdminRunner
        """
        _payload = RegisterRunnerOptions(
            description=description,
            ephemeral=ephemeral,
            name=name,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("POST", "/admin/actions/runners", json=_payload)
        return decode(_response, RegisterRunnerResponse)

    def jobs(self, *, labels: str | None = None) -> builtins.list[ActionRunJob]:
        """
        Get action run jobs.

        Args:
            labels: a comma separated list of labels to search for

        Returns:
            RunJobList is a list of action run jobs.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: adminGetActionRunJobs
        """
        _query: dict[str, object] = {"labels": labels}

        _response = self._client._request("GET", "/admin/actions/runners/jobs", params=_query)
        return decode(_response, list[ActionRunJob])

    def registration_token(self) -> RegistrationToken:
        """
        Get a runner registration token for registering global runners.

        This operation has been deprecated in Forgejo 15. Use the web UI or
        [`/admin/actions/runners`](#/admin/registerAdminRunner) instead.

        Returns:
            RegistrationToken is a string used to register a runner with a server.

        Deprecated:
            Deprecated in the vendored Spec; generated for compatibility.

        Operation ID: adminGetRunnerRegistrationToken
        """
        _response = self._client._request("GET", "/admin/actions/runners/registration-token")
        return decode(_response, RegistrationToken)

    def get(self, runner_id: str) -> ActionRunner:
        """
        Get a particular runner, no matter whether it is a global runner or scoped to an organization, user, or
        repository.

        Args:
            runner_id: ID of the runner

        Returns:
            ActionRunner represents a runner.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: getAdminRunner
        """
        _response = self._client._request("GET", f"/admin/actions/runners/{runner_id}")
        return decode(_response, ActionRunner)

    def delete(self, runner_id: str) -> None:
        """
        Delete a particular runner, no matter whether it is a global runner or scoped to an organization, user, or
        repository.

        Args:
            runner_id: ID of the runner

        Returns:
            No content.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: deleteAdminRunner
        """
        _response = self._client._request("DELETE", f"/admin/actions/runners/{runner_id}")
        return decode(_response, None)


class AsyncAdminActionsRunners:
    """The ``admin.actions.runners`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(
        self,
        *,
        visible: bool | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> AsyncPaginated[ActionRunner]:
        """
        Get all runners, no matter whether they are global runners or scoped to an organization, user, or repository.

        Args:
            visible: whether to include all visible runners (true) or only those that are directly owned by the instance
                (false)
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            ActionRunnerList is a list of Forgejo Action runners.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: getAdminRunners
        """
        _query: dict[str, object] = {"visible": visible}

        return await self._client._paginate(
            "GET", "/admin/actions/runners", model=ActionRunner, params=_query, page=page, limit=limit
        )

    async def register(
        self,
        *,
        description: str | None = None,
        ephemeral: bool | None = None,
        name: str,
    ) -> RegisterRunnerResponse:
        """
        Register a new global runner.

        Args:
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

        Operation ID: registerAdminRunner
        """
        _payload = RegisterRunnerOptions(
            description=description,
            ephemeral=ephemeral,
            name=name,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request("POST", "/admin/actions/runners", json=_payload)
        return decode(_response, RegisterRunnerResponse)

    async def jobs(self, *, labels: str | None = None) -> builtins.list[ActionRunJob]:
        """
        Get action run jobs.

        Args:
            labels: a comma separated list of labels to search for

        Returns:
            RunJobList is a list of action run jobs.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: adminGetActionRunJobs
        """
        _query: dict[str, object] = {"labels": labels}

        _response = await self._client._request("GET", "/admin/actions/runners/jobs", params=_query)
        return decode(_response, list[ActionRunJob])

    async def registration_token(self) -> RegistrationToken:
        """
        Get a runner registration token for registering global runners.

        This operation has been deprecated in Forgejo 15. Use the web UI or
        [`/admin/actions/runners`](#/admin/registerAdminRunner) instead.

        Returns:
            RegistrationToken is a string used to register a runner with a server.

        Deprecated:
            Deprecated in the vendored Spec; generated for compatibility.

        Operation ID: adminGetRunnerRegistrationToken
        """
        _response = await self._client._request("GET", "/admin/actions/runners/registration-token")
        return decode(_response, RegistrationToken)

    async def get(self, runner_id: str) -> ActionRunner:
        """
        Get a particular runner, no matter whether it is a global runner or scoped to an organization, user, or
        repository.

        Args:
            runner_id: ID of the runner

        Returns:
            ActionRunner represents a runner.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: getAdminRunner
        """
        _response = await self._client._request("GET", f"/admin/actions/runners/{runner_id}")
        return decode(_response, ActionRunner)

    async def delete(self, runner_id: str) -> None:
        """
        Delete a particular runner, no matter whether it is a global runner or scoped to an organization, user, or
        repository.

        Args:
            runner_id: ID of the runner

        Returns:
            No content.

        Raises:
            BadRequestError: 400. APIError is error format response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: deleteAdminRunner
        """
        _response = await self._client._request("DELETE", f"/admin/actions/runners/{runner_id}")
        return decode(_response, None)


class AdminCron:
    """The ``admin.cron`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(self, *, page: int | None = None, limit: int | None = None) -> Paginated[Cron]:
        """
        List cron tasks.

        Args:
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            CronList.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: adminCronList
        """
        return self._client._paginate("GET", "/admin/cron", model=Cron, page=page, limit=limit)

    def run(self, task: str) -> None:
        """
        Run cron task.

        Args:
            task: task to run

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: adminCronRun
        """
        _response = self._client._request("POST", f"/admin/cron/{task}")
        return decode(_response, None)


class AsyncAdminCron:
    """The ``admin.cron`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(self, *, page: int | None = None, limit: int | None = None) -> AsyncPaginated[Cron]:
        """
        List cron tasks.

        Args:
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            CronList.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: adminCronList
        """
        return await self._client._paginate("GET", "/admin/cron", model=Cron, page=page, limit=limit)

    async def run(self, task: str) -> None:
        """
        Run cron task.

        Args:
            task: task to run

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: adminCronRun
        """
        _response = await self._client._request("POST", f"/admin/cron/{task}")
        return decode(_response, None)


class AdminEmails:
    """The ``admin.emails`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(self, *, page: int | None = None, limit: int | None = None) -> Paginated[Email]:
        """
        List all users' email addresses.

        Args:
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            EmailList.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: adminGetAllEmails
        """
        return self._client._paginate("GET", "/admin/emails", model=Email, page=page, limit=limit)

    def search(self, *, q: str | None = None, page: int | None = None, limit: int | None = None) -> Paginated[Email]:
        """
        Search users' email addresses.

        Args:
            q: keyword
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            EmailList.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: adminSearchEmails
        """
        _query: dict[str, object] = {"q": q}

        return self._client._paginate("GET", "/admin/emails/search", model=Email, params=_query, page=page, limit=limit)


class AsyncAdminEmails:
    """The ``admin.emails`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(self, *, page: int | None = None, limit: int | None = None) -> AsyncPaginated[Email]:
        """
        List all users' email addresses.

        Args:
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            EmailList.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: adminGetAllEmails
        """
        return await self._client._paginate("GET", "/admin/emails", model=Email, page=page, limit=limit)

    async def search(
        self,
        *,
        q: str | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> AsyncPaginated[Email]:
        """
        Search users' email addresses.

        Args:
            q: keyword
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            EmailList.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: adminSearchEmails
        """
        _query: dict[str, object] = {"q": q}

        return await self._client._paginate(
            "GET", "/admin/emails/search", model=Email, params=_query, page=page, limit=limit
        )


class AdminHooks:
    """The ``admin.hooks`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(self, *, page: int | None = None, limit: int | None = None) -> Paginated[Hook]:
        """
        List global (system) webhooks.

        Args:
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            HookListWithoutPagination - Hooks without pagination headers.

        Operation ID: adminListHooks
        """
        return self._client._paginate("GET", "/admin/hooks", model=Hook, page=page, limit=limit)

    def create(
        self,
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
            active:
            authorization_header:
            branch_filter:
            config:
            events:
            type:

        Returns:
            Hook.

        Operation ID: adminCreateHook
        """
        _payload = CreateHookOption(
            active=active,
            authorization_header=authorization_header,
            branch_filter=branch_filter,
            config=config,
            events=events,
            type=type,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("POST", "/admin/hooks", json=_payload)
        return decode(_response, Hook)

    def get(self, id: int) -> Hook:
        """
        Get a hook.

        Args:
            id: id of the hook to get

        Returns:
            Hook.

        Operation ID: adminGetHook
        """
        _response = self._client._request("GET", f"/admin/hooks/{id}")
        return decode(_response, Hook)

    def update(
        self,
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
            id: id of the hook to update
            active:
            authorization_header:
            branch_filter:
            config:
            events:

        Returns:
            Hook.

        Operation ID: adminEditHook
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

        _response = self._client._request("PATCH", f"/admin/hooks/{id}", json=_payload)
        return decode(_response, Hook)

    def delete(self, id: int) -> None:
        """
        Delete a hook.

        Args:
            id: id of the hook to delete

        Returns:
            No content.

        Operation ID: adminDeleteHook
        """
        _response = self._client._request("DELETE", f"/admin/hooks/{id}")
        return decode(_response, None)


class AsyncAdminHooks:
    """The ``admin.hooks`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(self, *, page: int | None = None, limit: int | None = None) -> AsyncPaginated[Hook]:
        """
        List global (system) webhooks.

        Args:
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            HookListWithoutPagination - Hooks without pagination headers.

        Operation ID: adminListHooks
        """
        return await self._client._paginate("GET", "/admin/hooks", model=Hook, page=page, limit=limit)

    async def create(
        self,
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
            active:
            authorization_header:
            branch_filter:
            config:
            events:
            type:

        Returns:
            Hook.

        Operation ID: adminCreateHook
        """
        _payload = CreateHookOption(
            active=active,
            authorization_header=authorization_header,
            branch_filter=branch_filter,
            config=config,
            events=events,
            type=type,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request("POST", "/admin/hooks", json=_payload)
        return decode(_response, Hook)

    async def get(self, id: int) -> Hook:
        """
        Get a hook.

        Args:
            id: id of the hook to get

        Returns:
            Hook.

        Operation ID: adminGetHook
        """
        _response = await self._client._request("GET", f"/admin/hooks/{id}")
        return decode(_response, Hook)

    async def update(
        self,
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
            id: id of the hook to update
            active:
            authorization_header:
            branch_filter:
            config:
            events:

        Returns:
            Hook.

        Operation ID: adminEditHook
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

        _response = await self._client._request("PATCH", f"/admin/hooks/{id}", json=_payload)
        return decode(_response, Hook)

    async def delete(self, id: int) -> None:
        """
        Delete a hook.

        Args:
            id: id of the hook to delete

        Returns:
            No content.

        Operation ID: adminDeleteHook
        """
        _response = await self._client._request("DELETE", f"/admin/hooks/{id}")
        return decode(_response, None)


class AdminQuota:
    """The ``admin.quota`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client
        self.groups: AdminQuotaGroups = AdminQuotaGroups(client)
        self.rules: AdminQuotaRules = AdminQuotaRules(client)


class AsyncAdminQuota:
    """The ``admin.quota`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client
        self.groups: AsyncAdminQuotaGroups = AsyncAdminQuotaGroups(client)
        self.rules: AsyncAdminQuotaRules = AsyncAdminQuotaRules(client)


class AdminQuotaGroups:
    """The ``admin.quota.groups`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client
        self.rules: AdminQuotaGroupsRules = AdminQuotaGroupsRules(client)
        self.users: AdminQuotaGroupsUsers = AdminQuotaGroupsUsers(client)

    def list(self) -> builtins.list[QuotaGroup]:
        """
        List the available quota groups.

        Returns:
            QuotaGroupList.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: adminListQuotaGroups
        """
        _response = self._client._request("GET", "/admin/quota/groups")
        return decode(_response, list[QuotaGroup])

    def create(
        self,
        *,
        name: str | None = None,
        rules: builtins.list[CreateQuotaRuleOptions] | None = None,
    ) -> QuotaGroup:
        """
        Create a new quota group.

        Args:
            name: Name of the quota group to create
            rules: Rules to add to the newly created group. If a rule does not exist, it will be created.

        Returns:
            QuotaGroup.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            ConflictError: 409. APIError is error format response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: adminCreateQuotaGroup
        """
        _payload = CreateQuotaGroupOptions(
            name=name,
            rules=rules,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("POST", "/admin/quota/groups", json=_payload)
        return decode(_response, QuotaGroup)

    def get(self, quotagroup: str) -> QuotaGroup:
        """
        Get information about the quota group.

        Args:
            quotagroup: quota group to query

        Returns:
            QuotaGroup.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: adminGetQuotaGroup
        """
        _response = self._client._request("GET", f"/admin/quota/groups/{quotagroup}")
        return decode(_response, QuotaGroup)

    def delete(self, quotagroup: str) -> None:
        """
        Delete a quota group.

        Args:
            quotagroup: quota group to delete

        Returns:
            No content.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: adminDeleteQuotaGroup
        """
        _response = self._client._request("DELETE", f"/admin/quota/groups/{quotagroup}")
        return decode(_response, None)


class AsyncAdminQuotaGroups:
    """The ``admin.quota.groups`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client
        self.rules: AsyncAdminQuotaGroupsRules = AsyncAdminQuotaGroupsRules(client)
        self.users: AsyncAdminQuotaGroupsUsers = AsyncAdminQuotaGroupsUsers(client)

    async def list(self) -> builtins.list[QuotaGroup]:
        """
        List the available quota groups.

        Returns:
            QuotaGroupList.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: adminListQuotaGroups
        """
        _response = await self._client._request("GET", "/admin/quota/groups")
        return decode(_response, list[QuotaGroup])

    async def create(
        self,
        *,
        name: str | None = None,
        rules: builtins.list[CreateQuotaRuleOptions] | None = None,
    ) -> QuotaGroup:
        """
        Create a new quota group.

        Args:
            name: Name of the quota group to create
            rules: Rules to add to the newly created group. If a rule does not exist, it will be created.

        Returns:
            QuotaGroup.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            ConflictError: 409. APIError is error format response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: adminCreateQuotaGroup
        """
        _payload = CreateQuotaGroupOptions(
            name=name,
            rules=rules,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request("POST", "/admin/quota/groups", json=_payload)
        return decode(_response, QuotaGroup)

    async def get(self, quotagroup: str) -> QuotaGroup:
        """
        Get information about the quota group.

        Args:
            quotagroup: quota group to query

        Returns:
            QuotaGroup.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: adminGetQuotaGroup
        """
        _response = await self._client._request("GET", f"/admin/quota/groups/{quotagroup}")
        return decode(_response, QuotaGroup)

    async def delete(self, quotagroup: str) -> None:
        """
        Delete a quota group.

        Args:
            quotagroup: quota group to delete

        Returns:
            No content.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: adminDeleteQuotaGroup
        """
        _response = await self._client._request("DELETE", f"/admin/quota/groups/{quotagroup}")
        return decode(_response, None)


class AdminQuotaGroupsRules:
    """The ``admin.quota.groups.rules`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def add(self, quotagroup: str, quotarule: str) -> None:
        """
        Adds a rule to a quota group.

        Args:
            quotagroup: quota group to add a rule to
            quotarule: the name of the quota rule to add to the group

        Returns:
            No content.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            ConflictError: 409. APIError is error format response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: adminAddRuleToQuotaGroup
        """
        _response = self._client._request("PUT", f"/admin/quota/groups/{quotagroup}/rules/{quotarule}")
        return decode(_response, None)

    def remove(self, quotagroup: str, quotarule: str) -> None:
        """
        Removes a rule from a quota group.

        Args:
            quotagroup: quota group to remove a rule from
            quotarule: the name of the quota rule to remove from the group

        Returns:
            No content.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: adminRemoveRuleFromQuotaGroup
        """
        _response = self._client._request("DELETE", f"/admin/quota/groups/{quotagroup}/rules/{quotarule}")
        return decode(_response, None)


class AsyncAdminQuotaGroupsRules:
    """The ``admin.quota.groups.rules`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def add(self, quotagroup: str, quotarule: str) -> None:
        """
        Adds a rule to a quota group.

        Args:
            quotagroup: quota group to add a rule to
            quotarule: the name of the quota rule to add to the group

        Returns:
            No content.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            ConflictError: 409. APIError is error format response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: adminAddRuleToQuotaGroup
        """
        _response = await self._client._request("PUT", f"/admin/quota/groups/{quotagroup}/rules/{quotarule}")
        return decode(_response, None)

    async def remove(self, quotagroup: str, quotarule: str) -> None:
        """
        Removes a rule from a quota group.

        Args:
            quotagroup: quota group to remove a rule from
            quotarule: the name of the quota rule to remove from the group

        Returns:
            No content.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: adminRemoveRuleFromQuotaGroup
        """
        _response = await self._client._request("DELETE", f"/admin/quota/groups/{quotagroup}/rules/{quotarule}")
        return decode(_response, None)


class AdminQuotaGroupsUsers:
    """The ``admin.quota.groups.users`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(self, quotagroup: str) -> builtins.list[User]:
        """
        List users in a quota group.

        Args:
            quotagroup: quota group to list members of

        Returns:
            UserList.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: adminListUsersInQuotaGroup
        """
        _response = self._client._request("GET", f"/admin/quota/groups/{quotagroup}/users")
        return decode(_response, list[User])

    def add(self, quotagroup: str, username: str) -> None:
        """
        Add a user to a quota group.

        Args:
            quotagroup: quota group to add the user to
            username: username of the user to add to the quota group

        Returns:
            No content.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            ConflictError: 409. APIError is error format response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: adminAddUserToQuotaGroup
        """
        _response = self._client._request("PUT", f"/admin/quota/groups/{quotagroup}/users/{username}")
        return decode(_response, None)

    def remove(self, quotagroup: str, username: str) -> None:
        """
        Remove a user from a quota group.

        Args:
            quotagroup: quota group to remove a user from
            username: username of the user to remove from the quota group

        Returns:
            No content.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: adminRemoveUserFromQuotaGroup
        """
        _response = self._client._request("DELETE", f"/admin/quota/groups/{quotagroup}/users/{username}")
        return decode(_response, None)


class AsyncAdminQuotaGroupsUsers:
    """The ``admin.quota.groups.users`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(self, quotagroup: str) -> builtins.list[User]:
        """
        List users in a quota group.

        Args:
            quotagroup: quota group to list members of

        Returns:
            UserList.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: adminListUsersInQuotaGroup
        """
        _response = await self._client._request("GET", f"/admin/quota/groups/{quotagroup}/users")
        return decode(_response, list[User])

    async def add(self, quotagroup: str, username: str) -> None:
        """
        Add a user to a quota group.

        Args:
            quotagroup: quota group to add the user to
            username: username of the user to add to the quota group

        Returns:
            No content.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            ConflictError: 409. APIError is error format response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: adminAddUserToQuotaGroup
        """
        _response = await self._client._request("PUT", f"/admin/quota/groups/{quotagroup}/users/{username}")
        return decode(_response, None)

    async def remove(self, quotagroup: str, username: str) -> None:
        """
        Remove a user from a quota group.

        Args:
            quotagroup: quota group to remove a user from
            username: username of the user to remove from the quota group

        Returns:
            No content.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: adminRemoveUserFromQuotaGroup
        """
        _response = await self._client._request("DELETE", f"/admin/quota/groups/{quotagroup}/users/{username}")
        return decode(_response, None)


class AdminQuotaRules:
    """The ``admin.quota.rules`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(self) -> builtins.list[QuotaRuleInfo]:
        """
        List the available quota rules.

        Returns:
            QuotaRuleInfoList.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: adminListQuotaRules
        """
        _response = self._client._request("GET", "/admin/quota/rules")
        return decode(_response, list[QuotaRuleInfo])

    def create(
        self,
        *,
        limit: int | None = None,
        name: str | None = None,
        subjects: builtins.list[str] | None = None,
    ) -> QuotaRuleInfo:
        """
        Create a new quota rule.

        Args:
            limit: The limit set by the rule
            name: Name of the rule to create
            subjects: The subjects affected by the rule

        Returns:
            QuotaRuleInfo.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            ConflictError: 409. APIError is error format response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: adminCreateQuotaRule
        """
        _payload = CreateQuotaRuleOptions(
            limit=limit,
            name=name,
            subjects=subjects,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("POST", "/admin/quota/rules", json=_payload)
        return decode(_response, QuotaRuleInfo)

    def get(self, quotarule: str) -> QuotaRuleInfo:
        """
        Get information about a quota rule.

        Args:
            quotarule: quota rule to query

        Returns:
            QuotaRuleInfo.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: adminGetQuotaRule
        """
        _response = self._client._request("GET", f"/admin/quota/rules/{quotarule}")
        return decode(_response, QuotaRuleInfo)

    def update(
        self,
        quotarule: str,
        *,
        limit: int | None = None,
        subjects: builtins.list[str] | None = None,
    ) -> QuotaRuleInfo:
        """
        Change an existing quota rule.

        Args:
            quotarule: Quota rule to change
            limit: The limit set by the rule
            subjects: The subjects affected by the rule

        Returns:
            QuotaRuleInfo.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: adminEditQuotaRule
        """
        _payload = EditQuotaRuleOptions(
            limit=limit,
            subjects=subjects,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("PATCH", f"/admin/quota/rules/{quotarule}", json=_payload)
        return decode(_response, QuotaRuleInfo)

    def delete(self, quotarule: str) -> None:
        """
        Deletes a quota rule.

        Args:
            quotarule: quota rule to delete

        Returns:
            No content.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: adminDeleteQuotaRule
        """
        _response = self._client._request("DELETE", f"/admin/quota/rules/{quotarule}")
        return decode(_response, None)


class AsyncAdminQuotaRules:
    """The ``admin.quota.rules`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(self) -> builtins.list[QuotaRuleInfo]:
        """
        List the available quota rules.

        Returns:
            QuotaRuleInfoList.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: adminListQuotaRules
        """
        _response = await self._client._request("GET", "/admin/quota/rules")
        return decode(_response, list[QuotaRuleInfo])

    async def create(
        self,
        *,
        limit: int | None = None,
        name: str | None = None,
        subjects: builtins.list[str] | None = None,
    ) -> QuotaRuleInfo:
        """
        Create a new quota rule.

        Args:
            limit: The limit set by the rule
            name: Name of the rule to create
            subjects: The subjects affected by the rule

        Returns:
            QuotaRuleInfo.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            ConflictError: 409. APIError is error format response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: adminCreateQuotaRule
        """
        _payload = CreateQuotaRuleOptions(
            limit=limit,
            name=name,
            subjects=subjects,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request("POST", "/admin/quota/rules", json=_payload)
        return decode(_response, QuotaRuleInfo)

    async def get(self, quotarule: str) -> QuotaRuleInfo:
        """
        Get information about a quota rule.

        Args:
            quotarule: quota rule to query

        Returns:
            QuotaRuleInfo.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: adminGetQuotaRule
        """
        _response = await self._client._request("GET", f"/admin/quota/rules/{quotarule}")
        return decode(_response, QuotaRuleInfo)

    async def update(
        self,
        quotarule: str,
        *,
        limit: int | None = None,
        subjects: builtins.list[str] | None = None,
    ) -> QuotaRuleInfo:
        """
        Change an existing quota rule.

        Args:
            quotarule: Quota rule to change
            limit: The limit set by the rule
            subjects: The subjects affected by the rule

        Returns:
            QuotaRuleInfo.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: adminEditQuotaRule
        """
        _payload = EditQuotaRuleOptions(
            limit=limit,
            subjects=subjects,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request("PATCH", f"/admin/quota/rules/{quotarule}", json=_payload)
        return decode(_response, QuotaRuleInfo)

    async def delete(self, quotarule: str) -> None:
        """
        Deletes a quota rule.

        Args:
            quotarule: quota rule to delete

        Returns:
            No content.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: adminDeleteQuotaRule
        """
        _response = await self._client._request("DELETE", f"/admin/quota/rules/{quotarule}")
        return decode(_response, None)


class AdminRunners:
    """The ``admin.runners`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def jobs(self, *, labels: str | None = None) -> builtins.list[ActionRunJob]:
        """
        Search action jobs according to filter conditions.

        This operation has been deprecated in Forgejo 15. Use
        [`/admin/actions/runners/jobs`](#/admin/adminGetActionRunJobs) instead.

        Args:
            labels: a comma separated list of run job labels to search for

        Returns:
            RunJobList is a list of action run jobs.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Deprecated:
            Deprecated in the vendored Spec; generated for compatibility.

        Operation ID: adminSearchRunJobs
        """
        _query: dict[str, object] = {"labels": labels}

        _response = self._client._request("GET", "/admin/runners/jobs", params=_query)
        return decode(_response, list[ActionRunJob])

    def registration_token(self) -> RegistrationToken:
        """
        Get a runner registration token for registering global runners.

        This operation has been deprecated in Forgejo 15. Use the web UI or
        [`/admin/actions/runners`](#/admin/registerAdminRunner) instead.

        Returns:
            RegistrationToken is a string used to register a runner with a server.

        Deprecated:
            Deprecated in the vendored Spec; generated for compatibility.

        Operation ID: adminGetRegistrationToken
        """
        _response = self._client._request("GET", "/admin/runners/registration-token")
        return decode(_response, RegistrationToken)


class AsyncAdminRunners:
    """The ``admin.runners`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def jobs(self, *, labels: str | None = None) -> builtins.list[ActionRunJob]:
        """
        Search action jobs according to filter conditions.

        This operation has been deprecated in Forgejo 15. Use
        [`/admin/actions/runners/jobs`](#/admin/adminGetActionRunJobs) instead.

        Args:
            labels: a comma separated list of run job labels to search for

        Returns:
            RunJobList is a list of action run jobs.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Deprecated:
            Deprecated in the vendored Spec; generated for compatibility.

        Operation ID: adminSearchRunJobs
        """
        _query: dict[str, object] = {"labels": labels}

        _response = await self._client._request("GET", "/admin/runners/jobs", params=_query)
        return decode(_response, list[ActionRunJob])

    async def registration_token(self) -> RegistrationToken:
        """
        Get a runner registration token for registering global runners.

        This operation has been deprecated in Forgejo 15. Use the web UI or
        [`/admin/actions/runners`](#/admin/registerAdminRunner) instead.

        Returns:
            RegistrationToken is a string used to register a runner with a server.

        Deprecated:
            Deprecated in the vendored Spec; generated for compatibility.

        Operation ID: adminGetRegistrationToken
        """
        _response = await self._client._request("GET", "/admin/runners/registration-token")
        return decode(_response, RegistrationToken)


class AdminUnadopted:
    """The ``admin.unadopted`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(
        self,
        *,
        page: int | None = None,
        limit: int | None = None,
        pattern: str | None = None,
    ) -> builtins.list[str]:
        """
        List unadopted repositories.

        Args:
            page: page number of results to return (1-based)
            limit: page size of results
            pattern: pattern of repositories to search for

        Returns:
            StringSlice.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: adminUnadoptedList
        """
        _query: dict[str, object] = {"page": page, "limit": limit, "pattern": pattern}

        _response = self._client._request("GET", "/admin/unadopted", params=_query)
        return decode(_response, list[str])

    def adopt(self, owner: str, repo: str) -> None:
        """
        Adopt unadopted files as a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: adminAdoptRepository
        """
        _response = self._client._request("POST", f"/admin/unadopted/{owner}/{repo}")
        return decode(_response, None)

    def delete(self, owner: str, repo: str) -> None:
        """
        Delete unadopted files.

        Args:
            owner: owner of the repo
            repo: name of the repo

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: adminDeleteUnadoptedRepository
        """
        _response = self._client._request("DELETE", f"/admin/unadopted/{owner}/{repo}")
        return decode(_response, None)


class AsyncAdminUnadopted:
    """The ``admin.unadopted`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(
        self,
        *,
        page: int | None = None,
        limit: int | None = None,
        pattern: str | None = None,
    ) -> builtins.list[str]:
        """
        List unadopted repositories.

        Args:
            page: page number of results to return (1-based)
            limit: page size of results
            pattern: pattern of repositories to search for

        Returns:
            StringSlice.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: adminUnadoptedList
        """
        _query: dict[str, object] = {"page": page, "limit": limit, "pattern": pattern}

        _response = await self._client._request("GET", "/admin/unadopted", params=_query)
        return decode(_response, list[str])

    async def adopt(self, owner: str, repo: str) -> None:
        """
        Adopt unadopted files as a repository.

        Args:
            owner: owner of the repo
            repo: name of the repo

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: adminAdoptRepository
        """
        _response = await self._client._request("POST", f"/admin/unadopted/{owner}/{repo}")
        return decode(_response, None)

    async def delete(self, owner: str, repo: str) -> None:
        """
        Delete unadopted files.

        Args:
            owner: owner of the repo
            repo: name of the repo

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: adminDeleteUnadoptedRepository
        """
        _response = await self._client._request("DELETE", f"/admin/unadopted/{owner}/{repo}")
        return decode(_response, None)


class AdminUsers:
    """The ``admin.users`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client
        self.emails: AdminUsersEmails = AdminUsersEmails(client)
        self.keys: AdminUsersKeys = AdminUsersKeys(client)
        self.quota: AdminUsersQuota = AdminUsersQuota(client)
        self.tokens: AdminUsersTokens = AdminUsersTokens(client)

    def list(
        self,
        *,
        source_id: int | None = None,
        login_name: str | None = None,
        is_2fa_enabled: bool | None = None,
        sort: Literal["oldest", "newest", "alphabetically", "reversealphabetically", "recentupdate", "leastupdate"]
        | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> Paginated[User]:
        """
        Search users according filter conditions.

        Args:
            source_id: ID of the user's login source to search for
            login_name: user's login name to search for
            is_2fa_enabled: whether or not to filter users with the 2fa enabled
            sort: sort order of results
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            UserList.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: adminSearchUsers
        """
        _query: dict[str, object] = {
            "source_id": source_id,
            "login_name": login_name,
            "is_2fa_enabled": is_2fa_enabled,
            "sort": sort,
        }

        return self._client._paginate("GET", "/admin/users", model=User, params=_query, page=page, limit=limit)

    def create(
        self,
        *,
        created_at: datetime | None = None,
        email: str,
        full_name: str | None = None,
        login_name: str | None = None,
        must_change_password: bool | None = None,
        password: str | None = None,
        restricted: bool | None = None,
        send_notify: bool | None = None,
        source_id: int | None = None,
        username: str,
        visibility: str | None = None,
    ) -> User:
        """
        Create a user account.

        Args:
            created_at: For explicitly setting the user creation timestamp. Useful when users are migrated from other
                systems. When omitted, the user's creation timestamp will be set to "now".
            email:
            full_name:
            login_name:
            must_change_password:
            password:
            restricted:
            send_notify:
            source_id:
            username:
            visibility:

        Returns:
            User.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: adminCreateUser
        """
        _payload = CreateUserOption(
            created_at=created_at,
            email=email,
            full_name=full_name,
            login_name=login_name,
            must_change_password=must_change_password,
            password=password,
            restricted=restricted,
            send_notify=send_notify,
            source_id=source_id,
            username=username,
            visibility=visibility,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("POST", "/admin/users", json=_payload)
        return decode(_response, User)

    def update(
        self,
        username: str,
        *,
        active: bool | None = None,
        admin: bool | None = None,
        allow_create_organization: bool | None = None,
        allow_git_hook: bool | None = None,
        allow_import_local: bool | None = None,
        description: str | None = None,
        email: str | None = None,
        full_name: str | None = None,
        hide_email: bool | None = None,
        location: str | None = None,
        login_name: str | None = None,
        max_repo_creation: int | None = None,
        must_change_password: bool | None = None,
        password: str | None = None,
        prohibit_login: bool | None = None,
        pronouns: str | None = None,
        restricted: bool | None = None,
        source_id: int | None = None,
        visibility: str | None = None,
        website: str | None = None,
    ) -> User:
        """
        Edit an existing user.

        Args:
            username: username of user to edit
            active:
            admin:
            allow_create_organization:
            allow_git_hook:
            allow_import_local:
            description:
            email:
            full_name:
            hide_email:
            location:
            login_name:
            max_repo_creation:
            must_change_password:
            password:
            prohibit_login:
            pronouns:
            restricted:
            source_id:
            visibility:
            website:

        Returns:
            User.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: adminEditUser
        """
        if (
            active is not None
            or admin is not None
            or allow_create_organization is not None
            or allow_git_hook is not None
            or allow_import_local is not None
            or description is not None
            or email is not None
            or full_name is not None
            or hide_email is not None
            or location is not None
            or login_name is not None
            or max_repo_creation is not None
            or must_change_password is not None
            or password is not None
            or prohibit_login is not None
            or pronouns is not None
            or restricted is not None
            or source_id is not None
            or visibility is not None
            or website is not None
        ):
            _payload = EditUserOption(
                active=active,
                admin=admin,
                allow_create_organization=allow_create_organization,
                allow_git_hook=allow_git_hook,
                allow_import_local=allow_import_local,
                description=description,
                email=email,
                full_name=full_name,
                hide_email=hide_email,
                location=location,
                login_name=login_name,
                max_repo_creation=max_repo_creation,
                must_change_password=must_change_password,
                password=password,
                prohibit_login=prohibit_login,
                pronouns=pronouns,
                restricted=restricted,
                source_id=source_id,
                visibility=visibility,
                website=website,
            ).model_dump(mode="json", by_alias=True, exclude_none=True)
        else:
            _payload = None

        _response = self._client._request("PATCH", f"/admin/users/{username}", json=_payload)
        return decode(_response, User)

    def delete(self, username: str, *, purge: bool | None = None) -> None:
        """
        Delete user account.

        Args:
            username: username of user to delete
            purge: purge the user from the system completely

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: adminDeleteUser
        """
        _query: dict[str, object] = {"purge": purge}

        _response = self._client._request("DELETE", f"/admin/users/{username}", params=_query)
        return decode(_response, None)

    def create_org(
        self,
        username: str,
        *,
        description: str | None = None,
        email: str | None = None,
        full_name: str | None = None,
        location: str | None = None,
        repo_admin_change_team_access: bool | None = None,
        body_username: str,
        visibility: CreateOrgOptionVisibility | None = None,
        website: str | None = None,
    ) -> Organization:
        """
        Create an organization.

        Args:
            username: username of the user that will own the created organization
            description:
            email:
            full_name:
            location:
            repo_admin_change_team_access:
            body_username: Wire field ``username``.
            visibility: possible values are `public` (default), `limited` or `private`
            website:

        Returns:
            Organization.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: adminCreateOrg
        """
        _payload = CreateOrgOption(
            description=description,
            email=email,
            full_name=full_name,
            location=location,
            repo_admin_change_team_access=repo_admin_change_team_access,
            username=body_username,
            visibility=visibility,
            website=website,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("POST", f"/admin/users/{username}/orgs", json=_payload)
        return decode(_response, Organization)

    def rename(self, username: str, *, new_username: str) -> None:
        """
        Rename a user.

        Args:
            username: existing username of user
            new_username: New username for this user. This name cannot be in use yet by any other user.

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: adminRenameUser
        """
        _payload = RenameUserOption(
            new_username=new_username,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("POST", f"/admin/users/{username}/rename", json=_payload)
        return decode(_response, None)

    def create_repo(
        self,
        username: str,
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
        Create a repository on behalf of a user.

        Args:
            username: username of the user. This user will own the created repository
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
            ConflictError: 409. APIError is error format response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: adminCreateRepo
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

        _response = self._client._request("POST", f"/admin/users/{username}/repos", json=_payload)
        return decode(_response, Repository)


class AsyncAdminUsers:
    """The ``admin.users`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client
        self.emails: AsyncAdminUsersEmails = AsyncAdminUsersEmails(client)
        self.keys: AsyncAdminUsersKeys = AsyncAdminUsersKeys(client)
        self.quota: AsyncAdminUsersQuota = AsyncAdminUsersQuota(client)
        self.tokens: AsyncAdminUsersTokens = AsyncAdminUsersTokens(client)

    async def list(
        self,
        *,
        source_id: int | None = None,
        login_name: str | None = None,
        is_2fa_enabled: bool | None = None,
        sort: Literal["oldest", "newest", "alphabetically", "reversealphabetically", "recentupdate", "leastupdate"]
        | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> AsyncPaginated[User]:
        """
        Search users according filter conditions.

        Args:
            source_id: ID of the user's login source to search for
            login_name: user's login name to search for
            is_2fa_enabled: whether or not to filter users with the 2fa enabled
            sort: sort order of results
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            UserList.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: adminSearchUsers
        """
        _query: dict[str, object] = {
            "source_id": source_id,
            "login_name": login_name,
            "is_2fa_enabled": is_2fa_enabled,
            "sort": sort,
        }

        return await self._client._paginate("GET", "/admin/users", model=User, params=_query, page=page, limit=limit)

    async def create(
        self,
        *,
        created_at: datetime | None = None,
        email: str,
        full_name: str | None = None,
        login_name: str | None = None,
        must_change_password: bool | None = None,
        password: str | None = None,
        restricted: bool | None = None,
        send_notify: bool | None = None,
        source_id: int | None = None,
        username: str,
        visibility: str | None = None,
    ) -> User:
        """
        Create a user account.

        Args:
            created_at: For explicitly setting the user creation timestamp. Useful when users are migrated from other
                systems. When omitted, the user's creation timestamp will be set to "now".
            email:
            full_name:
            login_name:
            must_change_password:
            password:
            restricted:
            send_notify:
            source_id:
            username:
            visibility:

        Returns:
            User.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: adminCreateUser
        """
        _payload = CreateUserOption(
            created_at=created_at,
            email=email,
            full_name=full_name,
            login_name=login_name,
            must_change_password=must_change_password,
            password=password,
            restricted=restricted,
            send_notify=send_notify,
            source_id=source_id,
            username=username,
            visibility=visibility,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request("POST", "/admin/users", json=_payload)
        return decode(_response, User)

    async def update(
        self,
        username: str,
        *,
        active: bool | None = None,
        admin: bool | None = None,
        allow_create_organization: bool | None = None,
        allow_git_hook: bool | None = None,
        allow_import_local: bool | None = None,
        description: str | None = None,
        email: str | None = None,
        full_name: str | None = None,
        hide_email: bool | None = None,
        location: str | None = None,
        login_name: str | None = None,
        max_repo_creation: int | None = None,
        must_change_password: bool | None = None,
        password: str | None = None,
        prohibit_login: bool | None = None,
        pronouns: str | None = None,
        restricted: bool | None = None,
        source_id: int | None = None,
        visibility: str | None = None,
        website: str | None = None,
    ) -> User:
        """
        Edit an existing user.

        Args:
            username: username of user to edit
            active:
            admin:
            allow_create_organization:
            allow_git_hook:
            allow_import_local:
            description:
            email:
            full_name:
            hide_email:
            location:
            login_name:
            max_repo_creation:
            must_change_password:
            password:
            prohibit_login:
            pronouns:
            restricted:
            source_id:
            visibility:
            website:

        Returns:
            User.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: adminEditUser
        """
        if (
            active is not None
            or admin is not None
            or allow_create_organization is not None
            or allow_git_hook is not None
            or allow_import_local is not None
            or description is not None
            or email is not None
            or full_name is not None
            or hide_email is not None
            or location is not None
            or login_name is not None
            or max_repo_creation is not None
            or must_change_password is not None
            or password is not None
            or prohibit_login is not None
            or pronouns is not None
            or restricted is not None
            or source_id is not None
            or visibility is not None
            or website is not None
        ):
            _payload = EditUserOption(
                active=active,
                admin=admin,
                allow_create_organization=allow_create_organization,
                allow_git_hook=allow_git_hook,
                allow_import_local=allow_import_local,
                description=description,
                email=email,
                full_name=full_name,
                hide_email=hide_email,
                location=location,
                login_name=login_name,
                max_repo_creation=max_repo_creation,
                must_change_password=must_change_password,
                password=password,
                prohibit_login=prohibit_login,
                pronouns=pronouns,
                restricted=restricted,
                source_id=source_id,
                visibility=visibility,
                website=website,
            ).model_dump(mode="json", by_alias=True, exclude_none=True)
        else:
            _payload = None

        _response = await self._client._request("PATCH", f"/admin/users/{username}", json=_payload)
        return decode(_response, User)

    async def delete(self, username: str, *, purge: bool | None = None) -> None:
        """
        Delete user account.

        Args:
            username: username of user to delete
            purge: purge the user from the system completely

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: adminDeleteUser
        """
        _query: dict[str, object] = {"purge": purge}

        _response = await self._client._request("DELETE", f"/admin/users/{username}", params=_query)
        return decode(_response, None)

    async def create_org(
        self,
        username: str,
        *,
        description: str | None = None,
        email: str | None = None,
        full_name: str | None = None,
        location: str | None = None,
        repo_admin_change_team_access: bool | None = None,
        body_username: str,
        visibility: CreateOrgOptionVisibility | None = None,
        website: str | None = None,
    ) -> Organization:
        """
        Create an organization.

        Args:
            username: username of the user that will own the created organization
            description:
            email:
            full_name:
            location:
            repo_admin_change_team_access:
            body_username: Wire field ``username``.
            visibility: possible values are `public` (default), `limited` or `private`
            website:

        Returns:
            Organization.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: adminCreateOrg
        """
        _payload = CreateOrgOption(
            description=description,
            email=email,
            full_name=full_name,
            location=location,
            repo_admin_change_team_access=repo_admin_change_team_access,
            username=body_username,
            visibility=visibility,
            website=website,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request("POST", f"/admin/users/{username}/orgs", json=_payload)
        return decode(_response, Organization)

    async def rename(self, username: str, *, new_username: str) -> None:
        """
        Rename a user.

        Args:
            username: existing username of user
            new_username: New username for this user. This name cannot be in use yet by any other user.

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: adminRenameUser
        """
        _payload = RenameUserOption(
            new_username=new_username,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request("POST", f"/admin/users/{username}/rename", json=_payload)
        return decode(_response, None)

    async def create_repo(
        self,
        username: str,
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
        Create a repository on behalf of a user.

        Args:
            username: username of the user. This user will own the created repository
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
            ConflictError: 409. APIError is error format response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: adminCreateRepo
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

        _response = await self._client._request("POST", f"/admin/users/{username}/repos", json=_payload)
        return decode(_response, Repository)


class AdminUsersEmails:
    """The ``admin.users.emails`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(self, username: str) -> builtins.list[Email]:
        """
        List all email addresses for a user.

        Args:
            username: username of user to get email addresses of

        Returns:
            EmailList.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: adminListUserEmails
        """
        _response = self._client._request("GET", f"/admin/users/{username}/emails")
        return decode(_response, list[Email])

    def delete(self, username: str, *, emails: builtins.list[str] | None = None) -> None:
        """
        Delete email addresses from a user's account.

        Args:
            username: username of user to delete email addresses from
            emails: email addresses to delete

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: adminDeleteUserEmails
        """
        if emails is not None:
            _payload = DeleteEmailOption(emails=emails).model_dump(mode="json", by_alias=True, exclude_none=True)
        else:
            _payload = None

        _response = self._client._request("DELETE", f"/admin/users/{username}/emails", json=_payload)
        return decode(_response, None)


class AsyncAdminUsersEmails:
    """The ``admin.users.emails`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(self, username: str) -> builtins.list[Email]:
        """
        List all email addresses for a user.

        Args:
            username: username of user to get email addresses of

        Returns:
            EmailList.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: adminListUserEmails
        """
        _response = await self._client._request("GET", f"/admin/users/{username}/emails")
        return decode(_response, list[Email])

    async def delete(self, username: str, *, emails: builtins.list[str] | None = None) -> None:
        """
        Delete email addresses from a user's account.

        Args:
            username: username of user to delete email addresses from
            emails: email addresses to delete

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: adminDeleteUserEmails
        """
        if emails is not None:
            _payload = DeleteEmailOption(emails=emails).model_dump(mode="json", by_alias=True, exclude_none=True)
        else:
            _payload = None

        _response = await self._client._request("DELETE", f"/admin/users/{username}/emails", json=_payload)
        return decode(_response, None)


class AdminUsersKeys:
    """The ``admin.users.keys`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def create(self, username: str, *, key: str, read_only: bool | None = None, title: str) -> PublicKey:
        """
        Add an SSH public key to user's account.

        Args:
            username: username of the user
            key: An armored SSH key to add
            read_only: Describe if the key has only read access or read/write
            title: Title of the key to add

        Returns:
            PublicKey.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: adminCreatePublicKey
        """
        _payload = CreateKeyOption(
            key=key,
            read_only=read_only,
            title=title,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("POST", f"/admin/users/{username}/keys", json=_payload)
        return decode(_response, PublicKey)

    def delete(self, username: str, id: int) -> None:
        """
        Remove a public key from user's account.

        Args:
            username: username of user
            id: id of the key to delete

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: adminDeleteUserPublicKey
        """
        _response = self._client._request("DELETE", f"/admin/users/{username}/keys/{id}")
        return decode(_response, None)


class AsyncAdminUsersKeys:
    """The ``admin.users.keys`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def create(self, username: str, *, key: str, read_only: bool | None = None, title: str) -> PublicKey:
        """
        Add an SSH public key to user's account.

        Args:
            username: username of the user
            key: An armored SSH key to add
            read_only: Describe if the key has only read access or read/write
            title: Title of the key to add

        Returns:
            PublicKey.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: adminCreatePublicKey
        """
        _payload = CreateKeyOption(
            key=key,
            read_only=read_only,
            title=title,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request("POST", f"/admin/users/{username}/keys", json=_payload)
        return decode(_response, PublicKey)

    async def delete(self, username: str, id: int) -> None:
        """
        Remove a public key from user's account.

        Args:
            username: username of user
            id: id of the key to delete

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: adminDeleteUserPublicKey
        """
        _response = await self._client._request("DELETE", f"/admin/users/{username}/keys/{id}")
        return decode(_response, None)


class AdminUsersQuota:
    """The ``admin.users.quota`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def get(self, username: str) -> QuotaInfo:
        """
        Get the user's quota info.

        Args:
            username: username of user to query

        Returns:
            QuotaInfo.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: adminGetUserQuota
        """
        _response = self._client._request("GET", f"/admin/users/{username}/quota")
        return decode(_response, QuotaInfo)

    def set_groups(self, username: str, *, groups: builtins.list[str]) -> None:
        """
        Set the user's quota groups to a given list.

        Args:
            username: username of the user to modify the quota groups from
            groups: Quota groups the user shall have

        Returns:
            No content.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: adminSetUserQuotaGroups
        """
        _payload = SetUserQuotaGroupsOptions(
            groups=groups,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("POST", f"/admin/users/{username}/quota/groups", json=_payload)
        return decode(_response, None)


class AsyncAdminUsersQuota:
    """The ``admin.users.quota`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def get(self, username: str) -> QuotaInfo:
        """
        Get the user's quota info.

        Args:
            username: username of user to query

        Returns:
            QuotaInfo.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: adminGetUserQuota
        """
        _response = await self._client._request("GET", f"/admin/users/{username}/quota")
        return decode(_response, QuotaInfo)

    async def set_groups(self, username: str, *, groups: builtins.list[str]) -> None:
        """
        Set the user's quota groups to a given list.

        Args:
            username: username of the user to modify the quota groups from
            groups: Quota groups the user shall have

        Returns:
            No content.

        Raises:
            BadRequestError: 400. APIError is error format response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: adminSetUserQuotaGroups
        """
        _payload = SetUserQuotaGroupsOptions(
            groups=groups,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request("POST", f"/admin/users/{username}/quota/groups", json=_payload)
        return decode(_response, None)


class AdminUsersTokens:
    """The ``admin.users.tokens`` namespace."""

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

        Operation ID: adminListUserAccessTokens
        """
        return self._client._paginate(
            "GET", f"/admin/users/{username}/tokens", model=AccessToken, page=page, limit=limit
        )

    def create(
        self,
        username: str,
        *,
        name: str,
        repositories: builtins.list[RepoTargetOption] | None = None,
        scopes: builtins.list[str] | None = None,
    ) -> AccessToken:
        """
        Create an access token for the specified user.

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

        Operation ID: adminCreateUserAccessToken
        """
        _payload = CreateAccessTokenOption(
            name=name,
            repositories=repositories,
            scopes=scopes,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("POST", f"/admin/users/{username}/tokens", json=_payload)
        return decode(_response, AccessToken)

    def delete(self, username: str, token: str) -> None:
        """
        Delete an access token for the specified user.

        Args:
            username: username of user
            token: token to be deleted, identified by ID and if not available by name

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIError is error format response.

        Operation ID: adminDeleteUserAccessToken
        """
        _response = self._client._request("DELETE", f"/admin/users/{username}/tokens/{token}")
        return decode(_response, None)


class AsyncAdminUsersTokens:
    """The ``admin.users.tokens`` namespace."""

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

        Operation ID: adminListUserAccessTokens
        """
        return await self._client._paginate(
            "GET", f"/admin/users/{username}/tokens", model=AccessToken, page=page, limit=limit
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
        Create an access token for the specified user.

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

        Operation ID: adminCreateUserAccessToken
        """
        _payload = CreateAccessTokenOption(
            name=name,
            repositories=repositories,
            scopes=scopes,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request("POST", f"/admin/users/{username}/tokens", json=_payload)
        return decode(_response, AccessToken)

    async def delete(self, username: str, token: str) -> None:
        """
        Delete an access token for the specified user.

        Args:
            username: username of user
            token: token to be deleted, identified by ID and if not available by name

        Returns:
            No content.

        Raises:
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIError is error format response.

        Operation ID: adminDeleteUserAccessToken
        """
        _response = await self._client._request("DELETE", f"/admin/users/{username}/tokens/{token}")
        return decode(_response, None)
