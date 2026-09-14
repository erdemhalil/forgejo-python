"""Generated from spec/openapi.json (CreateTagProtectionOption). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class CreateTagProtectionOption(BaseModel):
    """CreateTagProtectionOption options for creating a tag protection"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name_pattern: str | None = None
    whitelist_teams: list[str] | None = None
    whitelist_usernames: list[str] | None = None
