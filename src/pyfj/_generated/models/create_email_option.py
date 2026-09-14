"""Generated from spec/openapi.json (CreateEmailOption). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class CreateEmailOption(BaseModel):
    """CreateEmailOption options when creating email addresses"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    emails: list[str] | None = Field(default=None, description="email addresses to add")
