"""Generated from spec/openapi.json (FilesResponse). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict

from pyfj._generated.models.contents_response import ContentsResponse
from pyfj._generated.models.file_commit_response import FileCommitResponse
from pyfj._generated.models.payload_commit_verification import PayloadCommitVerification


class FilesResponse(BaseModel):
    """FilesResponse contains information about multiple files from a repo"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    commit: FileCommitResponse | None = None
    files: list[ContentsResponse] | None = None
    verification: PayloadCommitVerification | None = None
