"""Generated from spec/openapi.json (PRBranchInfo). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict

from pyfj._generated.models.repository import Repository


class PRBranchInfo(BaseModel):
    """PRBranchInfo information about a branch"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    label: str | None = None
    ref: str | None = None
    repo: Repository | None = None
    repo_id: int | None = None
    sha: str | None = None
