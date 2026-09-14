"""Generated from spec/openapi.json (PayloadCommit). Do not edit by hand."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from pyfj._generated.models.payload_commit_verification import PayloadCommitVerification
from pyfj._generated.models.payload_user import PayloadUser


class PayloadCommit(BaseModel):
    """PayloadCommit represents a commit"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    added: list[str] | None = None
    author: PayloadUser | None = None
    committer: PayloadUser | None = None
    id: str | None = Field(default=None, description="sha1 hash of the commit")
    message: str | None = None
    modified: list[str] | None = None
    removed: list[str] | None = None
    timestamp: datetime | None = None
    url: str | None = None
    verification: PayloadCommitVerification | None = None
