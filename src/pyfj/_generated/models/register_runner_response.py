"""Generated from spec/openapi.json (RegisterRunnerResponse). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class RegisterRunnerResponse(BaseModel):
    """RegisterRunnerResponse contains the details of the just registered runner."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int | None = None
    token: str | None = None
    uuid: str | None = None
