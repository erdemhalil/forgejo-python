"""Generated from spec/openapi.json (Package). Do not edit by hand."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict

from pyfj._generated.models.repository import Repository
from pyfj._generated.models.user import User


class Package(BaseModel):
    """Package represents a package"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    created_at: datetime | None = None
    creator: User | None = None
    html_url: str | None = None
    id: int | None = None
    name: str | None = None
    owner: User | None = None
    repository: Repository | None = None
    type: str | None = None
    version: str | None = None
