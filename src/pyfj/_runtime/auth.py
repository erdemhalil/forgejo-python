"""Credential and header assembly.

``Auth`` is the resolved credential configuration of a client. It is built
once at construction time and turns each request into headers:

- ``token`` → ``Authorization: token <value>`` (an existing ``token `` prefix
  is tolerated and not duplicated);
- ``basic`` → ``Authorization: Basic <base64(user:pass)>``;
- ``otp`` → ``X-FORGEJO-OTP``.

``token`` and ``basic`` are mutually exclusive; constructing ``Auth`` with
both raises :class:`ValueError`.

Impersonation is not a credential: the ``Sudo`` header is composed by the
client from its client-scoped sudo state (see ``pyfj._runtime.client``).
"""

from __future__ import annotations

import base64
from dataclasses import dataclass

__all__ = ["OTP_HEADER", "Auth"]

OTP_HEADER = "X-FORGEJO-OTP"

_SCHEME = "token"
_PREFIX = f"{_SCHEME} "


@dataclass(frozen=True, slots=True)
class Auth:
    """Resolved credentials for one client.

    Args:
        token: API token; sent as ``Authorization: token <value>``.
        basic: ``(username, password)`` pair for HTTP Basic auth.
        otp: one-time password sent as ``X-FORGEJO-OTP``.
    """

    token: str | None = None
    basic: tuple[str, str] | None = None
    otp: str | None = None

    def __post_init__(self) -> None:
        if self.token is not None and self.basic is not None:
            message = "token and basic auth are mutually exclusive"
            raise ValueError(message)
        if self.token is not None and self.token.lower().startswith(_PREFIX):
            object.__setattr__(self, "token", self.token[len(_PREFIX) :])

    @property
    def authorizes_requests(self) -> bool:
        """Whether pyfj itself sets the ``Authorization`` header."""
        return self.token is not None or self.basic is not None

    def headers(self) -> dict[str, str]:
        """Build the credential headers for one request.

        Returns:
            Headers to merge into the request; empty when no credentials are
            configured.
        """
        headers: dict[str, str] = {}
        if self.token is not None:
            headers["Authorization"] = f"{_SCHEME} {self.token}"
        elif self.basic is not None:
            username, password = self.basic
            encoded = base64.b64encode(f"{username}:{password}".encode()).decode("ascii")
            headers["Authorization"] = f"Basic {encoded}"
        if self.otp is not None:
            headers[OTP_HEADER] = self.otp
        return headers
