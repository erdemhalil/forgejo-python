"""Generated from spec/openapi.json (CreateBranchProtectionOption). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class CreateBranchProtectionOption(BaseModel):
    """CreateBranchProtectionOption options for creating a branch protection"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    apply_to_admins: bool | None = None
    approvals_whitelist_teams: list[str] | None = None
    approvals_whitelist_username: list[str] | None = None
    block_on_official_review_requests: bool | None = None
    block_on_outdated_branch: bool | None = None
    block_on_rejected_reviews: bool | None = None
    branch_name: str | None = Field(default=None, description="Deprecated: true")
    dismiss_stale_approvals: bool | None = None
    enable_approvals_whitelist: bool | None = None
    enable_merge_whitelist: bool | None = None
    enable_push: bool | None = None
    enable_push_whitelist: bool | None = None
    enable_status_check: bool | None = None
    ignore_stale_approvals: bool | None = None
    merge_whitelist_teams: list[str] | None = None
    merge_whitelist_usernames: list[str] | None = None
    protected_file_patterns: str | None = None
    push_whitelist_deploy_keys: bool | None = None
    push_whitelist_teams: list[str] | None = None
    push_whitelist_usernames: list[str] | None = None
    require_signed_commits: bool | None = None
    required_approvals: int | None = None
    rule_name: str | None = None
    status_check_contexts: list[str] | None = None
    unprotected_file_patterns: str | None = None
