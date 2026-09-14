"""Generated from spec/openapi.json (EditMilestoneOption). Do not edit by hand."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict


class EditMilestoneOption(BaseModel):
    """EditMilestoneOption options for editing a milestone"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    description: str | None = None
    due_on: datetime | None = None
    state: str | None = None
    title: str | None = None
