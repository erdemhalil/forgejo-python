"""Generated from spec/openapi.json (RepoCommit). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict

from pyfj._generated.models.commit_meta import CommitMeta
from pyfj._generated.models.commit_user import CommitUser
from pyfj._generated.models.payload_commit_verification import PayloadCommitVerification


class RepoCommit(BaseModel):
    """RepoCommit contains information of a commit in the context of a repository."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    author: CommitUser | None = None
    committer: CommitUser | None = None
    message: str | None = None
    tree: CommitMeta | None = None
    url: str | None = None
    verification: PayloadCommitVerification | None = None
