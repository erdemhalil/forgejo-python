"""Generated from spec/openapi.json (ActionTask). Do not edit by hand."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ActionTask(BaseModel):
    """ActionTask represents a ActionTask"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    created_at: datetime | None = None
    display_title: str | None = None
    event: str | None = None
    head_branch: str | None = None
    head_sha: str | None = None
    id: int | None = None
    name: str | None = None
    run_number: int | None = None
    run_started_at: datetime | None = None
    status: str | None = None
    updated_at: datetime | None = None
    url: str | None = None
    workflow_id: str | None = None
