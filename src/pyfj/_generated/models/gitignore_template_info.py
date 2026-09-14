"""Generated from spec/openapi.json (GitignoreTemplateInfo). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class GitignoreTemplateInfo(BaseModel):
    """GitignoreTemplateInfo name and text of a gitignore template"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None = None
    source: str | None = None
