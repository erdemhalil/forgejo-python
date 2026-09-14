"""Generated from spec/openapi.json (FileLinksResponse). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class FileLinksResponse(BaseModel):
    """FileLinksResponse contains the links for a repo's file"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    git: str | None = None
    html: str | None = None
    self: str | None = None
