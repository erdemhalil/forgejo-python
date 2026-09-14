"""Generated from spec/openapi.json (Owner). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class Owner(BaseModel):
    """A widget owner."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    login: str | None = Field(default=None, description="Login name.")
