"""Generated from spec/openapi.json (CreateOAuth2ApplicationOptions). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class CreateOAuth2ApplicationOptions(BaseModel):
    """CreateOAuth2ApplicationOptions holds options to create an oauth2 application"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    confidential_client: bool | None = None
    name: str | None = None
    redirect_uris: list[str] | None = None
