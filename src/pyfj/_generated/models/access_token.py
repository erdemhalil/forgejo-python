"""Generated from spec/openapi.json (AccessToken). Do not edit by hand."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from pyfj._generated.models.repository_meta import RepositoryMeta


class AccessToken(BaseModel):
    """AccessToken represents an API access token."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    created_at: datetime | None = None
    id: int | None = None
    name: str | None = None
    repositories: list[RepositoryMeta] | None = Field(
        default=None,
        description=(
            "Indicates that an access token only has access to the specified repositories.  Will be null if the "
            "access token is not limited to a set of specified repositories."
        ),
    )
    scopes: list[str] | None = None
    sha1: str | None = None
    token_last_eight: str | None = None
