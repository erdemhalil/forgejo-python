"""Generated from spec/openapi.json (APRemoteFollowOption). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class APRemoteFollowOption(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    target: str | None = None
