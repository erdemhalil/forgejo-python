"""Generated from spec/openapi.json (MarkdownOption). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class MarkdownOption(BaseModel):
    """MarkdownOption markdown options"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    context: str | None = Field(default=None, alias="Context", description="Context to render")
    mode: str | None = Field(default=None, alias="Mode", description="Mode to render (comment, gfm, markdown)")
    text: str | None = Field(default=None, alias="Text", description="Text markdown to render")
    wiki: bool | None = Field(default=None, alias="Wiki", description="Is it a wiki page ?")
