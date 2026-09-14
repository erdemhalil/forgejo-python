"""Generated from spec/openapi.json (APIValidationError). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class APIValidationError(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    message: str | None = None
    url: str | None = None
