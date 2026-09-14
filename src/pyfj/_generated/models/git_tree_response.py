"""Generated from spec/openapi.json (GitTreeResponse). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict

from pyfj._generated.models.git_entry import GitEntry


class GitTreeResponse(BaseModel):
    """GitTreeResponse returns a git tree"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    page: int | None = None
    sha: str | None = None
    total_count: int | None = None
    tree: list[GitEntry] | None = None
    truncated: bool | None = None
    url: str | None = None
