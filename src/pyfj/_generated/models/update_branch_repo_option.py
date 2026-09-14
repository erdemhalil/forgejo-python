"""Generated from spec/openapi.json (UpdateBranchRepoOption). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class UpdateBranchRepoOption(BaseModel):
    """UpdateBranchRepoOption options when updating a branch in a repository"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str = Field(description="New branch name")
