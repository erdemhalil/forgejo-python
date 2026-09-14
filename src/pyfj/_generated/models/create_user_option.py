"""Generated from spec/openapi.json (CreateUserOption). Do not edit by hand."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class CreateUserOption(BaseModel):
    """CreateUserOption create user options"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    created_at: datetime | None = Field(
        default=None,
        description=(
            "For explicitly setting the user creation timestamp. Useful when users are migrated from other "
            'systems. When omitted, the user\'s creation timestamp will be set to "now".'
        ),
    )
    email: str
    full_name: str | None = None
    login_name: str | None = None
    must_change_password: bool | None = None
    password: str | None = None
    restricted: bool | None = None
    send_notify: bool | None = None
    source_id: int | None = None
    username: str
    visibility: str | None = None
