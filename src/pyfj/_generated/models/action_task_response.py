"""Generated from spec/openapi.json (ActionTaskResponse). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict

from pyfj._generated.models.action_task import ActionTask


class ActionTaskResponse(BaseModel):
    """ActionTaskResponse returns a ActionTask"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    total_count: int | None = None
    workflow_runs: list[ActionTask] | None = None
