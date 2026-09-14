"""Generated from spec/openapi.json (TopicResponse). Do not edit by hand."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict


class TopicResponse(BaseModel):
    """TopicResponse for returning topics"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    created: datetime | None = None
    id: int | None = None
    repo_count: int | None = None
    topic_name: str | None = None
    updated: datetime | None = None
