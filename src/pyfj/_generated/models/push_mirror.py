"""Generated from spec/openapi.json (PushMirror). Do not edit by hand."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict


class PushMirror(BaseModel):
    """PushMirror represents information of a push mirror"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    branch_filter: str | None = None
    created: datetime | None = None
    interval: str | None = None
    last_error: str | None = None
    last_update: datetime | None = None
    public_key: str | None = None
    remote_address: str | None = None
    remote_name: str | None = None
    repo_name: str | None = None
    sync_on_commit: bool | None = None
