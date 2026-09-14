"""Generated from spec/openapi.json (CreateWikiPageOptions). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class CreateWikiPageOptions(BaseModel):
    """CreateWikiPageOptions form for creating wiki"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    content_base64: str | None = Field(default=None, description="content must be base64 encoded")
    message: str | None = Field(default=None, description="optional commit message summarizing the change")
    title: str | None = Field(default=None, description="page title. leave empty to keep unchanged")
