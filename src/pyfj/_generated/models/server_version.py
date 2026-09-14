"""Generated from spec/openapi.json (ServerVersion). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class ServerVersion(BaseModel):
    """ServerVersion wraps the version of the server"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    version: str | None = None
