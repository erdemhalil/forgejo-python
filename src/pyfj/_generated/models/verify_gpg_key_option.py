"""Generated from spec/openapi.json (VerifyGPGKeyOption). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class VerifyGPGKeyOption(BaseModel):
    """VerifyGPGKeyOption options verifies user GPG key"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    armored_signature: str | None = None
    key_id: str = Field(description="An Signature for a GPG key token")
