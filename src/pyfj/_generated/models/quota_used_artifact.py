"""Generated from spec/openapi.json (QuotaUsedArtifact). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class QuotaUsedArtifact(BaseModel):
    """QuotaUsedArtifact represents an artifact counting towards a user's quota"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    html_url: str | None = Field(default=None, description="HTML URL to the action run containing the artifact")
    name: str | None = Field(default=None, description="Name of the artifact")
    size: int | None = Field(default=None, description="Size of the artifact (compressed)")
