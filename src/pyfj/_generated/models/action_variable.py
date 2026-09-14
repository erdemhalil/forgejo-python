"""Generated from spec/openapi.json (ActionVariable). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class ActionVariable(BaseModel):
    """ActionVariable return value of the query API"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: str | None = Field(default=None, description="the value of the variable")
    name: str | None = Field(default=None, description="the name of the variable")
    owner_id: int | None = Field(default=None, description="the owner to which the variable belongs")
    repo_id: int | None = Field(default=None, description="the repository to which the variable belongs")
