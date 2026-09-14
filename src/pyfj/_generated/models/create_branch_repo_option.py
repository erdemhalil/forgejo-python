"""Generated from spec/openapi.json (CreateBranchRepoOption). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class CreateBranchRepoOption(BaseModel):
    """CreateBranchRepoOption options when creating a branch in a repository"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    new_branch_name: str = Field(description="Name of the branch to create")
    old_branch_name: str | None = Field(
        default=None, description="Deprecated: true Name of the old branch to create from"
    )
    old_ref_name: str | None = Field(default=None, description="Name of the old branch/tag/commit to create from")
