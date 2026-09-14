"""Generated from spec/openapi.json (Compare). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict

from pyfj._generated.models.commit import Commit
from pyfj._generated.models.commit_affected_files import CommitAffectedFiles


class Compare(BaseModel):
    """Compare represents a comparison between two commits."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    commits: list[Commit] | None = None
    files: list[CommitAffectedFiles] | None = None
    total_commits: int | None = None
