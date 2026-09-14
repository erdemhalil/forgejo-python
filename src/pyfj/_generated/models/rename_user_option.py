"""Generated from spec/openapi.json (RenameUserOption). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class RenameUserOption(BaseModel):
    """RenameUserOption options when renaming a user"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    new_username: str = Field(
        description="New username for this user. This name cannot be in use yet by any other user."
    )
