"""Generated from spec/openapi.json (Comment). Do not edit by hand."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from pyfj._generated.models.attachment import Attachment
from pyfj._generated.models.user import User


class Comment(BaseModel):
    """Comment represents a comment on a commit or issue"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    assets: list[Attachment] | None = Field(default=None, description="The attachments to the comment")
    body: str | None = Field(default=None, description="The body of the comment")
    created_at: datetime | None = Field(default=None, description="The time of the comment's creation")
    html_url: str | None = Field(default=None, description="The HTML URL of the comment")
    id: int | None = Field(default=None, description="The identifier of the comment")
    issue_url: str | None = Field(
        default=None, description="The HTML URL of the issue if the comment is posted on an issue, else empty string"
    )
    original_author: str | None = Field(
        default=None,
        description="The original author that posted the comment if it was not posted locally, else empty string",
    )
    original_author_id: int | None = Field(
        default=None,
        description="The ID of the original author that posted the comment if it was not posted locally, else 0",
    )
    pull_request_url: str | None = Field(
        default=None,
        description="The HTML URL of the pull request if the comment is posted on a pull request, else empty string",
    )
    updated_at: datetime | None = Field(default=None, description="The time of the comment's update")
    user: User | None = None
