"""Generated from spec/openapi.json (RegisterRunnerOptions). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class RegisterRunnerOptions(BaseModel):
    """RegisterRunnerOptions declares the accepted options for registering runners."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    description: str | None = Field(default=None, description="Description of the runner to register.")
    ephemeral: bool | None = Field(
        default=None,
        description=(
            "Register as ephemeral runner https://forgejo.org/docs/latest/admin/actions/security/#ephemeral-runner"
        ),
    )
    name: str = Field(description="Name of the runner to register. The name of the runner does not have to be unique.")
