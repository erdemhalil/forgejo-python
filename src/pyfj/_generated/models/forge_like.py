"""Generated from spec/openapi.json (ForgeLike). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class ForgeLike(BaseModel):
    """ForgeLike activity data type"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)
