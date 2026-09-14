"""Generated from spec/openapi.json (APIInternalServerError). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class APIInternalServerError(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    message: str | None = None
    url: str | None = None
