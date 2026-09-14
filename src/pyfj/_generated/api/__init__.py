"""Generated Forgejo clients with typed namespace attributes. Do not edit by hand.

Regenerate with ``python -m codegen``; see docs/development/codegen.md.
"""

from __future__ import annotations

from functools import cached_property

from pyfj._generated.api.activitypub import Activitypub, AsyncActivitypub
from pyfj._generated.api.admin import Admin, AsyncAdmin
from pyfj._generated.api.misc import AsyncMisc, Misc
from pyfj._generated.api.notifications import AsyncNotifications, Notifications
from pyfj._generated.api.orgs import AsyncOrgs, Orgs
from pyfj._generated.api.packages import AsyncPackages, Packages
from pyfj._generated.api.repos import AsyncRepos, Repos
from pyfj._generated.api.settings import AsyncSettings, Settings
from pyfj._generated.api.teams import AsyncTeams, Teams
from pyfj._generated.api.user import AsyncUser, User
from pyfj._generated.api.users import AsyncUsers, Users
from pyfj._runtime import AsyncForgejo as _RuntimeAsyncForgejo
from pyfj._runtime import Forgejo as _RuntimeForgejo

__all__ = ["AsyncForgejo", "Forgejo"]


class Forgejo(_RuntimeForgejo):
    """The synchronous pyfj client."""

    @cached_property
    def activitypub(self) -> Activitypub:
        """The ``activitypub`` namespace."""
        return Activitypub(self)

    @cached_property
    def admin(self) -> Admin:
        """The ``admin`` namespace."""
        return Admin(self)

    @cached_property
    def misc(self) -> Misc:
        """The ``misc`` namespace."""
        return Misc(self)

    @cached_property
    def notifications(self) -> Notifications:
        """The ``notifications`` namespace."""
        return Notifications(self)

    @cached_property
    def orgs(self) -> Orgs:
        """The ``orgs`` namespace."""
        return Orgs(self)

    @cached_property
    def packages(self) -> Packages:
        """The ``packages`` namespace."""
        return Packages(self)

    @cached_property
    def repos(self) -> Repos:
        """The ``repos`` namespace."""
        return Repos(self)

    @cached_property
    def settings(self) -> Settings:
        """The ``settings`` namespace."""
        return Settings(self)

    @cached_property
    def teams(self) -> Teams:
        """The ``teams`` namespace."""
        return Teams(self)

    @cached_property
    def user(self) -> User:
        """The ``user`` namespace."""
        return User(self)

    @cached_property
    def users(self) -> Users:
        """The ``users`` namespace."""
        return Users(self)


class AsyncForgejo(_RuntimeAsyncForgejo):
    """The asynchronous pyfj client."""

    @cached_property
    def activitypub(self) -> AsyncActivitypub:
        """The ``activitypub`` namespace."""
        return AsyncActivitypub(self)

    @cached_property
    def admin(self) -> AsyncAdmin:
        """The ``admin`` namespace."""
        return AsyncAdmin(self)

    @cached_property
    def misc(self) -> AsyncMisc:
        """The ``misc`` namespace."""
        return AsyncMisc(self)

    @cached_property
    def notifications(self) -> AsyncNotifications:
        """The ``notifications`` namespace."""
        return AsyncNotifications(self)

    @cached_property
    def orgs(self) -> AsyncOrgs:
        """The ``orgs`` namespace."""
        return AsyncOrgs(self)

    @cached_property
    def packages(self) -> AsyncPackages:
        """The ``packages`` namespace."""
        return AsyncPackages(self)

    @cached_property
    def repos(self) -> AsyncRepos:
        """The ``repos`` namespace."""
        return AsyncRepos(self)

    @cached_property
    def settings(self) -> AsyncSettings:
        """The ``settings`` namespace."""
        return AsyncSettings(self)

    @cached_property
    def teams(self) -> AsyncTeams:
        """The ``teams`` namespace."""
        return AsyncTeams(self)

    @cached_property
    def user(self) -> AsyncUser:
        """The ``user`` namespace."""
        return AsyncUser(self)

    @cached_property
    def users(self) -> AsyncUsers:
        """The ``users`` namespace."""
        return AsyncUsers(self)
