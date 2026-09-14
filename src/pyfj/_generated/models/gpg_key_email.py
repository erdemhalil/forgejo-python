"""Generated from spec/openapi.json (GPGKeyEmail). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class GPGKeyEmail(BaseModel):
    """GPGKeyEmail an email attached to a GPGKey"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    email: str | None = None
    verified: bool | None = None
