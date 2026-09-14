"""Generated from spec/openapi.json (Release). Do not edit by hand."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict

from pyfj._generated.models.attachment import Attachment
from pyfj._generated.models.tag_archive_download_count import TagArchiveDownloadCount
from pyfj._generated.models.user import User


class Release(BaseModel):
    """Release represents a repository release"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    archive_download_count: TagArchiveDownloadCount | None = None
    assets: list[Attachment] | None = None
    author: User | None = None
    body: str | None = None
    created_at: datetime | None = None
    draft: bool | None = None
    hide_archive_links: bool | None = None
    html_url: str | None = None
    id: int | None = None
    name: str | None = None
    prerelease: bool | None = None
    published_at: datetime | None = None
    tag_name: str | None = None
    tarball_url: str | None = None
    target_commitish: str | None = None
    upload_url: str | None = None
    url: str | None = None
    zipball_url: str | None = None
