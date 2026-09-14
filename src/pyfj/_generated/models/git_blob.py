"""Generated from spec/openapi.json (GitBlob). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class GitBlob(BaseModel):
    """GitBlob represents a git blob"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    content: str | None = None
    encoding: str | None = None
    sha: str | None = None
    size: int | None = None
    url: str | None = None
