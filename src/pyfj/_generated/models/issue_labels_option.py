"""Generated from spec/openapi.json (IssueLabelsOption). Do not edit by hand."""

from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class IssueLabelsOption(BaseModel):
    """IssueLabelsOption a collection of labels"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    labels: list[Any] | None = Field(
        default=None,
        description=(
            "Labels can be a list of integers representing label IDs or a list of strings representing label names"
        ),
    )
    updated_at: datetime | None = None
