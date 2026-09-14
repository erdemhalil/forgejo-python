"""Generated from spec/openapi.json (ReplaceFlagsOption). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class ReplaceFlagsOption(BaseModel):
    """ReplaceFlagsOption options when replacing the flags of a repository"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    flags: list[str] | None = None
