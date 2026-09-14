"""Generated from spec/openapi.json (EditReleaseOption). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class EditReleaseOption(BaseModel):
    """EditReleaseOption options when editing a release"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    body: str | None = None
    draft: bool | None = None
    hide_archive_links: bool | None = None
    name: str | None = None
    prerelease: bool | None = None
    tag_name: str | None = None
    target_commitish: str | None = None
