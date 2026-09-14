"""Generated from spec/openapi.json (Config). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class Config(BaseModel):
    """Free-form config."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)
