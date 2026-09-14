"""Generated from spec/openapi.json (QuotaRuleInfo). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class QuotaRuleInfo(BaseModel):
    """QuotaRuleInfo contains information about a quota rule"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    limit: int | None = Field(default=None, description="The limit set by the rule")
    name: str | None = Field(default=None, description="Name of the rule (only shown to admins)")
    subjects: list[str] | None = Field(default=None, description="Subjects the rule affects")
