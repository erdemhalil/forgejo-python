"""Generated from spec/openapi.json (ChangeFilesOptions). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

from pyfj._generated.models.change_file_operation import ChangeFileOperation
from pyfj._generated.models.commit_date_options import CommitDateOptions
from pyfj._generated.models.identity import Identity


class ChangeFilesOptions(BaseModel):
    """ChangeFilesOptions options for creating, updating or deleting multiple files Note: `author` and
    `committer` are optional (if only one is given, it will be used for the other, otherwise the authenticated
    user will be used)
    """

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    author: Identity | None = None
    branch: str | None = Field(
        default=None, description="branch (optional) to base this file from. if not given, the default branch is used"
    )
    committer: Identity | None = None
    dates: CommitDateOptions | None = None
    files: list[ChangeFileOperation] = Field(description="list of file operations")
    force_overwrite_new_branch: bool | None = Field(
        default=None, description="(optional) will do a force-push if the new branch already exists"
    )
    message: str | None = Field(
        default=None,
        description="message (optional) for the commit of this file. if not supplied, a default message will be used",
    )
    new_branch: str | None = Field(
        default=None, description="new_branch (optional) will make a new branch from `branch` before creating the file"
    )
    signoff: bool | None = Field(
        default=None, description="Add a Signed-off-by trailer by the committer at the end of the commit log message."
    )
