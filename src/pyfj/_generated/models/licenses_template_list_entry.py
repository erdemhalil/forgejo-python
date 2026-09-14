"""Generated from spec/openapi.json (LicensesTemplateListEntry). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class LicensesTemplateListEntry(BaseModel):
    """LicensesListEntry is used for the API"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    key: str | None = None
    name: str | None = None
    url: str | None = None
