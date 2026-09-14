"""Generated from spec/openapi.json (StopWatch). Do not edit by hand."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict


class StopWatch(BaseModel):
    """StopWatch represent a running stopwatch"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    created: datetime | None = None
    duration: str | None = None
    issue_index: int | None = None
    issue_title: str | None = None
    repo_name: str | None = None
    repo_owner_name: str | None = None
    seconds: int | None = None
