"""Generated from spec/openapi.json (TagArchiveDownloadCount). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class TagArchiveDownloadCount(BaseModel):
    """TagArchiveDownloadCount counts how many times a archive was downloaded"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    tar_gz: int | None = None
    zip: int | None = None
