"""Generated from spec/openapi.json (Branch). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict

from pyfj._generated.models.payload_commit import PayloadCommit


class Branch(BaseModel):
    """Branch represents a repository branch"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    commit: PayloadCommit | None = None
    effective_branch_protection_name: str | None = None
    enable_status_check: bool | None = None
    name: str | None = None
    protected: bool | None = None
    required_approvals: int | None = None
    status_check_contexts: list[str] | None = None
    user_can_merge: bool | None = None
    user_can_push: bool | None = None
