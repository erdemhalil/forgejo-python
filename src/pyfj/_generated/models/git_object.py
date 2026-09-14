"""Generated from spec/openapi.json (GitObject). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class GitObject(BaseModel):
    """GitObject represents a Git object."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    sha: str | None = None
    type: str | None = None
    url: str | None = None
