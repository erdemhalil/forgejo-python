"""Generated from spec/openapi.json (AnnotatedTag). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict

from pyfj._generated.models.annotated_tag_object import AnnotatedTagObject
from pyfj._generated.models.commit_user import CommitUser
from pyfj._generated.models.payload_commit_verification import PayloadCommitVerification
from pyfj._generated.models.tag_archive_download_count import TagArchiveDownloadCount


class AnnotatedTag(BaseModel):
    """AnnotatedTag represents an annotated tag"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    archive_download_count: TagArchiveDownloadCount | None = None
    message: str | None = None
    object: AnnotatedTagObject | None = None
    sha: str | None = None
    tag: str | None = None
    tagger: CommitUser | None = None
    url: str | None = None
    verification: PayloadCommitVerification | None = None
