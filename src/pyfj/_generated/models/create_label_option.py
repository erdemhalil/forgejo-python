"""Generated from spec/openapi.json (CreateLabelOption). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class CreateLabelOption(BaseModel):
    """CreateLabelOption options for creating a label"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    color: str
    description: str | None = None
    exclusive: bool | None = None
    is_archived: bool | None = None
    name: str
