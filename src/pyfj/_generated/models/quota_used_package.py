"""Generated from spec/openapi.json (QuotaUsedPackage). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class QuotaUsedPackage(BaseModel):
    """QuotaUsedPackage represents a package counting towards a user's quota"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    html_url: str | None = Field(default=None, description="HTML URL to the package version")
    name: str | None = Field(default=None, description="Name of the package")
    size: int | None = Field(default=None, description="Size of the package version")
    type: str | None = Field(default=None, description="Type of the package")
    version: str | None = Field(default=None, description="Version of the package")
