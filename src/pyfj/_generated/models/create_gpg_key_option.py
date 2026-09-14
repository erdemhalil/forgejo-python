"""Generated from spec/openapi.json (CreateGPGKeyOption). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class CreateGPGKeyOption(BaseModel):
    """CreateGPGKeyOption options create user GPG key"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    armored_public_key: str = Field(description="An armored GPG key to add")
    armored_signature: str | None = None
