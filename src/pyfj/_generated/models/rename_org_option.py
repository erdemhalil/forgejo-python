"""Generated from spec/openapi.json (RenameOrgOption). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class RenameOrgOption(BaseModel):
    """RenameOrgOption options when renaming an organization"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    new_name: str = Field(description="New username for this org. This name cannot be in use yet by any other user.")
