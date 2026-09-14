"""Generated from spec/openapi.json (Part). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class Part(BaseModel):
    """A widget part."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None = Field(default=None, description="Part name.")
