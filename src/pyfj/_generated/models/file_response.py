"""Generated from spec/openapi.json (FileResponse). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict

from pyfj._generated.models.contents_response import ContentsResponse
from pyfj._generated.models.file_commit_response import FileCommitResponse
from pyfj._generated.models.payload_commit_verification import PayloadCommitVerification


class FileResponse(BaseModel):
    """FileResponse contains information about a repo's file"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    commit: FileCommitResponse | None = None
    content: ContentsResponse | None = None
    verification: PayloadCommitVerification | None = None
