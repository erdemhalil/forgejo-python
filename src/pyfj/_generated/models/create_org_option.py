"""Generated from spec/openapi.json (CreateOrgOption). Do not edit by hand."""

from __future__ import annotations

from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field


class CreateOrgOptionVisibility(StrEnum):
    """possible values are `public` (default), `limited` or `private`"""

    PUBLIC = "public"
    LIMITED = "limited"
    PRIVATE = "private"


class CreateOrgOption(BaseModel):
    """CreateOrgOption options for creating an organization"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    description: str | None = None
    email: str | None = None
    full_name: str | None = None
    location: str | None = None
    repo_admin_change_team_access: bool | None = None
    username: str
    visibility: CreateOrgOptionVisibility | None = Field(
        default=None, description="possible values are `public` (default), `limited` or `private`"
    )
    website: str | None = None
