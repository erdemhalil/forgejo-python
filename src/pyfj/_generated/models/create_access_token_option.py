"""Generated from spec/openapi.json (CreateAccessTokenOption). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

from pyfj._generated.models.repo_target_option import RepoTargetOption


class CreateAccessTokenOption(BaseModel):
    """CreateAccessTokenOption options when create access token"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str
    repositories: list[RepoTargetOption] | None = Field(
        default=None,
        description="If provided and not-empty, creates an access token with access only to specified repositories.",
    )
    scopes: list[str] | None = None
