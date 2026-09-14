"""Generated from spec/openapi.json (WikiCommitList). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict

from pyfj._generated.models.wiki_commit import WikiCommit


class WikiCommitList(BaseModel):
    """WikiCommitList commit/revision list"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    commits: list[WikiCommit] | None = None
    count: int | None = None
