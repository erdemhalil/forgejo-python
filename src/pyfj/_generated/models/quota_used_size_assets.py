"""Generated from spec/openapi.json (QuotaUsedSizeAssets). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

from pyfj._generated.models.quota_used_size_assets_attachments import QuotaUsedSizeAssetsAttachments
from pyfj._generated.models.quota_used_size_assets_packages import QuotaUsedSizeAssetsPackages


class QuotaUsedSizeAssets(BaseModel):
    """QuotaUsedSizeAssets represents the size-based asset usage of a user"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    artifacts: int | None = Field(default=None, description="Storage size used for the user's artifacts")
    attachments: QuotaUsedSizeAssetsAttachments | None = None
    packages: QuotaUsedSizeAssetsPackages | None = None
