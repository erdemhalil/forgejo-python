"""Generated from spec/openapi.json (CreateVariableOption). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class CreateVariableOption(BaseModel):
    """CreateVariableOption defines the properties of the variable to create."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    value: str = Field(
        description=(
            "Value of the variable to create. Special characters will be retained. Line endings will be "
            "normalized to LF to match the behaviour of browsers. Encode the data with Base64 if line endings "
            "should be retained."
        )
    )
