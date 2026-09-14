"""Generated from spec/openapi.json (WatchInfo). Do not edit by hand."""

from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict


class WatchInfo(BaseModel):
    """WatchInfo represents an API watch status of one repository"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    created_at: datetime | None = None
    ignored: bool | None = None
    reason: Any | None = None
    repository_url: str | None = None
    subscribed: bool | None = None
    url: str | None = None
