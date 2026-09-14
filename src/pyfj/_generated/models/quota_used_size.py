"""Generated from spec/openapi.json (QuotaUsedSize). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict

from pyfj._generated.models.quota_used_size_assets import QuotaUsedSizeAssets
from pyfj._generated.models.quota_used_size_git import QuotaUsedSizeGit
from pyfj._generated.models.quota_used_size_repos import QuotaUsedSizeRepos


class QuotaUsedSize(BaseModel):
    """QuotaUsedSize represents the size-based quota usage of a user"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    assets: QuotaUsedSizeAssets | None = None
    git: QuotaUsedSizeGit | None = None
    repos: QuotaUsedSizeRepos | None = None
