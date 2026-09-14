"""Generated from spec/openapi.json (RepoCollaboratorPermission). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict

from pyfj._generated.models.user import User


class RepoCollaboratorPermission(BaseModel):
    """RepoCollaboratorPermission to get repository permission for a collaborator"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    permission: str | None = None
    role_name: str | None = None
    user: User | None = None
