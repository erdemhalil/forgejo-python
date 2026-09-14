"""Generated from spec/openapi.json (CreateHookOptionConfig). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class CreateHookOptionConfig(BaseModel):
    """CreateHookOptionConfig has all config options in it required are "content_type" and "url" Required"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)
