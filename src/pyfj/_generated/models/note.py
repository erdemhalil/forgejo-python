"""Generated from spec/openapi.json (Note). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict

from pyfj._generated.models.commit import Commit


class Note(BaseModel):
    """Note contains information related to a git note"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    commit: Commit | None = None
    message: str | None = None
