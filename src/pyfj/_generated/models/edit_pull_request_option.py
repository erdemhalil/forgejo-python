"""Generated from spec/openapi.json (EditPullRequestOption). Do not edit by hand."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict


class EditPullRequestOption(BaseModel):
    """EditPullRequestOption options when modify pull request"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    allow_maintainer_edit: bool | None = None
    assignee: str | None = None
    assignees: list[str] | None = None
    base: str | None = None
    body: str | None = None
    due_date: datetime | None = None
    labels: list[int] | None = None
    milestone: int | None = None
    state: str | None = None
    title: str | None = None
    unset_due_date: bool | None = None
