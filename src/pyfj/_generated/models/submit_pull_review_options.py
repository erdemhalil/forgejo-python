"""Generated from spec/openapi.json (SubmitPullReviewOptions). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict

from pyfj._generated.models.review_state_type import ReviewStateType


class SubmitPullReviewOptions(BaseModel):
    """SubmitPullReviewOptions are options to submit a pending pull review"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    body: str | None = None
    event: ReviewStateType | None = None
