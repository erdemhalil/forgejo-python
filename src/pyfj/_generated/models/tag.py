"""Generated from spec/openapi.json (Tag). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict

from pyfj._generated.models.commit_meta import CommitMeta
from pyfj._generated.models.tag_archive_download_count import TagArchiveDownloadCount


class Tag(BaseModel):
    """Tag represents a repository tag"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    archive_download_count: TagArchiveDownloadCount | None = None
    commit: CommitMeta | None = None
    id: str | None = None
    message: str | None = None
    name: str | None = None
    tarball_url: str | None = None
    zipball_url: str | None = None
