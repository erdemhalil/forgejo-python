"""Generated from spec/openapi.json (GPGKey). Do not edit by hand."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict

from pyfj._generated.models.gpg_key_email import GPGKeyEmail


class GPGKey(BaseModel):
    """GPGKey a user GPG key to sign commit and tag in repository"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    can_certify: bool | None = None
    can_encrypt_comms: bool | None = None
    can_encrypt_storage: bool | None = None
    can_sign: bool | None = None
    created_at: datetime | None = None
    emails: list[GPGKeyEmail] | None = None
    expires_at: datetime | None = None
    id: int | None = None
    key_id: str | None = None
    primary_key_id: str | None = None
    public_key: str | None = None
    subkeys: list[GPGKey] | None = None
    verified: bool | None = None
