"""Generated from spec/openapi.json (EditAttachmentOptions). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class EditAttachmentOptions(BaseModel):
    """EditAttachmentOptions options for editing attachments"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    browser_download_url: str | None = Field(
        default=None, description="(Can only be set if existing attachment is of external type)"
    )
    name: str | None = None
