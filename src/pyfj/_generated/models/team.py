"""Generated from spec/openapi.json (Team). Do not edit by hand."""

from __future__ import annotations

from enum import StrEnum

from pydantic import BaseModel, ConfigDict

from pyfj._generated.models.organization import Organization


class TeamPermission(StrEnum):
    NONE = "none"
    READ = "read"
    WRITE = "write"
    ADMIN = "admin"
    OWNER = "owner"


class Team(BaseModel):
    """Team represents a team in an organization"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    can_create_org_repo: bool | None = None
    description: str | None = None
    id: int | None = None
    includes_all_repositories: bool | None = None
    name: str | None = None
    organization: Organization | None = None
    permission: TeamPermission | None = None
    units: list[str] | None = None
    units_map: dict[str, str] | None = None
