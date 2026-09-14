"""Generated from spec/openapi.json (GeneralUISettings). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class GeneralUISettings(BaseModel):
    """GeneralUISettings contains global ui settings exposed by API"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    allowed_reactions: list[str] | None = None
    custom_emojis: list[str] | None = None
    default_theme: str | None = None
