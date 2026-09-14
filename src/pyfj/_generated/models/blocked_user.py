"""Generated from spec/openapi.json (BlockedUser). Do not edit by hand."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict


class BlockedUser(BaseModel):
    """BlockedUser represents a blocked user."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    block_id: int | None = None
    created_at: datetime | None = None
