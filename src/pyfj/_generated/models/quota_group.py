"""Generated from spec/openapi.json (QuotaGroup). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

from pyfj._generated.models.quota_rule_info import QuotaRuleInfo


class QuotaGroup(BaseModel):
    """QuotaGroup represents a quota group"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None = Field(default=None, description="Name of the group")
    rules: list[QuotaRuleInfo] | None = Field(default=None, description="Rules associated with the group")
