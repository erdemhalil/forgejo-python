"""Generated from spec/openapi.json (WidgetSearchResults). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict

from pyfj._generated.models.widget import Widget


class WidgetSearchResults(BaseModel):
    """WidgetSearchResults"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    items: list[Widget] | None = None
    total: int | None = None
