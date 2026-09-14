"""Generated from spec/openapi.json (EditQuotaRuleOptions). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class EditQuotaRuleOptions(BaseModel):
    """EditQuotaRuleOptions represents the options for editing a quota rule"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    limit: int | None = Field(default=None, description="The limit set by the rule")
    subjects: list[str] | None = Field(default=None, description="The subjects affected by the rule")
