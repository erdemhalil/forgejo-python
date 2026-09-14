"""Generated from spec/openapi.json (ChangeFileOperation). Do not edit by hand."""

from __future__ import annotations

from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field


class ChangeFileOperationOperation(StrEnum):
    """indicates what to do with the file"""

    CREATE = "create"
    UPDATE = "update"
    DELETE = "delete"


class ChangeFileOperation(BaseModel):
    """ChangeFileOperation for creating, updating or deleting a file"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    content: str | None = Field(default=None, description="new or updated file content, must be base64 encoded")
    from_path: str | None = Field(default=None, description="old path of the file to move")
    operation: ChangeFileOperationOperation = Field(description="indicates what to do with the file")
    path: str = Field(description="path to the existing or new file")
    sha: str | None = Field(
        default=None, description="sha is the SHA for the file that already exists, required for update or delete"
    )
