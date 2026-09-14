"""Generated from spec/openapi.json (TopicSearchResults). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict

from pyfj._generated.models.topic_response import TopicResponse


class TopicSearchResults(BaseModel):
    """TopicSearchResults"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    topics: list[TopicResponse] | None = None
