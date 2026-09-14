"""Generated from spec/openapi.json (ForgeOutbox). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class ForgeOutbox(BaseModel):
    """ActivityStream OrderedCollection of activities"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)
