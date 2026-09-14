"""Generated from spec/openapi.json (UserSettings). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class UserSettings(BaseModel):
    """UserSettings represents user settings"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    description: str | None = None
    diff_view_style: str | None = None
    enable_repo_unit_hints: bool | None = None
    full_name: str | None = None
    hide_activity: bool | None = None
    hide_email: bool | None = Field(default=None, description="Privacy")
    hide_pronouns: bool | None = None
    language: str | None = None
    location: str | None = None
    pronouns: str | None = None
    theme: str | None = None
    website: str | None = None
