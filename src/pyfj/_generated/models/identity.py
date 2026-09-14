"""Generated from spec/openapi.json (Identity). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class Identity(BaseModel):
    """Identity for a person's identity like an author or committer"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    email: str | None = None
    name: str | None = None
