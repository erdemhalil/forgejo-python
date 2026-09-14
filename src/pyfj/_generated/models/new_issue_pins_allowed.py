"""Generated from spec/openapi.json (NewIssuePinsAllowed). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class NewIssuePinsAllowed(BaseModel):
    """NewIssuePinsAllowed represents an API response that says if new Issue Pins are allowed"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    issues: bool | None = None
    pull_requests: bool | None = None
