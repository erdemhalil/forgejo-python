"""Generated from spec/openapi.json (TagProtection). Do not edit by hand."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict


class TagProtection(BaseModel):
    """TagProtection represents a tag protection"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    created_at: datetime | None = None
    id: int | None = None
    name_pattern: str | None = None
    updated_at: datetime | None = None
    whitelist_teams: list[str] | None = None
    whitelist_usernames: list[str] | None = None
