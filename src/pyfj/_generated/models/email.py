"""Generated from spec/openapi.json (Email). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class Email(BaseModel):
    """Email an email address belonging to a user"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    email: str | None = None
    primary: bool | None = None
    user_id: int | None = None
    username: str | None = None
    verified: bool | None = None
