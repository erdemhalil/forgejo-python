"""Generated from spec/openapi.json (InternalTracker). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class InternalTracker(BaseModel):
    """InternalTracker represents settings for internal tracker"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    allow_only_contributors_to_track_time: bool | None = Field(
        default=None, description="Let only contributors track time (Built-in issue tracker)"
    )
    enable_issue_dependencies: bool | None = Field(
        default=None, description="Enable dependencies for issues and pull requests (Built-in issue tracker)"
    )
    enable_time_tracker: bool | None = Field(default=None, description="Enable time tracking (Built-in issue tracker)")
