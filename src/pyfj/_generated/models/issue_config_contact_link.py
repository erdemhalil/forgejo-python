"""Generated from spec/openapi.json (IssueConfigContactLink). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class IssueConfigContactLink(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    about: str | None = None
    name: str | None = None
    url: str | None = None
