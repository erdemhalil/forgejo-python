"""Generated from spec/openapi.json (Reaction). Do not edit by hand."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict

from pyfj._generated.models.user import User


class Reaction(BaseModel):
    """Reaction contain one reaction"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    content: str | None = None
    created_at: datetime | None = None
    user: User | None = None
