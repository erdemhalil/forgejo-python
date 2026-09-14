"""Generated from spec/openapi.json (Activity). Do not edit by hand."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field

from pyfj._generated.models.comment import Comment
from pyfj._generated.models.repository import Repository
from pyfj._generated.models.user import User


class ActivityOpType(StrEnum):
    """the type of action"""

    CREATE_REPO = "create_repo"
    RENAME_REPO = "rename_repo"
    STAR_REPO = "star_repo"
    WATCH_REPO = "watch_repo"
    COMMIT_REPO = "commit_repo"
    CREATE_ISSUE = "create_issue"
    CREATE_PULL_REQUEST = "create_pull_request"
    TRANSFER_REPO = "transfer_repo"
    PUSH_TAG = "push_tag"
    COMMENT_ISSUE = "comment_issue"
    MERGE_PULL_REQUEST = "merge_pull_request"
    CLOSE_ISSUE = "close_issue"
    REOPEN_ISSUE = "reopen_issue"
    CLOSE_PULL_REQUEST = "close_pull_request"
    REOPEN_PULL_REQUEST = "reopen_pull_request"
    DELETE_TAG = "delete_tag"
    DELETE_BRANCH = "delete_branch"
    MIRROR_SYNC_PUSH = "mirror_sync_push"
    MIRROR_SYNC_CREATE = "mirror_sync_create"
    MIRROR_SYNC_DELETE = "mirror_sync_delete"
    APPROVE_PULL_REQUEST = "approve_pull_request"
    REJECT_PULL_REQUEST = "reject_pull_request"
    COMMENT_PULL = "comment_pull"
    PUBLISH_RELEASE = "publish_release"
    PULL_REVIEW_DISMISSED = "pull_review_dismissed"
    PULL_REQUEST_READY_FOR_REVIEW = "pull_request_ready_for_review"
    AUTO_MERGE_PULL_REQUEST = "auto_merge_pull_request"


class Activity(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    act_user: User | None = None
    act_user_id: int | None = None
    comment: Comment | None = None
    comment_id: int | None = None
    content: str | None = None
    created: datetime | None = None
    id: int | None = None
    is_private: bool | None = None
    op_type: ActivityOpType | None = Field(default=None, description="the type of action")
    ref_name: str | None = None
    repo: Repository | None = None
    repo_id: int | None = None
    user_id: int | None = None
