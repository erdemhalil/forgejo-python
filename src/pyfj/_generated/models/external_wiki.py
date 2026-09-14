"""Generated from spec/openapi.json (ExternalWiki). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class ExternalWiki(BaseModel):
    """ExternalWiki represents setting for external wiki"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    external_wiki_url: str | None = Field(default=None, description="URL of external wiki.")
