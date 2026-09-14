"""Generated from spec/openapi.json (IssueConfig). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict

from pyfj._generated.models.issue_config_contact_link import IssueConfigContactLink


class IssueConfig(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    blank_issues_enabled: bool | None = None
    contact_links: list[IssueConfigContactLink] | None = None
