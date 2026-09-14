"""Handwritten runtime: transport, auth, pagination, errors, decoding.

This package is the import point for generated code: ``_generated/api``
modules import :func:`decode`, :class:`Paginated`, :class:`AsyncPaginated`,
and the client classes from here.

The frozen request-hook and namespace-binding contracts live in the
:mod:`pyfj._runtime.client` module docstring; read it before changing either.
"""

from __future__ import annotations

from pyfj._runtime.auth import Auth
from pyfj._runtime.client import API_PATH, AsyncForgejo, Forgejo
from pyfj._runtime.decode import decode
from pyfj._runtime.errors import (
    APIError,
    BadRequestError,
    ConflictError,
    DecodeError,
    ForbiddenError,
    ForgejoError,
    LockedError,
    MethodNotAllowedError,
    NotFoundError,
    PayloadTooLargeError,
    PreconditionFailedError,
    ServerError,
    TransportError,
    UnauthorizedError,
    UnprocessableEntityError,
    api_error,
)
from pyfj._runtime.pagination import AsyncPaginated, Paginated

__all__ = [
    "API_PATH",
    "APIError",
    "AsyncForgejo",
    "AsyncPaginated",
    "Auth",
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
    "api_error",
    "decode",
]
