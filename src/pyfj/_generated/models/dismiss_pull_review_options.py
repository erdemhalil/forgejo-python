"""Generated from spec/openapi.json (DismissPullReviewOptions). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class DismissPullReviewOptions(BaseModel):
    """DismissPullReviewOptions are options to dismiss a pull review"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    message: str | None = None
    priors: bool | None = None
