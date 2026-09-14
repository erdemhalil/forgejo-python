"""Generated from spec/openapi.json (CreateTeamOption). Do not edit by hand."""

from __future__ import annotations

from enum import StrEnum

from pydantic import BaseModel, ConfigDict


class CreateTeamOptionPermission(StrEnum):
    READ = "read"
    WRITE = "write"
    ADMIN = "admin"


class CreateTeamOption(BaseModel):
    """CreateTeamOption options for creating a team"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    can_create_org_repo: bool | None = None
    description: str | None = None
    includes_all_repositories: bool | None = None
    name: str
    permission: CreateTeamOptionPermission | None = None
    units: list[str] | None = None
    units_map: dict[str, str] | None = None
