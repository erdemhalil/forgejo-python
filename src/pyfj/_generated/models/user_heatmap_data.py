"""Generated from spec/openapi.json (UserHeatmapData). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict

from pyfj._generated.models.time_stamp import TimeStamp


class UserHeatmapData(BaseModel):
    """UserHeatmapData represents the data needed to create a heatmap"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    contributions: int | None = None
    timestamp: TimeStamp | None = None
