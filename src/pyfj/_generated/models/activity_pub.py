"""Generated from spec/openapi.json (ActivityPub). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class ActivityPub(BaseModel):
    """ActivityPub type"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    context: str | None = Field(default=None, alias="@context")
