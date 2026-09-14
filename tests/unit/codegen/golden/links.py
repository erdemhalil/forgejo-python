"""Generated from spec/openapi.json (Links). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class Links(BaseModel):
    """Links to related resources."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    self: str | None = Field(default=None, description="Canonical URL.")
