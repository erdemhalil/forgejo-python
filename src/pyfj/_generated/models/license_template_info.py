"""Generated from spec/openapi.json (LicenseTemplateInfo). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class LicenseTemplateInfo(BaseModel):
    """LicensesInfo contains information about a License"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    body: str | None = None
    implementation: str | None = None
    key: str | None = None
    name: str | None = None
    url: str | None = None
