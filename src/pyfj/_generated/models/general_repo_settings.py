"""Generated from spec/openapi.json (GeneralRepoSettings). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class GeneralRepoSettings(BaseModel):
    """GeneralRepoSettings contains global repository settings exposed by API"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    forks_disabled: bool | None = None
    http_git_disabled: bool | None = None
    lfs_disabled: bool | None = None
    migrations_disabled: bool | None = None
    mirrors_disabled: bool | None = None
    stars_disabled: bool | None = None
    time_tracking_disabled: bool | None = None
