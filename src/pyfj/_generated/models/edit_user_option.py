"""Generated from spec/openapi.json (EditUserOption). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class EditUserOption(BaseModel):
    """EditUserOption edit user options"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    active: bool | None = None
    admin: bool | None = None
    allow_create_organization: bool | None = None
    allow_git_hook: bool | None = None
    allow_import_local: bool | None = None
    description: str | None = None
    email: str | None = None
    full_name: str | None = None
    hide_email: bool | None = None
    location: str | None = None
    login_name: str | None = None
    max_repo_creation: int | None = None
    must_change_password: bool | None = None
    password: str | None = None
    prohibit_login: bool | None = None
    pronouns: str | None = None
    restricted: bool | None = None
    source_id: int | None = None
    visibility: str | None = None
    website: str | None = None
