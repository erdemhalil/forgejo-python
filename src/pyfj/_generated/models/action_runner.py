"""Generated from spec/openapi.json (ActionRunner). Do not edit by hand."""

from __future__ import annotations

from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field


class ActionRunnerStatus(StrEnum):
    """Status indicates whether this runner is offline, or active, for example."""

    OFFLINE = "offline"
    IDLE = "idle"
    ACTIVE = "active"


class ActionRunner(BaseModel):
    """ActionRunner represents a runner"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    description: str | None = Field(
        default=None, description="Description provides optional details about this runner."
    )
    ephemeral: bool | None = Field(default=None, description="Indicates if runner is ephemeral runner")
    id: int | None = Field(default=None, description="ID uniquely identifies this runner.")
    labels: list[str] | None = Field(default=None, description="Labels is a list of labels attached to this runner.")
    name: str | None = Field(default=None, description="Name of the runner; not unique.")
    owner_id: int | None = Field(
        default=None,
        description=(
            "OwnerID is the identifier of the user or organization this runner belongs to. O if the runner is "
            "owned by a repository."
        ),
    )
    repo_id: int | None = Field(
        default=None,
        description=(
            "RepoID is the identifier of the repository this runner belongs to. 0 if the runner belongs to a user"
            " or organization."
        ),
    )
    status: ActionRunnerStatus | None = Field(
        default=None, description="Status indicates whether this runner is offline, or active, for example."
    )
    uuid: str | None = Field(default=None, description="UUID uniquely identifies this runner.")
    version: str | None = Field(
        default=None, description="Version is the self-reported version string of Forgejo Runner."
    )
