"""Generated from spec/openapi.json (APIError). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class APIError(BaseModel):
    """APIError is an api error with a message"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    message: str | None = None
    url: str | None = None
