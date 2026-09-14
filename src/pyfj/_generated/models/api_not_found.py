"""Generated from spec/openapi.json (APINotFound). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class APINotFound(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    errors: list[str] | None = None
    message: str | None = None
    url: str | None = None
