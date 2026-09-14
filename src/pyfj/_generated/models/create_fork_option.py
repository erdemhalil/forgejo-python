"""Generated from spec/openapi.json (CreateForkOption). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class CreateForkOption(BaseModel):
    """CreateForkOption options for creating a fork"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None = Field(default=None, description="name of the forked repository")
    organization: str | None = Field(default=None, description="organization name, if forking into an organization")
