"""Generated from spec/openapi.json (WikiCommit). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict

from pyfj._generated.models.commit_user import CommitUser


class WikiCommit(BaseModel):
    """WikiCommit page commit/revision"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    author: CommitUser | None = None
    commiter: CommitUser | None = None
    message: str | None = None
    sha: str | None = None
