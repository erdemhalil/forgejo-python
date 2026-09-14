"""Generated from spec/openapi.json (PullReview). Do not edit by hand."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict

from pyfj._generated.models.review_state_type import ReviewStateType
from pyfj._generated.models.team import Team
from pyfj._generated.models.user import User


class PullReview(BaseModel):
    """PullReview represents a pull request review"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    body: str | None = None
    comments_count: int | None = None
    commit_id: str | None = None
    dismissed: bool | None = None
    html_url: str | None = None
    id: int | None = None
    official: bool | None = None
    pull_request_url: str | None = None
    stale: bool | None = None
    state: ReviewStateType | None = None
    submitted_at: datetime | None = None
    team: Team | None = None
    updated_at: datetime | None = None
    user: User | None = None
