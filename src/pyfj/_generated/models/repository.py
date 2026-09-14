"""Generated from spec/openapi.json (Repository). Do not edit by hand."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field

from pyfj._generated.models.external_tracker import ExternalTracker
from pyfj._generated.models.external_wiki import ExternalWiki
from pyfj._generated.models.internal_tracker import InternalTracker
from pyfj._generated.models.permission import Permission
from pyfj._generated.models.repo_transfer import RepoTransfer
from pyfj._generated.models.user import User


class RepositoryObjectFormatName(StrEnum):
    """ObjectFormatName of the underlying git repository"""

    SHA1 = "sha1"
    SHA256 = "sha256"


class Repository(BaseModel):
    """Repository represents a repository"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    allow_fast_forward_only_merge: bool | None = None
    allow_merge_commits: bool | None = None
    allow_rebase: bool | None = None
    allow_rebase_explicit: bool | None = None
    allow_rebase_update: bool | None = None
    allow_squash_merge: bool | None = None
    archived: bool | None = None
    archived_at: datetime | None = None
    avatar_url: str | None = None
    clone_url: str | None = None
    created_at: datetime | None = None
    default_allow_maintainer_edit: bool | None = None
    default_branch: str | None = None
    default_delete_branch_after_merge: bool | None = None
    default_merge_style: str | None = None
    default_update_style: str | None = None
    description: str | None = None
    empty: bool | None = None
    external_tracker: ExternalTracker | None = None
    external_wiki: ExternalWiki | None = None
    fork: bool | None = None
    forks_count: int | None = None
    full_name: str | None = None
    globally_editable_wiki: bool | None = None
    has_actions: bool | None = None
    has_issues: bool | None = None
    has_packages: bool | None = None
    has_projects: bool | None = None
    has_pull_requests: bool | None = None
    has_releases: bool | None = None
    has_wiki: bool | None = Field(default=None, description="is the wiki enabled")
    has_wiki_contents: bool | None = Field(default=None, description="have wiki pages ever been created")
    html_url: str | None = None
    id: int | None = None
    ignore_whitespace_conflicts: bool | None = None
    internal: bool | None = None
    internal_tracker: InternalTracker | None = None
    language: str | None = None
    languages_url: str | None = None
    link: str | None = None
    mirror: bool | None = None
    mirror_interval: str | None = None
    mirror_updated: datetime | None = None
    name: str | None = None
    object_format_name: RepositoryObjectFormatName | None = Field(
        default=None, description="ObjectFormatName of the underlying git repository"
    )
    open_issues_count: int | None = None
    open_pr_counter: int | None = None
    original_url: str | None = None
    owner: User | None = None
    parent: Repository | None = None
    permissions: Permission | None = None
    private: bool | None = None
    release_counter: int | None = None
    repo_transfer: RepoTransfer | None = None
    size: int | None = None
    ssh_url: str | None = None
    stars_count: int | None = None
    template: bool | None = None
    topics: list[str] | None = None
    updated_at: datetime | None = None
    url: str | None = None
    watchers_count: int | None = None
    website: str | None = None
    wiki_branch: str | None = None
    wiki_clone_url: str | None = None
    wiki_ssh_url: str | None = None
