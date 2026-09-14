"""Generated from spec/openapi.json (SyncForkInfo). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class SyncForkInfo(BaseModel):
    """SyncForkInfo information about syncing a fork"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    allowed: bool | None = None
    base_commit: str | None = None
    commits_behind: int | None = None
    fork_commit: str | None = None
