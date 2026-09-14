"""Generated from spec/openapi.json (PullRequestMeta). Do not edit by hand."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict


class PullRequestMeta(BaseModel):
    """PullRequestMeta PR info if an issue is a PR"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    draft: bool | None = None
    html_url: str | None = None
    merged: bool | None = None
    merged_at: datetime | None = None
