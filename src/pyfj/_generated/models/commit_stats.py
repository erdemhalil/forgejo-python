"""Generated from spec/openapi.json (CommitStats). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class CommitStats(BaseModel):
    """CommitStats is statistics for a RepoCommit"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    additions: int | None = None
    deletions: int | None = None
    total: int | None = None
