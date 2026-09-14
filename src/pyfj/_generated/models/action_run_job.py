"""Generated from spec/openapi.json (ActionRunJob). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class ActionRunJob(BaseModel):
    """ActionRunJob represents a job of a run"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    attempt: int | None = Field(
        default=None, description="How many times the job has been attempted including the current attempt."
    )
    handle: str | None = Field(
        default=None, description="Opaque identifier that uniquely identifies a single attempt of a job."
    )
    id: int | None = Field(default=None, description="Identifier of this job.")
    name: str | None = Field(default=None, description="the action run job name")
    needs: list[str] | None = Field(default=None, description="the action run job needed ids")
    owner_id: int | None = Field(default=None, description="the owner id")
    repo_id: int | None = Field(default=None, description="the repository id")
    run_id: int | None = Field(default=None, description="Identifier of the workflow run this job belongs to.")
    runs_on: list[str] | None = Field(default=None, description="the action run job labels to run on")
    status: str | None = Field(default=None, description="the action run job status")
    task_id: int | None = Field(default=None, description="the action run job latest task id")
