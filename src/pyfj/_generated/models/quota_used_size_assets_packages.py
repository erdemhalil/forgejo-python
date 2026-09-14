"""Generated from spec/openapi.json (QuotaUsedSizeAssetsPackages). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class QuotaUsedSizeAssetsPackages(BaseModel):
    """QuotaUsedSizeAssetsPackages represents the size-based package quota usage of a user"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    all: int | None = Field(default=None, description="Storage suze used for the user's packages")
