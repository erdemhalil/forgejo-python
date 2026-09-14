"""Generated from spec/openapi.json (Commit). Do not edit by hand."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict

from pyfj._generated.models.commit_affected_files import CommitAffectedFiles
from pyfj._generated.models.commit_meta import CommitMeta
from pyfj._generated.models.commit_stats import CommitStats
from pyfj._generated.models.repo_commit import RepoCommit
from pyfj._generated.models.user import User


class Commit(BaseModel):
    """Commit contains information generated from a Git commit."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    author: User | None = None
    commit: RepoCommit | None = None
    committer: User | None = None
    created: datetime | None = None
    files: list[CommitAffectedFiles] | None = None
    html_url: str | None = None
    parents: list[CommitMeta] | None = None
    sha: str | None = None
    stats: CommitStats | None = None
    url: str | None = None
