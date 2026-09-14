"""Generated from spec/openapi.json (NodeInfo). Do not edit by hand."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, ConfigDict, Field

from pyfj._generated.models.node_info_services import NodeInfoServices
from pyfj._generated.models.node_info_software import NodeInfoSoftware
from pyfj._generated.models.node_info_usage import NodeInfoUsage


class NodeInfo(BaseModel):
    """NodeInfo contains standardized way of exposing metadata about a server running one of the distributed
    social networks
    """

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    metadata: dict[str, Any] | None = None
    open_registrations: bool | None = Field(default=None, alias="openRegistrations")
    protocols: list[str] | None = None
    services: NodeInfoServices | None = None
    software: NodeInfoSoftware | None = None
    usage: NodeInfoUsage | None = None
    version: str | None = None
