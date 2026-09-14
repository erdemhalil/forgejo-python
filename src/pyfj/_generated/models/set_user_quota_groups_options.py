"""Generated from spec/openapi.json (SetUserQuotaGroupsOptions). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class SetUserQuotaGroupsOptions(BaseModel):
    """SetUserQuotaGroupsOptions represents the quota groups of a user"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    groups: list[str] = Field(description="Quota groups the user shall have")
