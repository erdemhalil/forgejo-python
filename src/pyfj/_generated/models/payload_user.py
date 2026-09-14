"""Generated from spec/openapi.json (PayloadUser). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class PayloadUser(BaseModel):
    """PayloadUser represents the author or committer of a commit"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    email: str | None = None
    name: str | None = Field(default=None, description="Full name of the commit author")
    username: str | None = None
