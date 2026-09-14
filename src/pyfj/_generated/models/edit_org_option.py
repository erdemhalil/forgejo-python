"""Generated from spec/openapi.json (EditOrgOption). Do not edit by hand."""

from __future__ import annotations

from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field


class EditOrgOptionVisibility(StrEnum):
    """possible values are `public`, `limited` or `private`"""

    PUBLIC = "public"
    LIMITED = "limited"
    PRIVATE = "private"


class EditOrgOption(BaseModel):
    """EditOrgOption options for editing an organization"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    description: str | None = None
    email: str | None = None
    full_name: str | None = None
    location: str | None = None
    repo_admin_change_team_access: bool | None = None
    visibility: EditOrgOptionVisibility | None = Field(
        default=None, description="possible values are `public`, `limited` or `private`"
    )
    website: str | None = None
