"""Generated from spec/openapi.json (IssueDeadline). Do not edit by hand."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict


class IssueDeadline(BaseModel):
    """IssueDeadline represents an issue deadline"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    due_date: datetime | None = None
