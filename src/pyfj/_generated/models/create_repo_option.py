"""Generated from spec/openapi.json (CreateRepoOption). Do not edit by hand."""

from __future__ import annotations

from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field


class CreateRepoOptionObjectFormatName(StrEnum):
    """ObjectFormatName of the underlying git repository"""

    SHA1 = "sha1"
    SHA256 = "sha256"


class CreateRepoOptionTrustModel(StrEnum):
    """TrustModel of the repository"""

    DEFAULT = "default"
    COLLABORATOR = "collaborator"
    COMMITTER = "committer"
    COLLABORATORCOMMITTER = "collaboratorcommitter"


class CreateRepoOption(BaseModel):
    """CreateRepoOption options when creating repository"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    auto_init: bool | None = Field(default=None, description="Whether the repository should be auto-initialized?")
    default_branch: str | None = Field(
        default=None, description="DefaultBranch of the repository (used when initializes and in template)"
    )
    description: str | None = Field(default=None, description="Description of the repository to create")
    gitignores: str | None = Field(default=None, description="Gitignores to use, separated by commas")
    issue_labels: str | None = Field(default=None, description="Label-Set to use")
    license: str | None = Field(default=None, description="License to use")
    name: str = Field(description="Name of the repository to create")
    object_format_name: CreateRepoOptionObjectFormatName | None = Field(
        default=None, description="ObjectFormatName of the underlying git repository"
    )
    private: bool | None = Field(default=None, description="Whether the repository is private")
    readme: str | None = Field(default=None, description="Readme of the repository to create")
    template: bool | None = Field(default=None, description="Whether the repository is template")
    trust_model: CreateRepoOptionTrustModel | None = Field(default=None, description="TrustModel of the repository")
