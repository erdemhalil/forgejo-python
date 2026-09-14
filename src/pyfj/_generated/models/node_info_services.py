"""Generated from spec/openapi.json (NodeInfoServices). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class NodeInfoServices(BaseModel):
    """NodeInfoServices contains the third party sites this server can connect to via their application API"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    inbound: list[str] | None = None
    outbound: list[str] | None = None
