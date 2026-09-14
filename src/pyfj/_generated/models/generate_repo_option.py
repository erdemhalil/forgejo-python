"""Generated from spec/openapi.json (GenerateRepoOption). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class GenerateRepoOption(BaseModel):
    """GenerateRepoOption options when creating repository using a template"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    avatar: bool | None = Field(default=None, description="include avatar of the template repo")
    default_branch: str | None = Field(default=None, description="Default branch of the new repository")
    description: str | None = Field(default=None, description="Description of the repository to create")
    git_content: bool | None = Field(default=None, description="include git content of default branch in template repo")
    git_hooks: bool | None = Field(default=None, description="include git hooks in template repo")
    labels: bool | None = Field(default=None, description="include labels in template repo")
    name: str = Field(description="Name of the repository to create")
    owner: str = Field(description="The organization or person who will own the new repository")
    private: bool | None = Field(default=None, description="Whether the repository is private")
    protected_branch: bool | None = Field(default=None, description="include protected branches in template repo")
    topics: bool | None = Field(default=None, description="include topics in template repo")
    webhooks: bool | None = Field(default=None, description="include webhooks in template repo")
