"""Generated from spec/openapi.json (PullReviewRequestOptions). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class PullReviewRequestOptions(BaseModel):
    """PullReviewRequestOptions are options to add or remove pull review requests"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    reviewers: list[str] | None = None
    team_reviewers: list[str] | None = None
