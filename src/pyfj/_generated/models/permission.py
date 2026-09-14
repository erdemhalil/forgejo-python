"""Generated from spec/openapi.json (Permission). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class Permission(BaseModel):
    """Permission represents a set of permissions"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    admin: bool | None = None
    pull: bool | None = None
    push: bool | None = None
