"""Generated from spec/openapi.json (Issue). Do not edit by hand."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict

from pyfj._generated.models.attachment import Attachment
from pyfj._generated.models.label import Label
from pyfj._generated.models.milestone import Milestone
from pyfj._generated.models.pull_request_meta import PullRequestMeta
from pyfj._generated.models.repository_meta import RepositoryMeta
from pyfj._generated.models.state_type import StateType
from pyfj._generated.models.user import User


class Issue(BaseModel):
    """Issue represents an issue in a repository"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    assets: list[Attachment] | None = None
    assignee: User | None = None
    assignees: list[User] | None = None
    body: str | None = None
    closed_at: datetime | None = None
    comments: int | None = None
    created_at: datetime | None = None
    due_date: datetime | None = None
    html_url: str | None = None
    id: int | None = None
    is_locked: bool | None = None
    labels: list[Label] | None = None
    milestone: Milestone | None = None
    number: int | None = None
    original_author: str | None = None
    original_author_id: int | None = None
    pin_order: int | None = None
    pull_request: PullRequestMeta | None = None
    ref: str | None = None
    repository: RepositoryMeta | None = None
    state: StateType | None = None
    title: str | None = None
    updated_at: datetime | None = None
    url: str | None = None
    user: User | None = None
