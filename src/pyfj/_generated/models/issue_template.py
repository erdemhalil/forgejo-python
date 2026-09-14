"""Generated from spec/openapi.json (IssueTemplate). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict

from pyfj._generated.models.issue_form_field import IssueFormField
from pyfj._generated.models.issue_template_labels import IssueTemplateLabels


class IssueTemplate(BaseModel):
    """IssueTemplate represents an issue template for a repository"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    about: str | None = None
    body: list[IssueFormField] | None = None
    content: str | None = None
    file_name: str | None = None
    labels: IssueTemplateLabels | None = None
    name: str | None = None
    ref: str | None = None
    title: str | None = None
