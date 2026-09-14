"""Generated from spec/openapi.json (IssueFormField). Do not edit by hand."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, ConfigDict

from pyfj._generated.models.issue_form_field_type import IssueFormFieldType
from pyfj._generated.models.issue_form_field_visible import IssueFormFieldVisible


class IssueFormField(BaseModel):
    """IssueFormField represents a form field"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    attributes: dict[str, Any] | None = None
    id: str | None = None
    type: IssueFormFieldType | None = None
    validations: dict[str, Any] | None = None
    visible: list[IssueFormFieldVisible] | None = None
