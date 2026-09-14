"""Generated from spec/openapi.json (CreatePushMirrorOption). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class CreatePushMirrorOption(BaseModel):
    """CreatePushMirrorOption represents need information to create a push mirror of a repository."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    branch_filter: str | None = None
    interval: str | None = None
    remote_address: str | None = None
    remote_password: str | None = None
    remote_username: str | None = None
    sync_on_commit: bool | None = None
    use_ssh: bool | None = None
