"""Generated from spec/openapi.json (Attachment). Do not edit by hand."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum

from pydantic import BaseModel, ConfigDict


class AttachmentType(StrEnum):
    ATTACHMENT = "attachment"
    EXTERNAL = "external"


class Attachment(BaseModel):
    """Attachment a generic attachment"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    browser_download_url: str | None = None
    created_at: datetime | None = None
    download_count: int | None = None
    id: int | None = None
    name: str | None = None
    size: int | None = None
    type: AttachmentType | None = None
    uuid: str | None = None
