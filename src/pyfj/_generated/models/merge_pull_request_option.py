"""Generated from spec/openapi.json (MergePullRequestOption). Do not edit by hand."""

from __future__ import annotations

from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field


class MergePullRequestOptionDo(StrEnum):
    MERGE = "merge"
    REBASE = "rebase"
    REBASE_MERGE = "rebase-merge"
    SQUASH = "squash"
    FAST_FORWARD_ONLY = "fast-forward-only"
    MANUALLY_MERGED = "manually-merged"


class MergePullRequestOption(BaseModel):
    """MergePullRequestForm form for merging Pull Request"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    do: MergePullRequestOptionDo = Field(alias="Do")
    merge_commit_id: str | None = Field(default=None, alias="MergeCommitID")
    merge_message_field: str | None = Field(default=None, alias="MergeMessageField")
    merge_title_field: str | None = Field(default=None, alias="MergeTitleField")
    delete_branch_after_merge: bool | None = None
    force_merge: bool | None = None
    head_commit_id: str | None = None
    merge_when_checks_succeed: bool | None = None
