"""Generated from spec/openapi.json (EditDeadlineOption). Do not edit by hand."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict


class EditDeadlineOption(BaseModel):
    """EditDeadlineOption options for creating a deadline"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    due_date: datetime
