"""Generated from spec/openapi.json (ChangedFile). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class ChangedFile(BaseModel):
    """ChangedFile store information about files affected by the pull request"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    additions: int | None = None
    changes: int | None = None
    contents_url: str | None = None
    deletions: int | None = None
    filename: str | None = None
    html_url: str | None = None
    previous_filename: str | None = None
    raw_url: str | None = None
    status: str | None = None
