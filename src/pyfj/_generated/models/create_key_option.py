"""Generated from spec/openapi.json (CreateKeyOption). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class CreateKeyOption(BaseModel):
    """CreateKeyOption options when creating a key"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    key: str = Field(description="An armored SSH key to add")
    read_only: bool | None = Field(default=None, description="Describe if the key has only read access or read/write")
    title: str = Field(description="Title of the key to add")
