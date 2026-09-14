"""Generated from spec/openapi.json (ActionRun). Do not edit by hand."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from pyfj._generated.models.duration import Duration
from pyfj._generated.models.repository import Repository
from pyfj._generated.models.user import User


class ActionRun(BaseModel):
    """ActionRun represents an action run"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    schedule_id: int | None = Field(
        default=None, alias="ScheduleID", description="the cron id for the schedule trigger"
    )
    approved_by: int | None = Field(default=None, description="who approved this action run")
    commit_sha: str | None = Field(default=None, description="the commit sha the action run ran on")
    created: datetime | None = Field(default=None, description="when the action run was created")
    duration: Duration | None = None
    event: str | None = Field(default=None, description="the webhook event that causes the workflow to run")
    event_payload: str | None = Field(
        default=None, description="the payload of the webhook event that causes the workflow to run"
    )
    html_url: str | None = Field(default=None, description="the url of this action run")
    id: int | None = Field(default=None, description="the action run id")
    index_in_repo: int | None = Field(default=None, description="a unique number for each run of a repository")
    is_fork_pull_request: bool | None = Field(
        default=None,
        description=(
            "If this is triggered by a PR from a forked repository or an untrusted user, we need to check if it "
            "is approved and limit permissions when running the workflow."
        ),
    )
    is_ref_deleted: bool | None = Field(
        default=None, description="has the commit/tag/… the action run ran on been deleted"
    )
    need_approval: bool | None = Field(default=None, description="may need approval if it's a fork pull request")
    prettyref: str | None = Field(default=None, description="the commit/tag/… the action run ran on")
    repository: Repository | None = None
    started: datetime | None = Field(default=None, description="when the action run was started")
    status: str | None = Field(default=None, description="the current status of this run")
    stopped: datetime | None = Field(default=None, description="when the action run was stopped")
    title: str | None = Field(default=None, description="the action run's title")
    trigger_event: str | None = Field(
        default=None, description="the trigger event defined in the `on` configuration of the triggered workflow"
    )
    trigger_user: User | None = None
    updated: datetime | None = Field(default=None, description="when the action run was last updated")
    workflow_id: str | None = Field(default=None, description="the name of workflow file")
