"""Generated from spec/openapi.json (CreateIssueOption). Do not edit by hand."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class CreateIssueOption(BaseModel):
    """CreateIssueOption options to create one issue"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    assignee: str | None = Field(default=None, description="deprecated")
    assignees: list[str] | None = None
    body: str | None = None
    closed: bool | None = None
    due_date: datetime | None = None
    labels: list[int] | None = Field(default=None, description="list of label ids")
    milestone: int | None = Field(default=None, description="milestone id")
    ref: str | None = None
    title: str
