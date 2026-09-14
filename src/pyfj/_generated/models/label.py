"""Generated from spec/openapi.json (Label). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class Label(BaseModel):
    """Label a label to an issue or a pr"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    color: str | None = None
    description: str | None = None
    exclusive: bool | None = None
    id: int | None = None
    is_archived: bool | None = None
    name: str | None = None
    url: str | None = None
