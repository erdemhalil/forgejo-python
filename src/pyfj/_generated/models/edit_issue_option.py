"""Generated from spec/openapi.json (EditIssueOption). Do not edit by hand."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class EditIssueOption(BaseModel):
    """EditIssueOption options for editing an issue"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    assignee: str | None = Field(default=None, description="deprecated")
    assignees: list[str] | None = None
    body: str | None = None
    due_date: datetime | None = None
    milestone: int | None = None
    ref: str | None = None
    state: str | None = None
    title: str | None = None
    unset_due_date: bool | None = None
    updated_at: datetime | None = None
