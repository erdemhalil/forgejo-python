"""Generated from spec/openapi.json (CreateStatusOption). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict

from pyfj._generated.models.commit_status_state import CommitStatusState


class CreateStatusOption(BaseModel):
    """CreateStatusOption holds the information needed to create a new CommitStatus for a Commit"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    context: str | None = None
    description: str | None = None
    state: CommitStatusState | None = None
    target_url: str | None = None
