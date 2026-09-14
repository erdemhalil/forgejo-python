"""Generated from spec/openapi.json (DispatchWorkflowRun). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class DispatchWorkflowRun(BaseModel):
    """DispatchWorkflowRun represents a workflow run"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int | None = Field(default=None, description="the workflow run id")
    jobs: list[str] | None = Field(default=None, description="the jobs name")
    run_number: int | None = Field(default=None, description="a unique number for each run of a repository")
