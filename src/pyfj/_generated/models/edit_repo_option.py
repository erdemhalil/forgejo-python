"""Generated from spec/openapi.json (EditRepoOption). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

from pyfj._generated.models.external_tracker import ExternalTracker
from pyfj._generated.models.external_wiki import ExternalWiki
from pyfj._generated.models.internal_tracker import InternalTracker


class EditRepoOption(BaseModel):
    """EditRepoOption options when editing a repository's properties"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    allow_fast_forward_only_merge: bool | None = Field(
        default=None,
        description=(
            "either `true` to allow fast-forward-only merging pull requests, or `false` to prevent "
            "fast-forward-only merging."
        ),
    )
    allow_manual_merge: bool | None = Field(
        default=None, description="either `true` to allow mark pr as merged manually, or `false` to prevent it."
    )
    allow_merge_commits: bool | None = Field(
        default=None,
        description=(
            "either `true` to allow merging pull requests with a merge commit, or `false` to prevent merging pull"
            " requests with merge commits."
        ),
    )
    allow_rebase: bool | None = Field(
        default=None,
        description="either `true` to allow rebase-merging pull requests, or `false` to prevent rebase-merging.",
    )
    allow_rebase_explicit: bool | None = Field(
        default=None,
        description=(
            "either `true` to allow rebase with explicit merge commits (--no-ff), or `false` to prevent rebase "
            "with explicit merge commits."
        ),
    )
    allow_rebase_update: bool | None = Field(
        default=None,
        description="either `true` to allow updating pull request branch by rebase, or `false` to prevent it.",
    )
    allow_squash_merge: bool | None = Field(
        default=None,
        description="either `true` to allow squash-merging pull requests, or `false` to prevent squash-merging.",
    )
    archived: bool | None = Field(default=None, description="set to `true` to archive this repository.")
    autodetect_manual_merge: bool | None = Field(
        default=None,
        description=(
            "either `true` to enable AutodetectManualMerge, or `false` to prevent it. Note: In some special "
            "cases, misjudgments can occur."
        ),
    )
    default_allow_maintainer_edit: bool | None = Field(
        default=None, description="set to `true` to allow edits from maintainers by default"
    )
    default_branch: str | None = Field(default=None, description="sets the default branch for this repository.")
    default_delete_branch_after_merge: bool | None = Field(
        default=None, description="set to `true` to delete pr branch after merge by default"
    )
    default_merge_style: str | None = Field(
        default=None,
        description=(
            'set to a merge style to be used by this repository: "merge", "rebase", "rebase-merge", "squash", '
            '"fast-forward-only", "manually-merged", or "rebase-update-only".'
        ),
    )
    default_update_style: str | None = Field(
        default=None, description='set to a update style to be used by this repository: "rebase" or "merge"'
    )
    description: str | None = Field(default=None, description="a short description of the repository.")
    enable_prune: bool | None = Field(
        default=None, description="enable prune - remove obsolete remote-tracking references when mirroring"
    )
    external_tracker: ExternalTracker | None = None
    external_wiki: ExternalWiki | None = None
    globally_editable_wiki: bool | None = Field(default=None, description="set the globally editable state of the wiki")
    has_actions: bool | None = Field(
        default=None, description="either `true` to enable actions unit, or `false` to disable them."
    )
    has_issues: bool | None = Field(
        default=None, description="either `true` to enable issues for this repository or `false` to disable them."
    )
    has_packages: bool | None = Field(
        default=None, description="either `true` to enable packages unit, or `false` to disable them."
    )
    has_projects: bool | None = Field(
        default=None, description="either `true` to enable project unit, or `false` to disable them."
    )
    has_pull_requests: bool | None = Field(
        default=None, description="either `true` to allow pull requests, or `false` to prevent pull request."
    )
    has_releases: bool | None = Field(
        default=None, description="either `true` to enable releases unit, or `false` to disable them."
    )
    has_wiki: bool | None = Field(
        default=None, description="either `true` to enable the wiki for this repository or `false` to disable it."
    )
    ignore_whitespace_conflicts: bool | None = Field(
        default=None,
        description="either `true` to ignore whitespace for conflicts, or `false` to not ignore whitespace.",
    )
    internal_tracker: InternalTracker | None = None
    mirror_interval: str | None = Field(
        default=None, description="set to a string like `8h30m0s` to set the mirror interval time"
    )
    name: str | None = Field(default=None, description="name of the repository")
    private: bool | None = Field(
        default=None,
        description=(
            "either `true` to make the repository private or `false` to make it public. Note: you will get a 422 "
            "error if the organization restricts changing repository visibility to organization owners and a "
            "non-owner tries to change the value of private."
        ),
    )
    template: bool | None = Field(
        default=None,
        description="either `true` to make this repository a template or `false` to make it a normal repository",
    )
    website: str | None = Field(default=None, description="a URL with more information about the repository.")
    wiki_branch: str | None = Field(default=None, description="sets the branch used for this repository's wiki.")
