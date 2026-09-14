"""Generated from spec/openapi.json (QuotaUsedSizeAssetsAttachments). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class QuotaUsedSizeAssetsAttachments(BaseModel):
    """QuotaUsedSizeAssetsAttachments represents the size-based attachment quota usage of a user"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    issues: int | None = Field(default=None, description="Storage size used for the user's issue & comment attachments")
    releases: int | None = Field(default=None, description="Storage size used for the user's release attachments")
