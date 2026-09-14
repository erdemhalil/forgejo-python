"""Generated from spec/openapi.json (QuotaInfo). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict

from pyfj._generated.models.quota_group_list import QuotaGroupList
from pyfj._generated.models.quota_used import QuotaUsed


class QuotaInfo(BaseModel):
    """QuotaInfo represents information about a user's quota"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    groups: QuotaGroupList | None = None
    used: QuotaUsed | None = None
