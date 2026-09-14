"""Generated from spec/openapi.json (TrackedTime). Do not edit by hand."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from pyfj._generated.models.issue import Issue


class TrackedTime(BaseModel):
    """TrackedTime worked time for an issue / pr"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    created: datetime | None = None
    id: int | None = None
    issue: Issue | None = None
    issue_id: int | None = Field(default=None, description="deprecated (only for backwards compatibility)")
    time: int | None = Field(default=None, description="Time in seconds")
    user_id: int | None = Field(default=None, description="deprecated (only for backwards compatibility)")
    user_name: str | None = None
