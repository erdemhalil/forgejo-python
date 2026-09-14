"""Generated from spec/openapi.json (RepoTransfer). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict

from pyfj._generated.models.team import Team
from pyfj._generated.models.user import User


class RepoTransfer(BaseModel):
    """RepoTransfer represents a pending repo transfer"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    doer: User | None = None
    recipient: User | None = None
    teams: list[Team] | None = None
