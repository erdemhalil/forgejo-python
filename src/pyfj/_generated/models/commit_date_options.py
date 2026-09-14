"""Generated from spec/openapi.json (CommitDateOptions). Do not edit by hand."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict


class CommitDateOptions(BaseModel):
    """CommitDateOptions store dates for GIT_AUTHOR_DATE and GIT_COMMITTER_DATE"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    author: datetime | None = None
    committer: datetime | None = None
