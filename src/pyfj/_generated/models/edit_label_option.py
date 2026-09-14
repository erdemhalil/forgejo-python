"""Generated from spec/openapi.json (EditLabelOption). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class EditLabelOption(BaseModel):
    """EditLabelOption options for editing a label"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    color: str | None = None
    description: str | None = None
    exclusive: bool | None = None
    is_archived: bool | None = None
    name: str | None = None
