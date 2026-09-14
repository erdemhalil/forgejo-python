"""Generated from spec/openapi.json (Organization). Do not edit by hand."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class Organization(BaseModel):
    """Organization represents an organization"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    avatar_url: str | None = None
    created: datetime | None = None
    description: str | None = None
    email: str | None = None
    full_name: str | None = None
    id: int | None = None
    location: str | None = None
    name: str | None = None
    repo_admin_change_team_access: bool | None = None
    username: str | None = Field(default=None, description="deprecated")
    visibility: str | None = None
    website: str | None = None
