"""Generated from spec/openapi.json (EmptyModel). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class EmptyModel(BaseModel):
    """An object with no declared properties."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)
