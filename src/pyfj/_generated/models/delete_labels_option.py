"""Generated from spec/openapi.json (DeleteLabelsOption). Do not edit by hand."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict


class DeleteLabelsOption(BaseModel):
    """DeleteLabelOption options for deleting a label"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    updated_at: datetime | None = None
