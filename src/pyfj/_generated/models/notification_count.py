"""Generated from spec/openapi.json (NotificationCount). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class NotificationCount(BaseModel):
    """NotificationCount number of unread notifications"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    new: int | None = None
