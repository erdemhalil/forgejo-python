"""Generated from spec/openapi.json (CreateIssueCommentOption). Do not edit by hand."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class CreateIssueCommentOption(BaseModel):
    """CreateIssueCommentOption options for creating a comment on an issue"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    body: str = Field(description="The body of the comment")
    updated_at: datetime | None = Field(
        default=None, description="The time of the comment's update, needs admin or repository owner permission"
    )
