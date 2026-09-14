"""Generated from spec/openapi.json (SearchResults). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict

from pyfj._generated.models.repository import Repository


class SearchResults(BaseModel):
    """SearchResults results of a successful search"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: list[Repository] | None = None
    ok: bool | None = None
