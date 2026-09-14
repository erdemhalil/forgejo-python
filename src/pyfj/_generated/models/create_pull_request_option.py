"""Generated from spec/openapi.json (CreatePullRequestOption). Do not edit by hand."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict


class CreatePullRequestOption(BaseModel):
    """CreatePullRequestOption options when creating a pull request"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    assignee: str | None = None
    assignees: list[str] | None = None
    base: str | None = None
    body: str | None = None
    due_date: datetime | None = None
    head: str | None = None
    labels: list[int] | None = None
    milestone: int | None = None
    title: str | None = None
