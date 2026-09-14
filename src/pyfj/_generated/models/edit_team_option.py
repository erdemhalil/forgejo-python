"""Generated from spec/openapi.json (EditTeamOption). Do not edit by hand."""

from __future__ import annotations

from enum import StrEnum

from pydantic import BaseModel, ConfigDict


class EditTeamOptionPermission(StrEnum):
    READ = "read"
    WRITE = "write"
    ADMIN = "admin"


class EditTeamOption(BaseModel):
    """EditTeamOption options for editing a team"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    can_create_org_repo: bool | None = None
    description: str | None = None
    includes_all_repositories: bool | None = None
    name: str
    permission: EditTeamOptionPermission | None = None
    units: list[str] | None = None
    units_map: dict[str, str] | None = None
