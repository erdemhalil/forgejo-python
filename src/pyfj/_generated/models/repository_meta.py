"""Generated from spec/openapi.json (RepositoryMeta). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class RepositoryMeta(BaseModel):
    """RepositoryMeta basic repository information"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    full_name: str | None = None
    id: int | None = None
    name: str | None = None
    owner: str | None = None
