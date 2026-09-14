"""Generated from spec/openapi.json (PullReviewComment). Do not edit by hand."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from pyfj._generated.models.user import User


class PullReviewComment(BaseModel):
    """PullReviewComment represents a comment on a pull request review"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    body: str | None = None
    commit_id: str | None = None
    created_at: datetime | None = None
    diff_hunk: str | None = None
    extra_lines_count: int | None = Field(
        default=None, description="number of additional lines after the commented line (0 = single line comment)"
    )
    html_url: str | None = None
    id: int | None = None
    original_commit_id: str | None = None
    original_position: int | None = None
    path: str | None = None
    position: int | None = None
    pull_request_review_id: int | None = None
    pull_request_url: str | None = None
    resolver: User | None = None
    updated_at: datetime | None = None
    user: User | None = None
