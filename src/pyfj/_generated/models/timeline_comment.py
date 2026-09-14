"""Generated from spec/openapi.json (TimelineComment). Do not edit by hand."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from pyfj._generated.models.comment import Comment
from pyfj._generated.models.issue import Issue
from pyfj._generated.models.label import Label
from pyfj._generated.models.milestone import Milestone
from pyfj._generated.models.team import Team
from pyfj._generated.models.tracked_time import TrackedTime
from pyfj._generated.models.user import User


class TimelineComment(BaseModel):
    """TimelineComment represents a timeline comment (comment of any type) on a commit or issue"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    assignee: User | None = None
    assignee_team: Team | None = None
    body: str | None = None
    created_at: datetime | None = None
    dependent_issue: Issue | None = None
    html_url: str | None = None
    id: int | None = None
    issue_url: str | None = None
    label: Label | None = None
    milestone: Milestone | None = None
    new_ref: str | None = None
    new_title: str | None = None
    old_milestone: Milestone | None = None
    old_project_id: int | None = None
    old_ref: str | None = None
    old_title: str | None = None
    project_id: int | None = None
    pull_request_url: str | None = None
    ref_action: str | None = None
    ref_comment: Comment | None = None
    ref_commit_sha: str | None = Field(default=None, description="commit SHA where issue/PR was referenced")
    ref_issue: Issue | None = None
    removed_assignee: bool | None = Field(default=None, description="whether the assignees were removed or added")
    resolve_doer: User | None = None
    review_id: int | None = None
    tracked_time: TrackedTime | None = None
    type: str | None = None
    updated_at: datetime | None = None
    user: User | None = None
