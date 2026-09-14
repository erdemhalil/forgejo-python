"""Generated from spec/openapi.json (MarkupOption). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class MarkupOption(BaseModel):
    """MarkupOption markup options"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    branch_path: str | None = Field(
        default=None, alias="BranchPath", description="The current branch path where the form gets posted"
    )
    context: str | None = Field(default=None, alias="Context", description="Context to render")
    file_path: str | None = Field(
        default=None, alias="FilePath", description="File path for detecting extension in file mode"
    )
    mode: str | None = Field(default=None, alias="Mode", description="Mode to render (comment, gfm, markdown, file)")
    text: str | None = Field(default=None, alias="Text", description="Text markup to render")
    wiki: bool | None = Field(default=None, alias="Wiki", description="Is it a wiki page ?")
