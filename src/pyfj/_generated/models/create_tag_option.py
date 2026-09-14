"""Generated from spec/openapi.json (CreateTagOption). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class CreateTagOption(BaseModel):
    """CreateTagOption options when creating a tag"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    message: str | None = None
    tag_name: str
    target: str | None = None
