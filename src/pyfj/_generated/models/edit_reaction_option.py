"""Generated from spec/openapi.json (EditReactionOption). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class EditReactionOption(BaseModel):
    """EditReactionOption contain the reaction type"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    content: str | None = None
