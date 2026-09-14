"""Generated from spec/openapi.json (APIInvalidTopicsError). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class APIInvalidTopicsError(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    invalid_topics: list[str] | None = Field(default=None, alias="invalidTopics")
    message: str | None = None
