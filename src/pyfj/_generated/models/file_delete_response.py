"""Generated from spec/openapi.json (FileDeleteResponse). Do not edit by hand."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, ConfigDict

from pyfj._generated.models.file_commit_response import FileCommitResponse
from pyfj._generated.models.payload_commit_verification import PayloadCommitVerification


class FileDeleteResponse(BaseModel):
    """FileDeleteResponse contains information about a repo's file that was deleted"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    commit: FileCommitResponse | None = None
    content: Any | None = None
    verification: PayloadCommitVerification | None = None
