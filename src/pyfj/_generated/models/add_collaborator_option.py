"""Generated from spec/openapi.json (AddCollaboratorOption). Do not edit by hand."""

from __future__ import annotations

from enum import StrEnum

from pydantic import BaseModel, ConfigDict


class AddCollaboratorOptionPermission(StrEnum):
    READ = "read"
    WRITE = "write"
    ADMIN = "admin"


class AddCollaboratorOption(BaseModel):
    """AddCollaboratorOption options when adding a user as a collaborator of a repository"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    permission: AddCollaboratorOptionPermission | None = None
