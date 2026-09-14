"""Generated from spec/openapi.json (Widget). Do not edit by hand."""

from __future__ import annotations

from datetime import date, datetime
from enum import IntEnum, StrEnum
from typing import Any

from pydantic import BaseModel, ConfigDict, Field

from pyfj._generated.models.links import Links
from pyfj._generated.models.owner import Owner
from pyfj._generated.models.part import Part
from pyfj._generated.models.state import State


class WidgetKind(StrEnum):
    """Widget kind."""

    STANDARD = "standard"
    DELUXE = "deluxe"
    LIMITED_EDITION = "limited-edition"


class WidgetPriority(IntEnum):
    """Sort priority."""

    _1 = 1
    _2 = 2
    _3 = 3


class WidgetDetail(BaseModel):
    """Inline detail."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    note: str | None = Field(default=None, description="A note.")
    weight: int | None = None


class Widget(BaseModel):
    """A widget in the mini Spec."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int = Field(description="Unique widget id.")
    name: str = Field(description="Display name.")
    state: State | None = None
    kind: WidgetKind | None = Field(default=None, description="Widget kind.")
    priority: WidgetPriority | None = Field(default=None, description="Sort priority.")
    created_at: datetime | None = Field(default=None, description="Creation timestamp.")
    birthday: date | None = Field(default=None, description="Launch date.")
    labels: list[str] | None = Field(default=None, description="Labels.")
    parts: list[Part] | None = None
    scores: list[Any] | None = Field(default=None, description="Heterogeneous scores.")
    attributes: dict[str, str] | None = Field(default=None, description="Free-form attributes.")
    anything: dict[str, Any] | None = Field(default=None, description="Arbitrary values.")
    metadata: dict[str, Any] | None = Field(default=None, description="Unmodelled metadata.")
    owner: Owner | None = None
    parent: Widget | None = None
    detail: WidgetDetail | None = Field(default=None, description="Inline detail.")
    context: str | None = Field(default=None, alias="@context", description="JSON-LD context.")
    links: Links | None = Field(default=None, alias="_links")
    camel_case: str | None = Field(
        default=None, alias="CamelCase", description="Wire name that differs from the Python field."
    )
