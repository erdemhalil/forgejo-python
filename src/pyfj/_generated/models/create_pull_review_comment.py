"""Generated from spec/openapi.json (CreatePullReviewComment). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class CreatePullReviewComment(BaseModel):
    """CreatePullReviewComment represent a review comment for creation api"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    body: str | None = None
    extra_lines_count: int | None = Field(
        default=None, description="number of additional lines after the commented line (0 = single line comment)"
    )
    new_position: int | None = Field(default=None, description="if comment to new file line or 0")
    old_position: int | None = Field(default=None, description="if comment to old file line or 0")
    path: str | None = Field(default=None, description="the tree path")
