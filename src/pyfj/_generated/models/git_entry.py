"""Generated from spec/openapi.json (GitEntry). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class GitEntry(BaseModel):
    """GitEntry represents a git tree"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    mode: str | None = None
    path: str | None = None
    sha: str | None = None
    size: int | None = None
    type: str | None = None
    url: str | None = None
