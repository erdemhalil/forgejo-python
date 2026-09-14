"""Generated from spec/openapi.json (ExternalTracker). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class ExternalTracker(BaseModel):
    """ExternalTracker represents settings for external tracker"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    external_tracker_format: str | None = Field(
        default=None,
        description=(
            "External Issue Tracker URL Format. Use the placeholders {user}, {repo} and {index} for the username,"
            " repository name and issue index."
        ),
    )
    external_tracker_regexp_pattern: str | None = Field(
        default=None, description="External Issue Tracker issue regular expression"
    )
    external_tracker_style: str | None = Field(
        default=None, description="External Issue Tracker Number Format, either `numeric`, `alphanumeric`, or `regexp`"
    )
    external_tracker_url: str | None = Field(default=None, description="URL of external issue tracker.")
