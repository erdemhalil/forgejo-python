"""Generated from spec/openapi.json (Cron). Do not edit by hand."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict


class Cron(BaseModel):
    """Cron represents a Cron task"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    exec_times: int | None = None
    name: str | None = None
    next: datetime | None = None
    prev: datetime | None = None
    schedule: str | None = None
