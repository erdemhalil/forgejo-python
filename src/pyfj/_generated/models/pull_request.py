"""Generated from spec/openapi.json (PullRequest). Do not edit by hand."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from pyfj._generated.models.label import Label
from pyfj._generated.models.milestone import Milestone
from pyfj._generated.models.pr_branch_info import PRBranchInfo
from pyfj._generated.models.state_type import StateType
from pyfj._generated.models.team import Team
from pyfj._generated.models.user import User


class PullRequest(BaseModel):
    """PullRequest represents a pull request"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    additions: int | None = None
    allow_maintainer_edit: bool | None = None
    assignee: User | None = None
    assignees: list[User] | None = None
    base: PRBranchInfo | None = None
    body: str | None = None
    changed_files: int | None = None
    closed_at: datetime | None = None
    comments: int | None = None
    created_at: datetime | None = None
    deletions: int | None = None
    diff_url: str | None = None
    draft: bool | None = None
    due_date: datetime | None = None
    flow: int | None = None
    head: PRBranchInfo | None = None
    html_url: str | None = None
    id: int | None = None
    is_locked: bool | None = None
    labels: list[Label] | None = None
    merge_base: str | None = None
    merge_commit_sha: str | None = None
    mergeable: bool | None = None
    merged: bool | None = None
    merged_at: datetime | None = None
    merged_by: User | None = None
    milestone: Milestone | None = None
    number: int | None = None
    patch_url: str | None = None
    pin_order: int | None = None
    requested_reviewers: list[User] | None = None
    requested_reviewers_teams: list[Team] | None = None
    review_comments: int | None = Field(
        default=None,
        description=(
            "number of review comments made on the diff of a PR review (not including comments on commits or "
            "issues in a PR)"
        ),
    )
    state: StateType | None = None
    title: str | None = None
    updated_at: datetime | None = None
    url: str | None = None
    user: User | None = None
