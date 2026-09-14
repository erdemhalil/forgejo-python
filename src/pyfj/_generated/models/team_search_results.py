"""Generated from spec/openapi.json (TeamSearchResults). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict

from pyfj._generated.models.team import Team


class TeamSearchResults(BaseModel):
    """TeamSearchResults"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: list[Team] | None = None
    ok: bool | None = None
