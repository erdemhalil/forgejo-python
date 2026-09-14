"""Generated from spec/openapi.json (GitHook). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class GitHook(BaseModel):
    """GitHook represents a Git repository hook"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    content: str | None = None
    is_active: bool | None = None
    name: str | None = None
