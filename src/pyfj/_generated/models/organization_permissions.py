"""Generated from spec/openapi.json (OrganizationPermissions). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class OrganizationPermissions(BaseModel):
    """OrganizationPermissions list different users permissions on an organization"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    can_create_repository: bool | None = None
    can_read: bool | None = None
    can_write: bool | None = None
    is_admin: bool | None = None
    is_owner: bool | None = None
