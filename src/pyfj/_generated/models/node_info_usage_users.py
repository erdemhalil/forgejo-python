"""Generated from spec/openapi.json (NodeInfoUsageUsers). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class NodeInfoUsageUsers(BaseModel):
    """NodeInfoUsageUsers contains statistics about the users of this server"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    active_halfyear: int | None = Field(default=None, alias="activeHalfyear")
    active_month: int | None = Field(default=None, alias="activeMonth")
    total: int | None = None
