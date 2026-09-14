"""Generated from spec/openapi.json (CreateMilestoneOption). Do not edit by hand."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum

from pydantic import BaseModel, ConfigDict


class CreateMilestoneOptionState(StrEnum):
    OPEN = "open"
    CLOSED = "closed"


class CreateMilestoneOption(BaseModel):
    """CreateMilestoneOption options for creating a milestone"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    description: str | None = None
    due_on: datetime | None = None
    state: CreateMilestoneOptionState | None = None
    title: str | None = None
