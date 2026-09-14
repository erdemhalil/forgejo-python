"""Generated from spec/openapi.json (ActionArtifact). Do not edit by hand."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class ActionArtifact(BaseModel):
    """ActionArtifact represents an artifact of a workflow run"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    archive_download_url: str | None = Field(default=None, description="the URL to download the artifact zip archive")
    created_at: datetime | None = None
    expired: bool | None = Field(default=None, description="whether the artifact has expired")
    expires_at: datetime | None = None
    id: int | None = Field(default=None, description="the artifact's ID")
    name: str | None = Field(default=None, description="the artifact's name")
    run_id: int | None = Field(default=None, description="the ID of the workflow run that produced this artifact")
    size_in_bytes: int | None = Field(default=None, description="the total size of the artifact in bytes")
    updated_at: datetime | None = None
