"""Generated from spec/openapi.json (OAuth2Application). Do not edit by hand."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict


class OAuth2Application(BaseModel):
    """OAuth2Application represents an OAuth2 application."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    client_id: str | None = None
    client_secret: str | None = None
    confidential_client: bool | None = None
    created: datetime | None = None
    id: int | None = None
    name: str | None = None
    redirect_uris: list[str] | None = None
