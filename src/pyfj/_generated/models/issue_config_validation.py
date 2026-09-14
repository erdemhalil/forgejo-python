"""Generated from spec/openapi.json (IssueConfigValidation). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class IssueConfigValidation(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    message: str | None = None
    valid: bool | None = None
