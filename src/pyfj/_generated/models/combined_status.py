"""Generated from spec/openapi.json (CombinedStatus). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict

from pyfj._generated.models.commit_status import CommitStatus
from pyfj._generated.models.commit_status_state import CommitStatusState
from pyfj._generated.models.repository import Repository


class CombinedStatus(BaseModel):
    """CombinedStatus holds the combined state of several statuses for a single commit"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    commit_url: str | None = None
    repository: Repository | None = None
    sha: str | None = None
    state: CommitStatusState | None = None
    statuses: list[CommitStatus] | None = None
    total_count: int | None = None
    url: str | None = None
