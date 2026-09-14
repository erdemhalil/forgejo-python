"""Generated from spec/openapi.json (QuotaUsedSizeGit). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class QuotaUsedSizeGit(BaseModel):
    """QuotaUsedSizeGit represents the size-based git (lfs) quota usage of a user"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    lfs: int | None = Field(default=None, alias="LFS", description="Storage size of the user's Git LFS objects")
