"""pyfj: a fully typed Python client for the Forgejo API.

The public surface is assembled here: :class:`Forgejo` / :class:`AsyncForgejo`
(the generated clients with typed resource namespaces), the exception
hierarchy and pagination types from the runtime, and every generated model
(also importable from :mod:`pyfj.models`). See ``docs/development/architecture.md``.
"""

from __future__ import annotations

from pyfj import models as models
from pyfj._generated.api import AsyncForgejo, Forgejo
from pyfj._generated.models import *  # noqa: F403
from pyfj._generated.models import __all__ as _model_exports
from pyfj._runtime import (
    API_PATH,
    APIError,
    AsyncPaginated,
    BadRequestError,
    ConflictError,
    DecodeError,
    ForbiddenError,
    ForgejoError,
    LockedError,
    MethodNotAllowedError,
    NotFoundError,
    Paginated,
    PayloadTooLargeError,
    PreconditionFailedError,
    ServerError,
    TransportError,
    UnauthorizedError,
    UnprocessableEntityError,
)

# ``pyfj.APIError`` is the runtime exception (the documented error surface);
# the Spec's ``APIError`` model stays importable as ``pyfj.models.APIError``.
# The generated model list is filtered so the name appears exactly once.
__all__ = [
    *(name for name in _model_exports if name != "APIError"),
    "API_PATH",
    "APIError",
    "AsyncForgejo",
    "AsyncPaginated",
    "BadRequestError",
    "ConflictError",
    "DecodeError",
    "ForbiddenError",
    "Forgejo",
    "ForgejoError",
    "LockedError",
    "MethodNotAllowedError",
    "NotFoundError",
    "Paginated",
    "PayloadTooLargeError",
    "PreconditionFailedError",
    "ServerError",
    "TransportError",
    "UnauthorizedError",
    "UnprocessableEntityError",
    "models",
]
