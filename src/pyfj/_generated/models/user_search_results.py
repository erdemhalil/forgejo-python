"""Generated from spec/openapi.json (UserSearchResults). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict

from pyfj._generated.models.user import User


class UserSearchResults(BaseModel):
    """UserSearchResults"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: list[User] | None = None
    ok: bool | None = None
