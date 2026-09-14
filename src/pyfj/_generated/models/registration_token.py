"""Generated from spec/openapi.json (RegistrationToken). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class RegistrationToken(BaseModel):
    """RegistrationToken is a string used to register a runner with a server"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    token: str | None = None
