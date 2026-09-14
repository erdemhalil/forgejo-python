"""Generated from spec/openapi.json (CommitUser). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class CommitUser(BaseModel):
    """CommitUser contains information of a user in the context of a commit."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    date: str | None = None
    email: str | None = None
    name: str | None = None
