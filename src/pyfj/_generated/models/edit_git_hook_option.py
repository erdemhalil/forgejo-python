"""Generated from spec/openapi.json (EditGitHookOption). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class EditGitHookOption(BaseModel):
    """EditGitHookOption options when modifying one Git hook"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    content: str | None = None
