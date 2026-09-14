"""Generated from spec/openapi.json (WrappedDoc). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class WrappedDoc(BaseModel):
    """WrappedDoc carries a deliberately long one-line description so that the generated class docstring must
    wrap across several physical lines without dropping any of the words in the Spec description.
    """

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    detail: str | None = Field(
        default=None,
        description=(
            "This field description is also deliberately long enough to require the emitter to wrap it into "
            "several implicitly concatenated string chunks while keeping every single word from the Spec."
        ),
    )
    notes: str | None = Field(default=None, description="First line of the notes. Second line of the notes.")
