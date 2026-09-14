"""Generated from spec/openapi.json (EditHookOption). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class EditHookOption(BaseModel):
    """EditHookOption options when modify one hook"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    active: bool | None = None
    authorization_header: str | None = None
    branch_filter: str | None = None
    config: dict[str, str] | None = None
    events: list[str] | None = None
