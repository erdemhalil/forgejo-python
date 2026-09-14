"""Generated from spec/openapi.json (CommitStatus). Do not edit by hand."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict

from pyfj._generated.models.commit_status_state import CommitStatusState
from pyfj._generated.models.user import User


class CommitStatus(BaseModel):
    """CommitStatus holds a single status of a single Commit"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    context: str | None = None
    created_at: datetime | None = None
    creator: User | None = None
    description: str | None = None
    id: int | None = None
    status: CommitStatusState | None = None
    target_url: str | None = None
    updated_at: datetime | None = None
    url: str | None = None
