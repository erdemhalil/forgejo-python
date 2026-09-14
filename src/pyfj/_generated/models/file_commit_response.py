"""Generated from spec/openapi.json (FileCommitResponse). Do not edit by hand."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict

from pyfj._generated.models.commit_meta import CommitMeta
from pyfj._generated.models.commit_user import CommitUser


class FileCommitResponse(BaseModel):
    """FileCommitResponse contains information generated from a Git commit for a repo's file."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    author: CommitUser | None = None
    committer: CommitUser | None = None
    created: datetime | None = None
    html_url: str | None = None
    message: str | None = None
    parents: list[CommitMeta] | None = None
    sha: str | None = None
    tree: CommitMeta | None = None
    url: str | None = None
