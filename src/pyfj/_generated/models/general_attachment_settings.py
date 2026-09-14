"""Generated from spec/openapi.json (GeneralAttachmentSettings). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class GeneralAttachmentSettings(BaseModel):
    """GeneralAttachmentSettings contains global Attachment settings exposed by API"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    allowed_types: str | None = None
    enabled: bool | None = None
    max_files: int | None = None
    max_size: int | None = None
