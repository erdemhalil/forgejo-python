"""Generated from spec/openapi.json (AddTimeOption). Do not edit by hand."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class AddTimeOption(BaseModel):
    """AddTimeOption options for adding time to an issue"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    created: datetime | None = None
    time: int = Field(description="time in seconds")
    user_name: str | None = Field(default=None, description="User who spent the time (optional)")
