"""Generated from spec/openapi.json (DispatchWorkflowOption). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class DispatchWorkflowOption(BaseModel):
    """DispatchWorkflowOption options when dispatching a workflow"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    inputs: dict[str, str] | None = Field(
        default=None, description="Input keys and values configured in the workflow file."
    )
    ref: str = Field(description="Git reference for the workflow")
    return_run_info: bool | None = Field(default=None, description="Flag to return the run info")
