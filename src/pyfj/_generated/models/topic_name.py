"""Generated from spec/openapi.json (TopicName). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class TopicName(BaseModel):
    """TopicName a list of repo topic names"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    topics: list[str] | None = None
