"""Generated from spec/openapi.json (Secret). Do not edit by hand."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class Secret(BaseModel):
    """Secret represents a secret"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    created_at: datetime | None = None
    name: str | None = Field(default=None, description="the secret's name")
