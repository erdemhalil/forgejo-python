"""Generated from spec/openapi.json (DeployKey). Do not edit by hand."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict

from pyfj._generated.models.repository import Repository


class DeployKey(BaseModel):
    """DeployKey a deploy key"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    created_at: datetime | None = None
    fingerprint: str | None = None
    id: int | None = None
    key: str | None = None
    key_id: int | None = None
    read_only: bool | None = None
    repository: Repository | None = None
    title: str | None = None
    url: str | None = None
