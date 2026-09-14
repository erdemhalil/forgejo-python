"""Generated from spec/openapi.json (CommitAffectedFiles). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class CommitAffectedFiles(BaseModel):
    """CommitAffectedFiles store information about files affected by the commit"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    filename: str | None = None
    status: str | None = None
