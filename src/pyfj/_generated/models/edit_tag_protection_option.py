"""Generated from spec/openapi.json (EditTagProtectionOption). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class EditTagProtectionOption(BaseModel):
    """EditTagProtectionOption options for editing a tag protection"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name_pattern: str | None = None
    whitelist_teams: list[str] | None = None
    whitelist_usernames: list[str] | None = None
