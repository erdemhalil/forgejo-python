"""Generated from spec/openapi.json (QuotaUsedAttachment). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class QuotaUsedAttachmentContainedIn(BaseModel):
    """Context for the attachment: URLs to the containing object"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    api_url: str | None = Field(default=None, description="API URL for the object that contains this attachment")
    html_url: str | None = Field(default=None, description="HTML URL for the object that contains this attachment")


class QuotaUsedAttachment(BaseModel):
    """QuotaUsedAttachment represents an attachment counting towards a user's quota"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    api_url: str | None = Field(default=None, description="API URL for the attachment")
    contained_in: QuotaUsedAttachmentContainedIn | None = Field(
        default=None, description="Context for the attachment: URLs to the containing object"
    )
    name: str | None = Field(default=None, description="Filename of the attachment")
    size: int | None = Field(default=None, description="Size of the attachment (in bytes)")
