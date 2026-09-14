"""Generated from spec/openapi.json (WikiPage). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

from pyfj._generated.models.wiki_commit import WikiCommit


class WikiPage(BaseModel):
    """WikiPage a wiki page"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    commit_count: int | None = None
    content_base64: str | None = Field(default=None, description="Page content, base64 encoded")
    footer: str | None = None
    html_url: str | None = None
    last_commit: WikiCommit | None = None
    sidebar: str | None = None
    sub_url: str | None = None
    title: str | None = None
