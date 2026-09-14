"""Generated from spec/openapi.json (NodeInfoSoftware). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class NodeInfoSoftware(BaseModel):
    """NodeInfoSoftware contains Metadata about server software in use"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    homepage: str | None = None
    name: str | None = None
    repository: str | None = None
    version: str | None = None
