"""Generated from spec/openapi.json (ContentsResponse). Do not edit by hand."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from pyfj._generated.models.file_links_response import FileLinksResponse


class ContentsResponse(BaseModel):
    """ContentsResponse contains information about a repo's entry's (dir, file, symlink, submodule) metadata and
    content
    """

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    links: FileLinksResponse | None = Field(default=None, alias="_links")
    content: str | None = Field(
        default=None, description="`content` is populated when `type` is `file`, otherwise null"
    )
    download_url: str | None = None
    encoding: str | None = Field(
        default=None, description="`encoding` is populated when `type` is `file`, otherwise null"
    )
    git_url: str | None = None
    html_url: str | None = None
    last_commit_sha: str | None = None
    last_commit_when: datetime | None = None
    name: str | None = None
    path: str | None = None
    sha: str | None = None
    size: int | None = None
    submodule_git_url: str | None = Field(
        default=None, description="`submodule_git_url` is populated when `type` is `submodule`, otherwise null"
    )
    target: str | None = Field(
        default=None, description="`target` is populated when `type` is `symlink`, otherwise null"
    )
    type: str | None = Field(default=None, description="`type` will be `file`, `dir`, `symlink`, or `submodule`")
    url: str | None = None
