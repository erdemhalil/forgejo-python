"""Generated from spec/openapi.json (IssueMeta). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class IssueMeta(BaseModel):
    """IssueMeta basic issue information"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    index: int
    owner: str
    repo: str
