"""Generated from spec/openapi.json (AnnotatedTagObject). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class AnnotatedTagObject(BaseModel):
    """AnnotatedTagObject contains meta information of the tag object"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    sha: str | None = None
    type: str | None = None
    url: str | None = None
