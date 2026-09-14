"""Generated from spec/openapi.json (WikiPageMetaData). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict

from pyfj._generated.models.wiki_commit import WikiCommit


class WikiPageMetaData(BaseModel):
    """WikiPageMetaData wiki page meta information"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    html_url: str | None = None
    last_commit: WikiCommit | None = None
    sub_url: str | None = None
    title: str | None = None
