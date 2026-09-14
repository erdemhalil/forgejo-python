"""Generated from spec/openapi.json (Hook). Do not edit by hand."""

from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class Hook(BaseModel):
    """Hook a hook is a web hook when one repository changed"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    active: bool | None = None
    authorization_header: str | None = None
    branch_filter: str | None = None
    config: dict[str, str] | None = Field(default=None, description="Deprecated: use Metadata instead")
    content_type: str | None = None
    created_at: datetime | None = None
    events: list[str] | None = None
    id: int | None = None
    metadata: Any | None = None
    type: str | None = None
    updated_at: datetime | None = None
    url: str | None = None
