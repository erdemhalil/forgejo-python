"""Generated from spec/openapi.json (CreateQuotaGroupOptions). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

from pyfj._generated.models.create_quota_rule_options import CreateQuotaRuleOptions


class CreateQuotaGroupOptions(BaseModel):
    """CreateQutaGroupOptions represents the options for creating a quota group"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None = Field(default=None, description="Name of the quota group to create")
    rules: list[CreateQuotaRuleOptions] | None = Field(
        default=None,
        description="Rules to add to the newly created group. If a rule does not exist, it will be created.",
    )
