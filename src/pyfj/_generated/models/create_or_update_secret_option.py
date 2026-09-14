"""Generated from spec/openapi.json (CreateOrUpdateSecretOption). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class CreateOrUpdateSecretOption(BaseModel):
    """CreateOrUpdateSecretOption defines the properties of the secret to create or update."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    data: str = Field(
        description=(
            "Data of the secret. Special characters will be retained. Line endings will be normalized to LF to "
            "match the behaviour of browsers. Encode the data with Base64 if line endings should be retained."
        )
    )
