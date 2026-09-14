"""Generated from spec/openapi.json (TransferRepoOption). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class TransferRepoOption(BaseModel):
    """TransferRepoOption options when transfer a repository's ownership"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    new_owner: str
    team_ids: list[int] | None = Field(
        default=None,
        description=(
            "ID of the team or teams to add to the repository. Teams can only be added to organization-owned "
            "repositories."
        ),
    )
