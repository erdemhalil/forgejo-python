"""Generated from spec/openapi.json (RepoTopicOptions). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class RepoTopicOptions(BaseModel):
    """RepoTopicOptions a collection of repo topic names"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    topics: list[str] | None = Field(default=None, description="list of topic names")
