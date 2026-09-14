"""Generated from spec/openapi.json (NodeInfoUsage). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

from pyfj._generated.models.node_info_usage_users import NodeInfoUsageUsers


class NodeInfoUsage(BaseModel):
    """NodeInfoUsage contains usage statistics for this server"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    local_comments: int | None = Field(default=None, alias="localComments")
    local_posts: int | None = Field(default=None, alias="localPosts")
    users: NodeInfoUsageUsers | None = None
