"""pyfj's exception hierarchy.

Every error raised by pyfj derives from :class:`ForgejoError`::

    ForgejoError
    ├── TransportError            network/timeout; wraps httpx.TransportError
    ├── DecodeError               response did not match the Spec
    └── APIError                  any non-2xx; carries status_code, body, response
        ├── BadRequestError           400
        ├── UnauthorizedError         401
        ├── ForbiddenError            403
        ├── NotFoundError             404
        ├── MethodNotAllowedError     405
        ├── ConflictError             409
        ├── PreconditionFailedError   412
        ├── PayloadTooLargeError      413
        ├── UnprocessableEntityError  422
        ├── LockedError               423
        ├── ServerError               5xx
        └── (other statuses map to APIError itself)

``APIError.body`` holds the JSON-decoded body when the response could be
parsed, and ``response.text`` otherwise. ``APIError.response`` is always the
raw :class:`httpx.Response`, so callers can inspect headers or stream content.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import httpx

__all__ = [
    "APIError",
    "BadRequestError",
    "ConflictError",
    "DecodeError",
    "ForbiddenError",
    "ForgejoError",
    "LockedError",
    "MethodNotAllowedError",
    "NotFoundError",
    "PayloadTooLargeError",
    "PreconditionFailedError",
    "ServerError",
    "TransportError",
    "UnauthorizedError",
    "UnprocessableEntityError",
    "api_error",
]


class ForgejoError(Exception):
    """Base class for every error raised by pyfj."""


class TransportError(ForgejoError):
    """The request produced no HTTP response: connection failure or timeout.

    Wraps the underlying :class:`httpx.TransportError` (available as
    :attr:`cause`, and chained via ``raise ... from``).
    """

    def __init__(self, method: str, url: str, cause: BaseException) -> None:
        super().__init__(f"{method} {url} failed: {cause}")
        self.method = method
        self.url = url
        self.cause = cause


class DecodeError(ForgejoError):
    """A documented response could not be decoded to its declared type.

    Raised by :func:`pyfj._runtime.decode.decode` when the body is not valid
    JSON for the requested model, fails pydantic validation, or does not have
    the documented JSON shape.
    """

    def __init__(self, response: httpx.Response, reason: str) -> None:
        request = response.request
        super().__init__(f"cannot decode {request.method} {request.url}: {reason}")
        self.response = response
        self.reason = reason


def _parse_body(response: httpx.Response) -> object:
    """Return the JSON-decoded body when possible, else the response text."""
    try:
        return response.json()
    except ValueError:
        return response.text


def _detail(body: object) -> str:
    """Best-effort human-readable detail from an error body."""
    if isinstance(body, str):
        return body.strip()
    if isinstance(body, dict):
        message = body.get("message")
        if isinstance(message, str):
            return message
    return ""


class APIError(ForgejoError):
    """The instance returned a non-2xx response.

    Attributes:
        status_code: the HTTP status code.
        body: the JSON-decoded body when possible, otherwise the response text.
        response: the raw :class:`httpx.Response`.
    """

    def __init__(self, response: httpx.Response) -> None:
        self.response = response
        self.status_code = response.status_code
        self.body = _parse_body(response)
        message = f"{response.request.method} {response.request.url} returned HTTP {self.status_code}"
        detail = _detail(self.body)
        if detail:
            message = f"{message}: {detail}"
        super().__init__(message)


class BadRequestError(APIError):
    """HTTP 400: the request was malformed."""


class UnauthorizedError(APIError):
    """HTTP 401: credentials are missing or invalid."""


class ForbiddenError(APIError):
    """HTTP 403: the authenticated user may not perform the operation."""


class NotFoundError(APIError):
    """HTTP 404: the requested object does not exist."""


class MethodNotAllowedError(APIError):
    """HTTP 405: the operation is not allowed on this resource."""


class ConflictError(APIError):
    """HTTP 409: the request conflicts with the current state."""


class PreconditionFailedError(APIError):
    """HTTP 412: a precondition (ETag, If-Match, ...) failed."""


class PayloadTooLargeError(APIError):
    """HTTP 413: the uploaded payload exceeds a server limit."""


class UnprocessableEntityError(APIError):
    """HTTP 422: the request was well-formed but semantically invalid."""


class LockedError(APIError):
    """HTTP 423: the resource is locked."""


class ServerError(APIError):
    """HTTP 5xx: the instance failed to process a valid request."""


_ERRORS_BY_STATUS: dict[int, type[APIError]] = {
    400: BadRequestError,
    401: UnauthorizedError,
    403: ForbiddenError,
    404: NotFoundError,
    405: MethodNotAllowedError,
    409: ConflictError,
    412: PreconditionFailedError,
    413: PayloadTooLargeError,
    422: UnprocessableEntityError,
    423: LockedError,
}

_SERVER_ERROR_MIN = 500
_SERVER_ERROR_MAX = 600


def api_error(response: httpx.Response) -> APIError:
    """Build the mapped exception for a non-2xx response.

    Unmapped 4xx, 3xx, and informational statuses map to :class:`APIError`;
    every 5xx maps to :class:`ServerError`.
    """
    mapped = _ERRORS_BY_STATUS.get(response.status_code)
    if mapped is not None:
        return mapped(response)
    if _SERVER_ERROR_MIN <= response.status_code < _SERVER_ERROR_MAX:
        return ServerError(response)
    return APIError(response)
