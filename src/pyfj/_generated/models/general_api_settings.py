"""Generated from spec/openapi.json (GeneralAPISettings). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class GeneralAPISettings(BaseModel):
    """GeneralAPISettings contains global api settings exposed by it"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    default_git_trees_per_page: int | None = None
    default_max_blob_size: int | None = None
    default_paging_num: int | None = None
    max_response_items: int | None = None
