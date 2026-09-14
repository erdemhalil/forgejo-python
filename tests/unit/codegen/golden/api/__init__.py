"""Generated Forgejo clients with typed namespace attributes. Do not edit by hand.

Regenerate with ``python -m codegen``; see docs/development/codegen.md.
"""

from __future__ import annotations

from functools import cached_property

from pyfj._generated.api.admin import Admin, AsyncAdmin
from pyfj._generated.api.misc import AsyncMisc, Misc
from pyfj._generated.api.orgs import AsyncOrgs, Orgs
from pyfj._generated.api.users import AsyncUsers, Users
from pyfj._runtime import AsyncForgejo as _RuntimeAsyncForgejo
from pyfj._runtime import Forgejo as _RuntimeForgejo

__all__ = ["AsyncForgejo", "Forgejo"]


class Forgejo(_RuntimeForgejo):
    """The synchronous pyfj client."""

    @cached_property
    def admin(self) -> Admin:
        """The ``admin`` namespace."""
        return Admin(self)

    @cached_property
    def misc(self) -> Misc:
        """The ``misc`` namespace."""
        return Misc(self)

    @cached_property
    def orgs(self) -> Orgs:
        """The ``orgs`` namespace."""
        return Orgs(self)

    @cached_property
    def users(self) -> Users:
        """The ``users`` namespace."""
        return Users(self)


class AsyncForgejo(_RuntimeAsyncForgejo):
    """The asynchronous pyfj client."""

    @cached_property
    def admin(self) -> AsyncAdmin:
        """The ``admin`` namespace."""
        return AsyncAdmin(self)

    @cached_property
    def misc(self) -> AsyncMisc:
        """The ``misc`` namespace."""
        return AsyncMisc(self)

    @cached_property
    def orgs(self) -> AsyncOrgs:
        """The ``orgs`` namespace."""
        return AsyncOrgs(self)

    @cached_property
    def users(self) -> AsyncUsers:
        """The ``users`` namespace."""
        return AsyncUsers(self)
