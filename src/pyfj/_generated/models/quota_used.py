"""Generated from spec/openapi.json (QuotaUsed). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict

from pyfj._generated.models.quota_used_size import QuotaUsedSize


class QuotaUsed(BaseModel):
    """QuotaUsed represents the quota usage of a user"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    size: QuotaUsedSize | None = None
