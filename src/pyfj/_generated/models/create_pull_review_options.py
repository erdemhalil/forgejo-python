"""Generated from spec/openapi.json (CreatePullReviewOptions). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict

from pyfj._generated.models.create_pull_review_comment import CreatePullReviewComment
from pyfj._generated.models.review_state_type import ReviewStateType


class CreatePullReviewOptions(BaseModel):
    """CreatePullReviewOptions are options to create a pull review"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    body: str | None = None
    comments: list[CreatePullReviewComment] | None = None
    commit_id: str | None = None
    event: ReviewStateType | None = None
