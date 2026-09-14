"""Generated from spec/openapi.json (UpdateRepoAvatarOption). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class UpdateRepoAvatarOption(BaseModel):
    """UpdateRepoAvatarUserOption options when updating the repo avatar"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    image: str | None = Field(default=None, description="image must be base64 encoded")
