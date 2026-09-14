"""Generated from spec/openapi.json (CommitMeta). Do not edit by hand."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict


class CommitMeta(BaseModel):
    """CommitMeta contains meta information of a commit in terms of API."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    created: datetime | None = None
    sha: str | None = None
    url: str | None = None
