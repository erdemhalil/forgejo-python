"""Generated from spec/openapi.json (LabelTemplate). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class LabelTemplate(BaseModel):
    """LabelTemplate info of a Label template"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    color: str | None = None
    description: str | None = None
    exclusive: bool | None = None
    name: str | None = None
