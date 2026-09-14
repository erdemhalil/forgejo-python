"""Generated from spec/openapi.json (Reference). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict

from pyfj._generated.models.git_object import GitObject


class Reference(BaseModel):
    """Reference represents a Git reference."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    object: GitObject | None = None
    ref: str | None = None
    url: str | None = None
