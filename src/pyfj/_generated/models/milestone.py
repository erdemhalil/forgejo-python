"""Generated from spec/openapi.json (Milestone). Do not edit by hand."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict

from pyfj._generated.models.state_type import StateType


class Milestone(BaseModel):
    """Milestone milestone is a collection of issues on one repository"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    closed_at: datetime | None = None
    closed_issues: int | None = None
    created_at: datetime | None = None
    description: str | None = None
    due_on: datetime | None = None
    id: int | None = None
    open_issues: int | None = None
    state: StateType | None = None
    title: str | None = None
    updated_at: datetime | None = None
