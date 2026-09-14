"""Generated from spec/openapi.json (QuotaUsedSizeRepos). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class QuotaUsedSizeRepos(BaseModel):
    """QuotaUsedSizeRepos represents the size-based repository quota usage of a user"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    private: int | None = Field(default=None, description="Storage size of the user's private repositories")
    public: int | None = Field(default=None, description="Storage size of the user's public repositories")
