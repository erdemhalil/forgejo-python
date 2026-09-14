"""Generated from spec/openapi.json (PublicKey). Do not edit by hand."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict

from pyfj._generated.models.user import User


class PublicKey(BaseModel):
    """PublicKey publickey is a user key to push code to repository"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    created_at: datetime | None = None
    fingerprint: str | None = None
    id: int | None = None
    key: str | None = None
    key_type: str | None = None
    read_only: bool | None = None
    title: str | None = None
    updated_at: datetime | None = None
    url: str | None = None
    user: User | None = None
    verified: bool | None = None
