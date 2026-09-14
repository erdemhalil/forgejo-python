"""Generated from spec/openapi.json (PayloadCommitVerification). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict

from pyfj._generated.models.payload_user import PayloadUser


class PayloadCommitVerification(BaseModel):
    """PayloadCommitVerification represents the GPG verification of a commit"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    payload: str | None = None
    reason: str | None = None
    signature: str | None = None
    signer: PayloadUser | None = None
    verified: bool | None = None
