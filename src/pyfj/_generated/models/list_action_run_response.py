"""Generated from spec/openapi.json (ListActionRunResponse). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict

from pyfj._generated.models.action_run import ActionRun


class ListActionRunResponse(BaseModel):
    """ListActionRunResponse return a list of ActionRun"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    total_count: int | None = None
    workflow_runs: list[ActionRun] | None = None
