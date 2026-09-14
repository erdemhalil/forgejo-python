"""Generated from spec/openapi.json (CreateQuotaRuleOptions). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class CreateQuotaRuleOptions(BaseModel):
    """CreateQuotaRuleOptions represents the options for creating a quota rule"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    limit: int | None = Field(default=None, description="The limit set by the rule")
    name: str | None = Field(default=None, description="Name of the rule to create")
    subjects: list[str] | None = Field(default=None, description="The subjects affected by the rule")
