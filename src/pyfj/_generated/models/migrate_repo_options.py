"""Generated from spec/openapi.json (MigrateRepoOptions). Do not edit by hand."""

from __future__ import annotations

from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field


class MigrateRepoOptionsService(StrEnum):
    GIT = "git"
    GITHUB = "github"
    GITEA = "gitea"
    GITLAB = "gitlab"
    GOGS = "gogs"
    ONEDEV = "onedev"
    GITBUCKET = "gitbucket"
    CODEBASE = "codebase"
    FORGEJO = "forgejo"
    PAGURE = "pagure"


class MigrateRepoOptions(BaseModel):
    """MigrateRepoOptions options for migrating repository's this is used to interact with api v1"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    auth_password: str | None = None
    auth_token: str | None = None
    auth_username: str | None = None
    clone_addr: str
    description: str | None = None
    issues: bool | None = None
    labels: bool | None = None
    lfs: bool | None = None
    lfs_endpoint: str | None = None
    milestones: bool | None = None
    mirror: bool | None = None
    mirror_interval: str | None = None
    private: bool | None = None
    pull_requests: bool | None = None
    releases: bool | None = None
    repo_name: str
    repo_owner: str | None = Field(
        default=None, description="Name of User or Organisation who will own Repo after migration"
    )
    service: MigrateRepoOptionsService | None = None
    uid: int | None = Field(default=None, description="deprecated (only for backwards compatibility)")
    wiki: bool | None = None
