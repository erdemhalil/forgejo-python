"""Generated from spec/openapi.json (RepoTargetOption). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class RepoTargetOption(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str = Field(description="Name of repository")
    owner: str = Field(description="Name of user or organisation that owns the repository")
