"""Generated from spec/openapi.json (UpdateUserAvatarOption). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class UpdateUserAvatarOption(BaseModel):
    """UpdateUserAvatarUserOption options when updating the user avatar"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    image: str | None = Field(default=None, description="image must be base64 encoded")
