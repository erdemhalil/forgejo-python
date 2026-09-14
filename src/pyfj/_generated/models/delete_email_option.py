"""Generated from spec/openapi.json (DeleteEmailOption). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class DeleteEmailOption(BaseModel):
    """DeleteEmailOption options when deleting email addresses"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    emails: list[str] | None = Field(default=None, description="email addresses to delete")
