"""Generated from spec/openapi.json (UpdateVariableOption). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class UpdateVariableOption(BaseModel):
    """UpdateVariableOption defines the properties of the variable to update."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str | None = Field(
        default=None,
        description=(
            "New name for the variable. If the field is empty, the variable name won't be updated. Forgejo will "
            "convert it to uppercase."
        ),
    )
    value: str = Field(
        description=(
            "Value of the variable to update. Special characters will be retained. Line endings will be "
            "normalized to LF to match the behaviour of browsers. Encode the data with Base64 if line endings "
            "should be retained."
        )
    )
