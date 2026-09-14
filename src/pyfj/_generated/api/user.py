"""Generated resource namespaces for the ``user`` group. Do not edit by hand.

Regenerate with ``python -m codegen``; see docs/development/codegen.md.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from pyfj._generated.models.action_run_job import ActionRunJob
from pyfj._generated.models.action_runner import ActionRunner
from pyfj._generated.models.action_variable import ActionVariable
from pyfj._generated.models.ap_remote_follow_option import APRemoteFollowOption
from pyfj._generated.models.blocked_user import BlockedUser
from pyfj._generated.models.create_email_option import CreateEmailOption
from pyfj._generated.models.create_gpg_key_option import CreateGPGKeyOption
from pyfj._generated.models.create_hook_option import CreateHookOption
from pyfj._generated.models.create_key_option import CreateKeyOption
from pyfj._generated.models.create_o_auth2_application_options import CreateOAuth2ApplicationOptions
from pyfj._generated.models.create_or_update_secret_option import CreateOrUpdateSecretOption
from pyfj._generated.models.create_repo_option import CreateRepoOption
from pyfj._generated.models.create_variable_option import CreateVariableOption
from pyfj._generated.models.delete_email_option import DeleteEmailOption
from pyfj._generated.models.edit_hook_option import EditHookOption
from pyfj._generated.models.email import Email
from pyfj._generated.models.gpg_key import GPGKey
from pyfj._generated.models.hook import Hook
from pyfj._generated.models.o_auth2_application import OAuth2Application
from pyfj._generated.models.organization import Organization
from pyfj._generated.models.public_key import PublicKey
from pyfj._generated.models.quota_info import QuotaInfo
from pyfj._generated.models.quota_used_artifact import QuotaUsedArtifact
from pyfj._generated.models.quota_used_attachment import QuotaUsedAttachment
from pyfj._generated.models.quota_used_package import QuotaUsedPackage
from pyfj._generated.models.register_runner_options import RegisterRunnerOptions
from pyfj._generated.models.register_runner_response import RegisterRunnerResponse
from pyfj._generated.models.registration_token import RegistrationToken
from pyfj._generated.models.repository import Repository
from pyfj._generated.models.stop_watch import StopWatch
from pyfj._generated.models.team import Team
from pyfj._generated.models.tracked_time import TrackedTime
from pyfj._generated.models.update_user_avatar_option import UpdateUserAvatarOption
from pyfj._generated.models.update_variable_option import UpdateVariableOption
from pyfj._generated.models.user import User as UserModel
from pyfj._generated.models.user_settings import UserSettings as UserSettingsModel
from pyfj._generated.models.user_settings_options import UserSettingsOptions
from pyfj._generated.models.verify_gpg_key_option import VerifyGPGKeyOption
from pyfj._runtime import decode

if TYPE_CHECKING:
    import builtins
    from datetime import datetime
    from typing import Literal

    from pyfj._generated.models.create_hook_option import CreateHookOptionType
    from pyfj._generated.models.create_hook_option_config import CreateHookOptionConfig
    from pyfj._generated.models.create_repo_option import CreateRepoOptionObjectFormatName, CreateRepoOptionTrustModel
    from pyfj._runtime import AsyncForgejo as _RuntimeAsyncForgejo
    from pyfj._runtime import AsyncPaginated, Paginated
    from pyfj._runtime import Forgejo as _RuntimeForgejo


class User:
    """The ``user`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client
        self.actions: UserActions = UserActions(client)
        self.activitypub: UserActivitypub = UserActivitypub(client)
        self.applications: UserApplications = UserApplications(client)
        self.avatar: UserAvatar = UserAvatar(client)
        self.emails: UserEmails = UserEmails(client)
        self.following: UserFollowing = UserFollowing(client)
        self.gpg_keys: UserGpgKeys = UserGpgKeys(client)
        self.hooks: UserHooks = UserHooks(client)
        self.keys: UserKeys = UserKeys(client)
        self.quota: UserQuota = UserQuota(client)
        self.repos: UserRepos = UserRepos(client)
        self.settings: UserSettings = UserSettings(client)
        self.starred: UserStarred = UserStarred(client)

    def get(self) -> UserModel:
        """
        Get the authenticated user.

        Returns:
            User.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: userGetCurrent
        """
        _response = self._client._request("GET", "/user")
        return decode(_response, UserModel)

    def block(self, username: str) -> None:
        """
        Blocks a user from the doer.

        Args:
            username: username of the user

        Returns:
            No content.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: userBlockUser
        """
        _response = self._client._request("PUT", f"/user/block/{username}")
        return decode(_response, None)

    def followers(self, *, page: int | None = None, limit: int | None = None) -> Paginated[UserModel]:
        """
        List the authenticated user's followers.

        Args:
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            UserList.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: userCurrentListFollowers
        """
        return self._client._paginate("GET", "/user/followers", model=UserModel, page=page, limit=limit)

    def gpg_key_token(self) -> str:
        """
        Get a Token to verify.

        Returns:
            APIString is a string response.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: getVerificationToken
        """
        _response = self._client._request("GET", "/user/gpg_key_token")
        return decode(_response, str)

    def gpg_key_verify(self, *, armored_signature: str | None = None, key_id: str) -> GPGKey:
        """
        Verify a GPG key.

        Args:
            armored_signature:
            key_id: An Signature for a GPG key token

        Returns:
            GPGKey.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: userVerifyGPGKey
        """
        _payload = VerifyGPGKeyOption(
            armored_signature=armored_signature,
            key_id=key_id,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("POST", "/user/gpg_key_verify", json=_payload)
        return decode(_response, GPGKey)

    def list_blocked(self, *, page: int | None = None, limit: int | None = None) -> Paginated[BlockedUser]:
        """
        List the authenticated user's blocked users.

        Args:
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            BlockedUserList.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: userListBlockedUsers
        """
        return self._client._paginate("GET", "/user/list_blocked", model=BlockedUser, page=page, limit=limit)

    def orgs(self, *, page: int | None = None, limit: int | None = None) -> Paginated[Organization]:
        """
        List the current user's organizations.

        Args:
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            OrganizationListWithoutPagination - Organizations without pagination headers.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgListCurrentUserOrgs
        """
        return self._client._paginate("GET", "/user/orgs", model=Organization, page=page, limit=limit)

    def stopwatches(self, *, page: int | None = None, limit: int | None = None) -> Paginated[StopWatch]:
        """
        Get list of all existing stopwatches.

        Args:
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            StopWatchList.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: userGetStopWatches
        """
        return self._client._paginate("GET", "/user/stopwatches", model=StopWatch, page=page, limit=limit)

    def subscriptions(self, *, page: int | None = None, limit: int | None = None) -> Paginated[Repository]:
        """
        List repositories watched by the authenticated user.

        Args:
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            RepositoryList.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: userCurrentListSubscriptions
        """
        return self._client._paginate("GET", "/user/subscriptions", model=Repository, page=page, limit=limit)

    def teams(self, *, page: int | None = None, limit: int | None = None) -> Paginated[Team]:
        """
        List all the teams a user belongs to.

        Args:
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            TeamList.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: userListTeams
        """
        return self._client._paginate("GET", "/user/teams", model=Team, page=page, limit=limit)

    def times(
        self,
        *,
        since: datetime | None = None,
        before: datetime | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> Paginated[TrackedTime]:
        """
        List the current user's tracked times.

        Args:
            since: Only show times updated after the given time. This is a timestamp in RFC 3339 format
            before: Only show times updated before the given time. This is a timestamp in RFC 3339 format
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            TrackedTimeList.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: userCurrentTrackedTimes
        """
        _query: dict[str, object] = {
            "since": None if since is None else since.isoformat(),
            "before": None if before is None else before.isoformat(),
        }

        return self._client._paginate("GET", "/user/times", model=TrackedTime, params=_query, page=page, limit=limit)

    def unblock(self, username: str) -> None:
        """
        Unblocks a user from the doer.

        Args:
            username: username of the user

        Returns:
            No content.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: userUnblockUser
        """
        _response = self._client._request("PUT", f"/user/unblock/{username}")
        return decode(_response, None)


class AsyncUser:
    """The ``user`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client
        self.actions: AsyncUserActions = AsyncUserActions(client)
        self.activitypub: AsyncUserActivitypub = AsyncUserActivitypub(client)
        self.applications: AsyncUserApplications = AsyncUserApplications(client)
        self.avatar: AsyncUserAvatar = AsyncUserAvatar(client)
        self.emails: AsyncUserEmails = AsyncUserEmails(client)
        self.following: AsyncUserFollowing = AsyncUserFollowing(client)
        self.gpg_keys: AsyncUserGpgKeys = AsyncUserGpgKeys(client)
        self.hooks: AsyncUserHooks = AsyncUserHooks(client)
        self.keys: AsyncUserKeys = AsyncUserKeys(client)
        self.quota: AsyncUserQuota = AsyncUserQuota(client)
        self.repos: AsyncUserRepos = AsyncUserRepos(client)
        self.settings: AsyncUserSettings = AsyncUserSettings(client)
        self.starred: AsyncUserStarred = AsyncUserStarred(client)

    async def get(self) -> UserModel:
        """
        Get the authenticated user.

        Returns:
            User.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: userGetCurrent
        """
        _response = await self._client._request("GET", "/user")
        return decode(_response, UserModel)

    async def block(self, username: str) -> None:
        """
        Blocks a user from the doer.

        Args:
            username: username of the user

        Returns:
            No content.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: userBlockUser
        """
        _response = await self._client._request("PUT", f"/user/block/{username}")
        return decode(_response, None)

    async def followers(self, *, page: int | None = None, limit: int | None = None) -> AsyncPaginated[UserModel]:
        """
        List the authenticated user's followers.

        Args:
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            UserList.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: userCurrentListFollowers
        """
        return await self._client._paginate("GET", "/user/followers", model=UserModel, page=page, limit=limit)

    async def gpg_key_token(self) -> str:
        """
        Get a Token to verify.

        Returns:
            APIString is a string response.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: getVerificationToken
        """
        _response = await self._client._request("GET", "/user/gpg_key_token")
        return decode(_response, str)

    async def gpg_key_verify(self, *, armored_signature: str | None = None, key_id: str) -> GPGKey:
        """
        Verify a GPG key.

        Args:
            armored_signature:
            key_id: An Signature for a GPG key token

        Returns:
            GPGKey.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: userVerifyGPGKey
        """
        _payload = VerifyGPGKeyOption(
            armored_signature=armored_signature,
            key_id=key_id,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request("POST", "/user/gpg_key_verify", json=_payload)
        return decode(_response, GPGKey)

    async def list_blocked(self, *, page: int | None = None, limit: int | None = None) -> AsyncPaginated[BlockedUser]:
        """
        List the authenticated user's blocked users.

        Args:
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            BlockedUserList.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: userListBlockedUsers
        """
        return await self._client._paginate("GET", "/user/list_blocked", model=BlockedUser, page=page, limit=limit)

    async def orgs(self, *, page: int | None = None, limit: int | None = None) -> AsyncPaginated[Organization]:
        """
        List the current user's organizations.

        Args:
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            OrganizationListWithoutPagination - Organizations without pagination headers.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: orgListCurrentUserOrgs
        """
        return await self._client._paginate("GET", "/user/orgs", model=Organization, page=page, limit=limit)

    async def stopwatches(self, *, page: int | None = None, limit: int | None = None) -> AsyncPaginated[StopWatch]:
        """
        Get list of all existing stopwatches.

        Args:
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            StopWatchList.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: userGetStopWatches
        """
        return await self._client._paginate("GET", "/user/stopwatches", model=StopWatch, page=page, limit=limit)

    async def subscriptions(self, *, page: int | None = None, limit: int | None = None) -> AsyncPaginated[Repository]:
        """
        List repositories watched by the authenticated user.

        Args:
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            RepositoryList.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: userCurrentListSubscriptions
        """
        return await self._client._paginate("GET", "/user/subscriptions", model=Repository, page=page, limit=limit)

    async def teams(self, *, page: int | None = None, limit: int | None = None) -> AsyncPaginated[Team]:
        """
        List all the teams a user belongs to.

        Args:
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            TeamList.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: userListTeams
        """
        return await self._client._paginate("GET", "/user/teams", model=Team, page=page, limit=limit)

    async def times(
        self,
        *,
        since: datetime | None = None,
        before: datetime | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> AsyncPaginated[TrackedTime]:
        """
        List the current user's tracked times.

        Args:
            since: Only show times updated after the given time. This is a timestamp in RFC 3339 format
            before: Only show times updated before the given time. This is a timestamp in RFC 3339 format
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            TrackedTimeList.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: userCurrentTrackedTimes
        """
        _query: dict[str, object] = {
            "since": None if since is None else since.isoformat(),
            "before": None if before is None else before.isoformat(),
        }

        return await self._client._paginate(
            "GET", "/user/times", model=TrackedTime, params=_query, page=page, limit=limit
        )

    async def unblock(self, username: str) -> None:
        """
        Unblocks a user from the doer.

        Args:
            username: username of the user

        Returns:
            No content.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: userUnblockUser
        """
        _response = await self._client._request("PUT", f"/user/unblock/{username}")
        return decode(_response, None)


class UserActions:
    """The ``user.actions`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client
        self.runners: UserActionsRunners = UserActionsRunners(client)
        self.secrets: UserActionsSecrets = UserActionsSecrets(client)
        self.variables: UserActionsVariables = UserActionsVariables(client)


class AsyncUserActions:
    """The ``user.actions`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client
        self.runners: AsyncUserActionsRunners = AsyncUserActionsRunners(client)
        self.secrets: AsyncUserActionsSecrets = AsyncUserActionsSecrets(client)
        self.variables: AsyncUserActionsVariables = AsyncUserActionsVariables(client)


class UserActionsRunners:
    """The ``user.actions.runners`` namespace."""

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
        Get the user's runners.

        Args:
            visible: whether to include all visible runners (true) or only those that are directly owned by the user
                (false)
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            ActionRunnerList is a list of Forgejo Action runners.

        Raises:
            BadRequestError: 400. APIError is error format response.
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: getUserRunners
        """
        _query: dict[str, object] = {"visible": visible}

        return self._client._paginate(
            "GET", "/user/actions/runners", model=ActionRunner, params=_query, page=page, limit=limit
        )

    def register(
        self,
        *,
        description: str | None = None,
        ephemeral: bool | None = None,
        name: str,
    ) -> RegisterRunnerResponse:
        """
        Register a new user-level runner.

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

        Operation ID: registerUserRunner
        """
        _payload = RegisterRunnerOptions(
            description=description,
            ephemeral=ephemeral,
            name=name,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("POST", "/user/actions/runners", json=_payload)
        return decode(_response, RegisterRunnerResponse)

    def jobs(self, *, labels: str | None = None) -> builtins.list[ActionRunJob]:
        """
        Search for user's action jobs according filter conditions.

        Args:
            labels: a comma separated list of run job labels to search for

        Returns:
            RunJobList is a list of action run jobs.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: userSearchRunJobs
        """
        _query: dict[str, object] = {"labels": labels}

        _response = self._client._request("GET", "/user/actions/runners/jobs", params=_query)
        return decode(_response, list[ActionRunJob])

    def registration_token(self) -> RegistrationToken:
        """
        Get the user's runner registration token.

        This operation has been deprecated in Forgejo 15. Use the web UI or
        [`/user/actions/runners`](#/user/registerUserRunner) instead.

        Returns:
            RegistrationToken is a string used to register a runner with a server.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Deprecated:
            Deprecated in the vendored Spec; generated for compatibility.

        Operation ID: userGetRunnerRegistrationToken
        """
        _response = self._client._request("GET", "/user/actions/runners/registration-token")
        return decode(_response, RegistrationToken)

    def get(self, runner_id: str) -> ActionRunner:
        """
        Get a particular runner that belongs to the user.

        Args:
            runner_id: ID of the runner

        Returns:
            ActionRunner represents a runner.

        Raises:
            BadRequestError: 400. APIError is error format response.
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: getUserRunner
        """
        _response = self._client._request("GET", f"/user/actions/runners/{runner_id}")
        return decode(_response, ActionRunner)

    def delete(self, runner_id: str) -> None:
        """
        Delete a particular user-level runner.

        Args:
            runner_id: ID of the runner

        Returns:
            No content.

        Raises:
            BadRequestError: 400. APIError is error format response.
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: deleteUserRunner
        """
        _response = self._client._request("DELETE", f"/user/actions/runners/{runner_id}")
        return decode(_response, None)


class AsyncUserActionsRunners:
    """The ``user.actions.runners`` namespace."""

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
        Get the user's runners.

        Args:
            visible: whether to include all visible runners (true) or only those that are directly owned by the user
                (false)
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            ActionRunnerList is a list of Forgejo Action runners.

        Raises:
            BadRequestError: 400. APIError is error format response.
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: getUserRunners
        """
        _query: dict[str, object] = {"visible": visible}

        return await self._client._paginate(
            "GET", "/user/actions/runners", model=ActionRunner, params=_query, page=page, limit=limit
        )

    async def register(
        self,
        *,
        description: str | None = None,
        ephemeral: bool | None = None,
        name: str,
    ) -> RegisterRunnerResponse:
        """
        Register a new user-level runner.

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

        Operation ID: registerUserRunner
        """
        _payload = RegisterRunnerOptions(
            description=description,
            ephemeral=ephemeral,
            name=name,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request("POST", "/user/actions/runners", json=_payload)
        return decode(_response, RegisterRunnerResponse)

    async def jobs(self, *, labels: str | None = None) -> builtins.list[ActionRunJob]:
        """
        Search for user's action jobs according filter conditions.

        Args:
            labels: a comma separated list of run job labels to search for

        Returns:
            RunJobList is a list of action run jobs.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: userSearchRunJobs
        """
        _query: dict[str, object] = {"labels": labels}

        _response = await self._client._request("GET", "/user/actions/runners/jobs", params=_query)
        return decode(_response, list[ActionRunJob])

    async def registration_token(self) -> RegistrationToken:
        """
        Get the user's runner registration token.

        This operation has been deprecated in Forgejo 15. Use the web UI or
        [`/user/actions/runners`](#/user/registerUserRunner) instead.

        Returns:
            RegistrationToken is a string used to register a runner with a server.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Deprecated:
            Deprecated in the vendored Spec; generated for compatibility.

        Operation ID: userGetRunnerRegistrationToken
        """
        _response = await self._client._request("GET", "/user/actions/runners/registration-token")
        return decode(_response, RegistrationToken)

    async def get(self, runner_id: str) -> ActionRunner:
        """
        Get a particular runner that belongs to the user.

        Args:
            runner_id: ID of the runner

        Returns:
            ActionRunner represents a runner.

        Raises:
            BadRequestError: 400. APIError is error format response.
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: getUserRunner
        """
        _response = await self._client._request("GET", f"/user/actions/runners/{runner_id}")
        return decode(_response, ActionRunner)

    async def delete(self, runner_id: str) -> None:
        """
        Delete a particular user-level runner.

        Args:
            runner_id: ID of the runner

        Returns:
            No content.

        Raises:
            BadRequestError: 400. APIError is error format response.
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: deleteUserRunner
        """
        _response = await self._client._request("DELETE", f"/user/actions/runners/{runner_id}")
        return decode(_response, None)


class UserActionsSecrets:
    """The ``user.actions.secrets`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def update(self, secretname: str, *, data: str) -> None:
        """
        Create or Update a secret value in a user scope.

        Args:
            secretname: name of the secret
            data: Data of the secret. Special characters will be retained. Line endings will be normalized to LF to
                match the behaviour of browsers. Encode the data with Base64 if line endings should be retained.

        Returns:
            No content.

        Raises:
            BadRequestError: 400. APIError is error format response.
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: updateUserSecret
        """
        _payload = CreateOrUpdateSecretOption(
            data=data,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("PUT", f"/user/actions/secrets/{secretname}", json=_payload)
        return decode(_response, None)

    def delete(self, secretname: str) -> None:
        """
        Delete a secret in a user scope.

        Args:
            secretname: name of the secret

        Returns:
            No content.

        Raises:
            BadRequestError: 400. APIError is error format response.
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: deleteUserSecret
        """
        _response = self._client._request("DELETE", f"/user/actions/secrets/{secretname}")
        return decode(_response, None)


class AsyncUserActionsSecrets:
    """The ``user.actions.secrets`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def update(self, secretname: str, *, data: str) -> None:
        """
        Create or Update a secret value in a user scope.

        Args:
            secretname: name of the secret
            data: Data of the secret. Special characters will be retained. Line endings will be normalized to LF to
                match the behaviour of browsers. Encode the data with Base64 if line endings should be retained.

        Returns:
            No content.

        Raises:
            BadRequestError: 400. APIError is error format response.
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: updateUserSecret
        """
        _payload = CreateOrUpdateSecretOption(
            data=data,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request("PUT", f"/user/actions/secrets/{secretname}", json=_payload)
        return decode(_response, None)

    async def delete(self, secretname: str) -> None:
        """
        Delete a secret in a user scope.

        Args:
            secretname: name of the secret

        Returns:
            No content.

        Raises:
            BadRequestError: 400. APIError is error format response.
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: deleteUserSecret
        """
        _response = await self._client._request("DELETE", f"/user/actions/secrets/{secretname}")
        return decode(_response, None)


class UserActionsVariables:
    """The ``user.actions.variables`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(self, *, page: int | None = None, limit: int | None = None) -> Paginated[ActionVariable]:
        """
        Get the user-level list of variables which is created by current doer.

        Args:
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            VariableList.

        Raises:
            BadRequestError: 400. APIError is error format response.
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: getUserVariablesList
        """
        return self._client._paginate("GET", "/user/actions/variables", model=ActionVariable, page=page, limit=limit)

    def get(self, variablename: str) -> ActionVariable:
        """
        Get a user-level variable which is created by current doer.

        Args:
            variablename: name of the variable

        Returns:
            ActionVariable.

        Raises:
            BadRequestError: 400. APIError is error format response.
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: getUserVariable
        """
        _response = self._client._request("GET", f"/user/actions/variables/{variablename}")
        return decode(_response, ActionVariable)

    def create(self, variablename: str, *, value: str) -> None:
        """
        Create a user-level variable.

        Args:
            variablename: name of the variable
            value: Value of the variable to create. Special characters will be retained. Line endings will be normalized
                to LF to match the behaviour of browsers. Encode the data with Base64 if line endings should be
                retained.

        Returns:
            No content.

        Raises:
            BadRequestError: 400. APIError is error format response.
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: createUserVariable
        """
        _payload = CreateVariableOption(
            value=value,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("POST", f"/user/actions/variables/{variablename}", json=_payload)
        return decode(_response, None)

    def update(self, variablename: str, *, name: str | None = None, value: str) -> None:
        """
        Update a user-level variable which is created by current doer.

        Args:
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
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: updateUserVariable
        """
        _payload = UpdateVariableOption(
            name=name,
            value=value,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("PUT", f"/user/actions/variables/{variablename}", json=_payload)
        return decode(_response, None)

    def delete(self, variablename: str) -> None:
        """
        Delete a user-level variable which is created by current doer.

        Args:
            variablename: name of the variable

        Returns:
            No content.

        Raises:
            BadRequestError: 400. APIError is error format response.
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: deleteUserVariable
        """
        _response = self._client._request("DELETE", f"/user/actions/variables/{variablename}")
        return decode(_response, None)


class AsyncUserActionsVariables:
    """The ``user.actions.variables`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(self, *, page: int | None = None, limit: int | None = None) -> AsyncPaginated[ActionVariable]:
        """
        Get the user-level list of variables which is created by current doer.

        Args:
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            VariableList.

        Raises:
            BadRequestError: 400. APIError is error format response.
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: getUserVariablesList
        """
        return await self._client._paginate(
            "GET", "/user/actions/variables", model=ActionVariable, page=page, limit=limit
        )

    async def get(self, variablename: str) -> ActionVariable:
        """
        Get a user-level variable which is created by current doer.

        Args:
            variablename: name of the variable

        Returns:
            ActionVariable.

        Raises:
            BadRequestError: 400. APIError is error format response.
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: getUserVariable
        """
        _response = await self._client._request("GET", f"/user/actions/variables/{variablename}")
        return decode(_response, ActionVariable)

    async def create(self, variablename: str, *, value: str) -> None:
        """
        Create a user-level variable.

        Args:
            variablename: name of the variable
            value: Value of the variable to create. Special characters will be retained. Line endings will be normalized
                to LF to match the behaviour of browsers. Encode the data with Base64 if line endings should be
                retained.

        Returns:
            No content.

        Raises:
            BadRequestError: 400. APIError is error format response.
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: createUserVariable
        """
        _payload = CreateVariableOption(
            value=value,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request("POST", f"/user/actions/variables/{variablename}", json=_payload)
        return decode(_response, None)

    async def update(self, variablename: str, *, name: str | None = None, value: str) -> None:
        """
        Update a user-level variable which is created by current doer.

        Args:
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
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: updateUserVariable
        """
        _payload = UpdateVariableOption(
            name=name,
            value=value,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request("PUT", f"/user/actions/variables/{variablename}", json=_payload)
        return decode(_response, None)

    async def delete(self, variablename: str) -> None:
        """
        Delete a user-level variable which is created by current doer.

        Args:
            variablename: name of the variable

        Returns:
            No content.

        Raises:
            BadRequestError: 400. APIError is error format response.
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: deleteUserVariable
        """
        _response = await self._client._request("DELETE", f"/user/actions/variables/{variablename}")
        return decode(_response, None)


class UserActivitypub:
    """The ``user.activitypub`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def follow(self, *, target: str | None = None) -> None:
        """
        Follow a remote activitypub account.

        Args:
            target:

        Returns:
            No content.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: userCurrentActivityPubFollow
        """
        if target is not None:
            _payload = APRemoteFollowOption(target=target).model_dump(mode="json", by_alias=True, exclude_none=True)
        else:
            _payload = None

        _response = self._client._request("POST", "/user/activitypub/follow", json=_payload)
        return decode(_response, None)


class AsyncUserActivitypub:
    """The ``user.activitypub`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def follow(self, *, target: str | None = None) -> None:
        """
        Follow a remote activitypub account.

        Args:
            target:

        Returns:
            No content.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: userCurrentActivityPubFollow
        """
        if target is not None:
            _payload = APRemoteFollowOption(target=target).model_dump(mode="json", by_alias=True, exclude_none=True)
        else:
            _payload = None

        _response = await self._client._request("POST", "/user/activitypub/follow", json=_payload)
        return decode(_response, None)


class UserApplications:
    """The ``user.applications`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client
        self.oauth2: UserApplicationsOauth2 = UserApplicationsOauth2(client)


class AsyncUserApplications:
    """The ``user.applications`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client
        self.oauth2: AsyncUserApplicationsOauth2 = AsyncUserApplicationsOauth2(client)


class UserApplicationsOauth2:
    """The ``user.applications.oauth2`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(self, *, page: int | None = None, limit: int | None = None) -> Paginated[OAuth2Application]:
        """
        List the authenticated user's oauth2 applications.

        Args:
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            OAuth2ApplicationList.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: userGetOAuth2Applications
        """
        return self._client._paginate(
            "GET", "/user/applications/oauth2", model=OAuth2Application, page=page, limit=limit
        )

    def create(
        self,
        *,
        confidential_client: bool | None = None,
        name: str | None = None,
        redirect_uris: builtins.list[str] | None = None,
    ) -> OAuth2Application:
        """
        Creates a new OAuth2 application.

        Args:
            confidential_client:
            name:
            redirect_uris:

        Returns:
            OAuth2Application.

        Raises:
            BadRequestError: 400. APIError is error format response.
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: userCreateOAuth2Application
        """
        _payload = CreateOAuth2ApplicationOptions(
            confidential_client=confidential_client,
            name=name,
            redirect_uris=redirect_uris,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("POST", "/user/applications/oauth2", json=_payload)
        return decode(_response, OAuth2Application)

    def get(self, id: int) -> OAuth2Application:
        """
        Get an OAuth2 application.

        Args:
            id: Application ID to be found

        Returns:
            OAuth2Application.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: userGetOAuth2Application
        """
        _response = self._client._request("GET", f"/user/applications/oauth2/{id}")
        return decode(_response, OAuth2Application)

    def update(
        self,
        id: int,
        *,
        confidential_client: bool | None = None,
        name: str | None = None,
        redirect_uris: builtins.list[str] | None = None,
    ) -> OAuth2Application:
        """
        Update an OAuth2 application, this includes regenerating the client secret.

        Args:
            id: application to be updated
            confidential_client:
            name:
            redirect_uris:

        Returns:
            OAuth2Application.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: userUpdateOAuth2Application
        """
        _payload = CreateOAuth2ApplicationOptions(
            confidential_client=confidential_client,
            name=name,
            redirect_uris=redirect_uris,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("PATCH", f"/user/applications/oauth2/{id}", json=_payload)
        return decode(_response, OAuth2Application)

    def delete(self, id: int) -> None:
        """
        Delete an OAuth2 application.

        Args:
            id: token to be deleted

        Returns:
            No content.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: userDeleteOAuth2Application
        """
        _response = self._client._request("DELETE", f"/user/applications/oauth2/{id}")
        return decode(_response, None)


class AsyncUserApplicationsOauth2:
    """The ``user.applications.oauth2`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(self, *, page: int | None = None, limit: int | None = None) -> AsyncPaginated[OAuth2Application]:
        """
        List the authenticated user's oauth2 applications.

        Args:
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            OAuth2ApplicationList.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: userGetOAuth2Applications
        """
        return await self._client._paginate(
            "GET", "/user/applications/oauth2", model=OAuth2Application, page=page, limit=limit
        )

    async def create(
        self,
        *,
        confidential_client: bool | None = None,
        name: str | None = None,
        redirect_uris: builtins.list[str] | None = None,
    ) -> OAuth2Application:
        """
        Creates a new OAuth2 application.

        Args:
            confidential_client:
            name:
            redirect_uris:

        Returns:
            OAuth2Application.

        Raises:
            BadRequestError: 400. APIError is error format response.
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: userCreateOAuth2Application
        """
        _payload = CreateOAuth2ApplicationOptions(
            confidential_client=confidential_client,
            name=name,
            redirect_uris=redirect_uris,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request("POST", "/user/applications/oauth2", json=_payload)
        return decode(_response, OAuth2Application)

    async def get(self, id: int) -> OAuth2Application:
        """
        Get an OAuth2 application.

        Args:
            id: Application ID to be found

        Returns:
            OAuth2Application.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: userGetOAuth2Application
        """
        _response = await self._client._request("GET", f"/user/applications/oauth2/{id}")
        return decode(_response, OAuth2Application)

    async def update(
        self,
        id: int,
        *,
        confidential_client: bool | None = None,
        name: str | None = None,
        redirect_uris: builtins.list[str] | None = None,
    ) -> OAuth2Application:
        """
        Update an OAuth2 application, this includes regenerating the client secret.

        Args:
            id: application to be updated
            confidential_client:
            name:
            redirect_uris:

        Returns:
            OAuth2Application.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: userUpdateOAuth2Application
        """
        _payload = CreateOAuth2ApplicationOptions(
            confidential_client=confidential_client,
            name=name,
            redirect_uris=redirect_uris,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request("PATCH", f"/user/applications/oauth2/{id}", json=_payload)
        return decode(_response, OAuth2Application)

    async def delete(self, id: int) -> None:
        """
        Delete an OAuth2 application.

        Args:
            id: token to be deleted

        Returns:
            No content.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: userDeleteOAuth2Application
        """
        _response = await self._client._request("DELETE", f"/user/applications/oauth2/{id}")
        return decode(_response, None)


class UserAvatar:
    """The ``user.avatar`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def update(self, *, image: str | None = None) -> None:
        """
        Update avatar of the current user.

        Args:
            image: image must be base64 encoded

        Returns:
            No content.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: userUpdateAvatar
        """
        if image is not None:
            _payload = UpdateUserAvatarOption(image=image).model_dump(mode="json", by_alias=True, exclude_none=True)
        else:
            _payload = None

        _response = self._client._request("POST", "/user/avatar", json=_payload)
        return decode(_response, None)

    def delete(self) -> None:
        """
        Delete avatar of the current user. It will be replaced by a default one.

        Returns:
            No content.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: userDeleteAvatar
        """
        _response = self._client._request("DELETE", "/user/avatar")
        return decode(_response, None)


class AsyncUserAvatar:
    """The ``user.avatar`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def update(self, *, image: str | None = None) -> None:
        """
        Update avatar of the current user.

        Args:
            image: image must be base64 encoded

        Returns:
            No content.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: userUpdateAvatar
        """
        if image is not None:
            _payload = UpdateUserAvatarOption(image=image).model_dump(mode="json", by_alias=True, exclude_none=True)
        else:
            _payload = None

        _response = await self._client._request("POST", "/user/avatar", json=_payload)
        return decode(_response, None)

    async def delete(self) -> None:
        """
        Delete avatar of the current user. It will be replaced by a default one.

        Returns:
            No content.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: userDeleteAvatar
        """
        _response = await self._client._request("DELETE", "/user/avatar")
        return decode(_response, None)


class UserEmails:
    """The ``user.emails`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(self) -> builtins.list[Email]:
        """
        List all email addresses of the current user.

        Returns:
            EmailList.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: userListEmails
        """
        _response = self._client._request("GET", "/user/emails")
        return decode(_response, list[Email])

    def add(self, *, emails: builtins.list[str] | None = None) -> builtins.list[Email]:
        """
        Add an email addresses to the current user's account.

        Args:
            emails: email addresses to add

        Returns:
            EmailList.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: userAddEmail
        """
        if emails is not None:
            _payload = CreateEmailOption(emails=emails).model_dump(mode="json", by_alias=True, exclude_none=True)
        else:
            _payload = None

        _response = self._client._request("POST", "/user/emails", json=_payload)
        return decode(_response, list[Email])

    def delete(self, *, emails: builtins.list[str] | None = None) -> None:
        """
        Delete email addresses from the current user's account.

        Args:
            emails: email addresses to delete

        Returns:
            No content.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: userDeleteEmail
        """
        if emails is not None:
            _payload = DeleteEmailOption(emails=emails).model_dump(mode="json", by_alias=True, exclude_none=True)
        else:
            _payload = None

        _response = self._client._request("DELETE", "/user/emails", json=_payload)
        return decode(_response, None)


class AsyncUserEmails:
    """The ``user.emails`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(self) -> builtins.list[Email]:
        """
        List all email addresses of the current user.

        Returns:
            EmailList.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: userListEmails
        """
        _response = await self._client._request("GET", "/user/emails")
        return decode(_response, list[Email])

    async def add(self, *, emails: builtins.list[str] | None = None) -> builtins.list[Email]:
        """
        Add an email addresses to the current user's account.

        Args:
            emails: email addresses to add

        Returns:
            EmailList.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: userAddEmail
        """
        if emails is not None:
            _payload = CreateEmailOption(emails=emails).model_dump(mode="json", by_alias=True, exclude_none=True)
        else:
            _payload = None

        _response = await self._client._request("POST", "/user/emails", json=_payload)
        return decode(_response, list[Email])

    async def delete(self, *, emails: builtins.list[str] | None = None) -> None:
        """
        Delete email addresses from the current user's account.

        Args:
            emails: email addresses to delete

        Returns:
            No content.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: userDeleteEmail
        """
        if emails is not None:
            _payload = DeleteEmailOption(emails=emails).model_dump(mode="json", by_alias=True, exclude_none=True)
        else:
            _payload = None

        _response = await self._client._request("DELETE", "/user/emails", json=_payload)
        return decode(_response, None)


class UserFollowing:
    """The ``user.following`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(self, *, page: int | None = None, limit: int | None = None) -> Paginated[UserModel]:
        """
        List the users that the authenticated user is following.

        Args:
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            UserList.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: userCurrentListFollowing
        """
        return self._client._paginate("GET", "/user/following", model=UserModel, page=page, limit=limit)

    def get(self, username: str) -> None:
        """
        Check whether a user is followed by the authenticated user.

        Args:
            username: username of followed user

        Returns:
            No content.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: userCurrentCheckFollowing
        """
        _response = self._client._request("GET", f"/user/following/{username}")
        return decode(_response, None)

    def add(self, username: str) -> None:
        """
        Follow a user.

        Args:
            username: username of user to follow

        Returns:
            No content.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: userCurrentPutFollow
        """
        _response = self._client._request("PUT", f"/user/following/{username}")
        return decode(_response, None)

    def remove(self, username: str) -> None:
        """
        Unfollow a user.

        Args:
            username: username of user to unfollow

        Returns:
            No content.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: userCurrentDeleteFollow
        """
        _response = self._client._request("DELETE", f"/user/following/{username}")
        return decode(_response, None)


class AsyncUserFollowing:
    """The ``user.following`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(self, *, page: int | None = None, limit: int | None = None) -> AsyncPaginated[UserModel]:
        """
        List the users that the authenticated user is following.

        Args:
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            UserList.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: userCurrentListFollowing
        """
        return await self._client._paginate("GET", "/user/following", model=UserModel, page=page, limit=limit)

    async def get(self, username: str) -> None:
        """
        Check whether a user is followed by the authenticated user.

        Args:
            username: username of followed user

        Returns:
            No content.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: userCurrentCheckFollowing
        """
        _response = await self._client._request("GET", f"/user/following/{username}")
        return decode(_response, None)

    async def add(self, username: str) -> None:
        """
        Follow a user.

        Args:
            username: username of user to follow

        Returns:
            No content.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: userCurrentPutFollow
        """
        _response = await self._client._request("PUT", f"/user/following/{username}")
        return decode(_response, None)

    async def remove(self, username: str) -> None:
        """
        Unfollow a user.

        Args:
            username: username of user to unfollow

        Returns:
            No content.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: userCurrentDeleteFollow
        """
        _response = await self._client._request("DELETE", f"/user/following/{username}")
        return decode(_response, None)


class UserGpgKeys:
    """The ``user.gpg_keys`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(self, *, page: int | None = None, limit: int | None = None) -> Paginated[GPGKey]:
        """
        List the authenticated user's GPG keys.

        Args:
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            GPGKeyList.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: userCurrentListGPGKeys
        """
        return self._client._paginate("GET", "/user/gpg_keys", model=GPGKey, page=page, limit=limit)

    def create(self, *, armored_public_key: str, armored_signature: str | None = None) -> GPGKey:
        """
        Add a GPG public key to current user's account.

        Args:
            armored_public_key: An armored GPG key to add
            armored_signature:

        Returns:
            GPGKey.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: userCurrentPostGPGKey
        """
        _payload = CreateGPGKeyOption(
            armored_public_key=armored_public_key,
            armored_signature=armored_signature,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("POST", "/user/gpg_keys", json=_payload)
        return decode(_response, GPGKey)

    def get(self, id: int) -> GPGKey:
        """
        Get a GPG key.

        Args:
            id: id of key to get

        Returns:
            GPGKey.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: userCurrentGetGPGKey
        """
        _response = self._client._request("GET", f"/user/gpg_keys/{id}")
        return decode(_response, GPGKey)

    def delete(self, id: int) -> None:
        """
        Remove a GPG public key from current user's account.

        Args:
            id: id of key to delete

        Returns:
            No content.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: userCurrentDeleteGPGKey
        """
        _response = self._client._request("DELETE", f"/user/gpg_keys/{id}")
        return decode(_response, None)


class AsyncUserGpgKeys:
    """The ``user.gpg_keys`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(self, *, page: int | None = None, limit: int | None = None) -> AsyncPaginated[GPGKey]:
        """
        List the authenticated user's GPG keys.

        Args:
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            GPGKeyList.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: userCurrentListGPGKeys
        """
        return await self._client._paginate("GET", "/user/gpg_keys", model=GPGKey, page=page, limit=limit)

    async def create(self, *, armored_public_key: str, armored_signature: str | None = None) -> GPGKey:
        """
        Add a GPG public key to current user's account.

        Args:
            armored_public_key: An armored GPG key to add
            armored_signature:

        Returns:
            GPGKey.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: userCurrentPostGPGKey
        """
        _payload = CreateGPGKeyOption(
            armored_public_key=armored_public_key,
            armored_signature=armored_signature,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request("POST", "/user/gpg_keys", json=_payload)
        return decode(_response, GPGKey)

    async def get(self, id: int) -> GPGKey:
        """
        Get a GPG key.

        Args:
            id: id of key to get

        Returns:
            GPGKey.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: userCurrentGetGPGKey
        """
        _response = await self._client._request("GET", f"/user/gpg_keys/{id}")
        return decode(_response, GPGKey)

    async def delete(self, id: int) -> None:
        """
        Remove a GPG public key from current user's account.

        Args:
            id: id of key to delete

        Returns:
            No content.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: userCurrentDeleteGPGKey
        """
        _response = await self._client._request("DELETE", f"/user/gpg_keys/{id}")
        return decode(_response, None)


class UserHooks:
    """The ``user.hooks`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(self, *, page: int | None = None, limit: int | None = None) -> Paginated[Hook]:
        """
        List the authenticated user's webhooks.

        Args:
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            HookListWithoutPagination - Hooks without pagination headers.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: userListHooks
        """
        return self._client._paginate("GET", "/user/hooks", model=Hook, page=page, limit=limit)

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

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: userCreateHook
        """
        _payload = CreateHookOption(
            active=active,
            authorization_header=authorization_header,
            branch_filter=branch_filter,
            config=config,
            events=events,
            type=type,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("POST", "/user/hooks", json=_payload)
        return decode(_response, Hook)

    def get(self, id: int) -> Hook:
        """
        Get a hook.

        Args:
            id: id of the hook to get

        Returns:
            Hook.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: userGetHook
        """
        _response = self._client._request("GET", f"/user/hooks/{id}")
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

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: userEditHook
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

        _response = self._client._request("PATCH", f"/user/hooks/{id}", json=_payload)
        return decode(_response, Hook)

    def delete(self, id: int) -> None:
        """
        Delete a hook.

        Args:
            id: id of the hook to delete

        Returns:
            No content.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: userDeleteHook
        """
        _response = self._client._request("DELETE", f"/user/hooks/{id}")
        return decode(_response, None)


class AsyncUserHooks:
    """The ``user.hooks`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(self, *, page: int | None = None, limit: int | None = None) -> AsyncPaginated[Hook]:
        """
        List the authenticated user's webhooks.

        Args:
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            HookListWithoutPagination - Hooks without pagination headers.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: userListHooks
        """
        return await self._client._paginate("GET", "/user/hooks", model=Hook, page=page, limit=limit)

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

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: userCreateHook
        """
        _payload = CreateHookOption(
            active=active,
            authorization_header=authorization_header,
            branch_filter=branch_filter,
            config=config,
            events=events,
            type=type,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request("POST", "/user/hooks", json=_payload)
        return decode(_response, Hook)

    async def get(self, id: int) -> Hook:
        """
        Get a hook.

        Args:
            id: id of the hook to get

        Returns:
            Hook.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: userGetHook
        """
        _response = await self._client._request("GET", f"/user/hooks/{id}")
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

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: userEditHook
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

        _response = await self._client._request("PATCH", f"/user/hooks/{id}", json=_payload)
        return decode(_response, Hook)

    async def delete(self, id: int) -> None:
        """
        Delete a hook.

        Args:
            id: id of the hook to delete

        Returns:
            No content.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: userDeleteHook
        """
        _response = await self._client._request("DELETE", f"/user/hooks/{id}")
        return decode(_response, None)


class UserKeys:
    """The ``user.keys`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(
        self,
        *,
        fingerprint: str | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> Paginated[PublicKey]:
        """
        List the authenticated user's public keys.

        Args:
            fingerprint: fingerprint of the key
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            PublicKeyList.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: userCurrentListKeys
        """
        _query: dict[str, object] = {"fingerprint": fingerprint}

        return self._client._paginate("GET", "/user/keys", model=PublicKey, params=_query, page=page, limit=limit)

    def create(self, *, key: str, read_only: bool | None = None, title: str) -> PublicKey:
        """
        Create a public key.

        Args:
            key: An armored SSH key to add
            read_only: Describe if the key has only read access or read/write
            title: Title of the key to add

        Returns:
            PublicKey.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: userCurrentPostKey
        """
        _payload = CreateKeyOption(
            key=key,
            read_only=read_only,
            title=title,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = self._client._request("POST", "/user/keys", json=_payload)
        return decode(_response, PublicKey)

    def get(self, id: int) -> PublicKey:
        """
        Get a public key.

        Args:
            id: id of key to get

        Returns:
            PublicKey.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: userCurrentGetKey
        """
        _response = self._client._request("GET", f"/user/keys/{id}")
        return decode(_response, PublicKey)

    def delete(self, id: int) -> None:
        """
        Delete a public key.

        Args:
            id: id of key to delete

        Returns:
            No content.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: userCurrentDeleteKey
        """
        _response = self._client._request("DELETE", f"/user/keys/{id}")
        return decode(_response, None)


class AsyncUserKeys:
    """The ``user.keys`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(
        self,
        *,
        fingerprint: str | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> AsyncPaginated[PublicKey]:
        """
        List the authenticated user's public keys.

        Args:
            fingerprint: fingerprint of the key
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            PublicKeyList.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: userCurrentListKeys
        """
        _query: dict[str, object] = {"fingerprint": fingerprint}

        return await self._client._paginate("GET", "/user/keys", model=PublicKey, params=_query, page=page, limit=limit)

    async def create(self, *, key: str, read_only: bool | None = None, title: str) -> PublicKey:
        """
        Create a public key.

        Args:
            key: An armored SSH key to add
            read_only: Describe if the key has only read access or read/write
            title: Title of the key to add

        Returns:
            PublicKey.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: userCurrentPostKey
        """
        _payload = CreateKeyOption(
            key=key,
            read_only=read_only,
            title=title,
        ).model_dump(mode="json", by_alias=True, exclude_none=True)

        _response = await self._client._request("POST", "/user/keys", json=_payload)
        return decode(_response, PublicKey)

    async def get(self, id: int) -> PublicKey:
        """
        Get a public key.

        Args:
            id: id of key to get

        Returns:
            PublicKey.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: userCurrentGetKey
        """
        _response = await self._client._request("GET", f"/user/keys/{id}")
        return decode(_response, PublicKey)

    async def delete(self, id: int) -> None:
        """
        Delete a public key.

        Args:
            id: id of key to delete

        Returns:
            No content.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: userCurrentDeleteKey
        """
        _response = await self._client._request("DELETE", f"/user/keys/{id}")
        return decode(_response, None)


class UserQuota:
    """The ``user.quota`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def get(self) -> QuotaInfo:
        """
        Get quota information for the authenticated user.

        Returns:
            QuotaInfo.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: userGetQuota
        """
        _response = self._client._request("GET", "/user/quota")
        return decode(_response, QuotaInfo)

    def artifacts(self, *, page: int | None = None, limit: int | None = None) -> Paginated[QuotaUsedArtifact]:
        """
        List the artifacts affecting the authenticated user's quota.

        Args:
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            QuotaUsedArtifactList.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: userListQuotaArtifacts
        """
        return self._client._paginate("GET", "/user/quota/artifacts", model=QuotaUsedArtifact, page=page, limit=limit)

    def attachments(self, *, page: int | None = None, limit: int | None = None) -> Paginated[QuotaUsedAttachment]:
        """
        List the attachments affecting the authenticated user's quota.

        Args:
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            QuotaUsedAttachmentList.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: userListQuotaAttachments
        """
        return self._client._paginate(
            "GET", "/user/quota/attachments", model=QuotaUsedAttachment, page=page, limit=limit
        )

    def check(self, *, subject: str) -> bool:
        """
        Check if the authenticated user is over quota for a given subject.

        Args:
            subject: subject of the quota

        Returns:
            Returns true if the action is accepted.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: userCheckQuota
        """
        _query: dict[str, object] = {"subject": subject}

        _response = self._client._request("GET", "/user/quota/check", params=_query)
        return decode(_response, bool)

    def packages(self, *, page: int | None = None, limit: int | None = None) -> Paginated[QuotaUsedPackage]:
        """
        List the packages affecting the authenticated user's quota.

        Args:
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            QuotaUsedPackageList.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: userListQuotaPackages
        """
        return self._client._paginate("GET", "/user/quota/packages", model=QuotaUsedPackage, page=page, limit=limit)


class AsyncUserQuota:
    """The ``user.quota`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def get(self) -> QuotaInfo:
        """
        Get quota information for the authenticated user.

        Returns:
            QuotaInfo.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: userGetQuota
        """
        _response = await self._client._request("GET", "/user/quota")
        return decode(_response, QuotaInfo)

    async def artifacts(
        self,
        *,
        page: int | None = None,
        limit: int | None = None,
    ) -> AsyncPaginated[QuotaUsedArtifact]:
        """
        List the artifacts affecting the authenticated user's quota.

        Args:
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            QuotaUsedArtifactList.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: userListQuotaArtifacts
        """
        return await self._client._paginate(
            "GET", "/user/quota/artifacts", model=QuotaUsedArtifact, page=page, limit=limit
        )

    async def attachments(
        self,
        *,
        page: int | None = None,
        limit: int | None = None,
    ) -> AsyncPaginated[QuotaUsedAttachment]:
        """
        List the attachments affecting the authenticated user's quota.

        Args:
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            QuotaUsedAttachmentList.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: userListQuotaAttachments
        """
        return await self._client._paginate(
            "GET", "/user/quota/attachments", model=QuotaUsedAttachment, page=page, limit=limit
        )

    async def check(self, *, subject: str) -> bool:
        """
        Check if the authenticated user is over quota for a given subject.

        Args:
            subject: subject of the quota

        Returns:
            Returns true if the action is accepted.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: userCheckQuota
        """
        _query: dict[str, object] = {"subject": subject}

        _response = await self._client._request("GET", "/user/quota/check", params=_query)
        return decode(_response, bool)

    async def packages(self, *, page: int | None = None, limit: int | None = None) -> AsyncPaginated[QuotaUsedPackage]:
        """
        List the packages affecting the authenticated user's quota.

        Args:
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            QuotaUsedPackageList.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: userListQuotaPackages
        """
        return await self._client._paginate(
            "GET", "/user/quota/packages", model=QuotaUsedPackage, page=page, limit=limit
        )


class UserRepos:
    """The ``user.repos`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(
        self,
        *,
        order_by: Literal[
            "name",
            "id",
            "newest",
            "oldest",
            "recentupdate",
            "leastupdate",
            "reversealphabetically",
            "alphabetically",
            "reversesize",
            "size",
            "reversegitsize",
            "gitsize",
            "reverselfssize",
            "lfssize",
            "moststars",
            "feweststars",
            "mostforks",
            "fewestforks",
        ]
        | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> Paginated[Repository]:
        """
        List the repos that the authenticated user owns.

        Args:
            order_by: order the repositories
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            RepositoryList.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: userCurrentListRepos
        """
        _query: dict[str, object] = {"order_by": order_by}

        return self._client._paginate("GET", "/user/repos", model=Repository, params=_query, page=page, limit=limit)

    def create(
        self,
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
        Create a repository.

        Args:
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
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            ConflictError: 409. The repository with the same name already exists.
            PayloadTooLargeError: 413. QuotaExceeded.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: createCurrentUserRepo
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

        _response = self._client._request("POST", "/user/repos", json=_payload)
        return decode(_response, Repository)


class AsyncUserRepos:
    """The ``user.repos`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(
        self,
        *,
        order_by: Literal[
            "name",
            "id",
            "newest",
            "oldest",
            "recentupdate",
            "leastupdate",
            "reversealphabetically",
            "alphabetically",
            "reversesize",
            "size",
            "reversegitsize",
            "gitsize",
            "reverselfssize",
            "lfssize",
            "moststars",
            "feweststars",
            "mostforks",
            "fewestforks",
        ]
        | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> AsyncPaginated[Repository]:
        """
        List the repos that the authenticated user owns.

        Args:
            order_by: order the repositories
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            RepositoryList.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: userCurrentListRepos
        """
        _query: dict[str, object] = {"order_by": order_by}

        return await self._client._paginate(
            "GET", "/user/repos", model=Repository, params=_query, page=page, limit=limit
        )

    async def create(
        self,
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
        Create a repository.

        Args:
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
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            ConflictError: 409. The repository with the same name already exists.
            PayloadTooLargeError: 413. QuotaExceeded.
            UnprocessableEntityError: 422. APIValidationError is error format response related to input validation.

        Operation ID: createCurrentUserRepo
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

        _response = await self._client._request("POST", "/user/repos", json=_payload)
        return decode(_response, Repository)


class UserSettings:
    """The ``user.settings`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def get(self) -> UserSettingsModel:
        """
        Get current user's account settings.

        Returns:
            UserSettings.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: getUserSettings
        """
        _response = self._client._request("GET", "/user/settings")
        return decode(_response, UserSettingsModel)

    def update(
        self,
        *,
        description: str | None = None,
        diff_view_style: str | None = None,
        enable_repo_unit_hints: bool | None = None,
        full_name: str | None = None,
        hide_activity: bool | None = None,
        hide_email: bool | None = None,
        hide_pronouns: bool | None = None,
        language: str | None = None,
        location: str | None = None,
        pronouns: str | None = None,
        theme: str | None = None,
        website: str | None = None,
    ) -> UserSettingsModel:
        """
        Update settings in current user's account.

        Args:
            description:
            diff_view_style:
            enable_repo_unit_hints:
            full_name:
            hide_activity:
            hide_email: Privacy
            hide_pronouns:
            language:
            location:
            pronouns:
            theme:
            website:

        Returns:
            UserSettings.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: updateUserSettings
        """
        if (
            description is not None
            or diff_view_style is not None
            or enable_repo_unit_hints is not None
            or full_name is not None
            or hide_activity is not None
            or hide_email is not None
            or hide_pronouns is not None
            or language is not None
            or location is not None
            or pronouns is not None
            or theme is not None
            or website is not None
        ):
            _payload = UserSettingsOptions(
                description=description,
                diff_view_style=diff_view_style,
                enable_repo_unit_hints=enable_repo_unit_hints,
                full_name=full_name,
                hide_activity=hide_activity,
                hide_email=hide_email,
                hide_pronouns=hide_pronouns,
                language=language,
                location=location,
                pronouns=pronouns,
                theme=theme,
                website=website,
            ).model_dump(mode="json", by_alias=True, exclude_none=True)
        else:
            _payload = None

        _response = self._client._request("PATCH", "/user/settings", json=_payload)
        return decode(_response, UserSettingsModel)


class AsyncUserSettings:
    """The ``user.settings`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def get(self) -> UserSettingsModel:
        """
        Get current user's account settings.

        Returns:
            UserSettings.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: getUserSettings
        """
        _response = await self._client._request("GET", "/user/settings")
        return decode(_response, UserSettingsModel)

    async def update(
        self,
        *,
        description: str | None = None,
        diff_view_style: str | None = None,
        enable_repo_unit_hints: bool | None = None,
        full_name: str | None = None,
        hide_activity: bool | None = None,
        hide_email: bool | None = None,
        hide_pronouns: bool | None = None,
        language: str | None = None,
        location: str | None = None,
        pronouns: str | None = None,
        theme: str | None = None,
        website: str | None = None,
    ) -> UserSettingsModel:
        """
        Update settings in current user's account.

        Args:
            description:
            diff_view_style:
            enable_repo_unit_hints:
            full_name:
            hide_activity:
            hide_email: Privacy
            hide_pronouns:
            language:
            location:
            pronouns:
            theme:
            website:

        Returns:
            UserSettings.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: updateUserSettings
        """
        if (
            description is not None
            or diff_view_style is not None
            or enable_repo_unit_hints is not None
            or full_name is not None
            or hide_activity is not None
            or hide_email is not None
            or hide_pronouns is not None
            or language is not None
            or location is not None
            or pronouns is not None
            or theme is not None
            or website is not None
        ):
            _payload = UserSettingsOptions(
                description=description,
                diff_view_style=diff_view_style,
                enable_repo_unit_hints=enable_repo_unit_hints,
                full_name=full_name,
                hide_activity=hide_activity,
                hide_email=hide_email,
                hide_pronouns=hide_pronouns,
                language=language,
                location=location,
                pronouns=pronouns,
                theme=theme,
                website=website,
            ).model_dump(mode="json", by_alias=True, exclude_none=True)
        else:
            _payload = None

        _response = await self._client._request("PATCH", "/user/settings", json=_payload)
        return decode(_response, UserSettingsModel)


class UserStarred:
    """The ``user.starred`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(self, *, page: int | None = None, limit: int | None = None) -> Paginated[Repository]:
        """
        The repos that the authenticated user has starred.

        Args:
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            RepositoryList.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: userCurrentListStarred
        """
        return self._client._paginate("GET", "/user/starred", model=Repository, page=page, limit=limit)

    def get(self, owner: str, repo: str) -> None:
        """
        Whether the authenticated is starring the repo.

        Args:
            owner: owner of the repo
            repo: name of the repo

        Returns:
            No content.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: userCurrentCheckStarring
        """
        _response = self._client._request("GET", f"/user/starred/{owner}/{repo}")
        return decode(_response, None)

    def add(self, owner: str, repo: str) -> None:
        """
        Star the given repo.

        Args:
            owner: owner of the repo to star
            repo: name of the repo to star

        Returns:
            No content.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: userCurrentPutStar
        """
        _response = self._client._request("PUT", f"/user/starred/{owner}/{repo}")
        return decode(_response, None)

    def remove(self, owner: str, repo: str) -> None:
        """
        Unstar the given repo.

        Args:
            owner: owner of the repo to unstar
            repo: name of the repo to unstar

        Returns:
            No content.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: userCurrentDeleteStar
        """
        _response = self._client._request("DELETE", f"/user/starred/{owner}/{repo}")
        return decode(_response, None)


class AsyncUserStarred:
    """The ``user.starred`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(self, *, page: int | None = None, limit: int | None = None) -> AsyncPaginated[Repository]:
        """
        The repos that the authenticated user has starred.

        Args:
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            RepositoryList.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.

        Operation ID: userCurrentListStarred
        """
        return await self._client._paginate("GET", "/user/starred", model=Repository, page=page, limit=limit)

    async def get(self, owner: str, repo: str) -> None:
        """
        Whether the authenticated is starring the repo.

        Args:
            owner: owner of the repo
            repo: name of the repo

        Returns:
            No content.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: userCurrentCheckStarring
        """
        _response = await self._client._request("GET", f"/user/starred/{owner}/{repo}")
        return decode(_response, None)

    async def add(self, owner: str, repo: str) -> None:
        """
        Star the given repo.

        Args:
            owner: owner of the repo to star
            repo: name of the repo to star

        Returns:
            No content.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: userCurrentPutStar
        """
        _response = await self._client._request("PUT", f"/user/starred/{owner}/{repo}")
        return decode(_response, None)

    async def remove(self, owner: str, repo: str) -> None:
        """
        Unstar the given repo.

        Args:
            owner: owner of the repo to unstar
            repo: name of the repo to unstar

        Returns:
            No content.

        Raises:
            UnauthorizedError: 401. APIUnauthorizedError is a unauthorized error response.
            ForbiddenError: 403. APIForbiddenError is a forbidden error response.
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: userCurrentDeleteStar
        """
        _response = await self._client._request("DELETE", f"/user/starred/{owner}/{repo}")
        return decode(_response, None)
