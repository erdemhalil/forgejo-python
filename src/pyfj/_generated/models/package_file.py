"""Generated from spec/openapi.json (PackageFile). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class PackageFile(BaseModel):
    """PackageFile represents a package file"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    size: int | None = Field(default=None, alias="Size")
    id: int | None = None
    md5: str | None = None
    name: str | None = None
    sha1: str | None = None
    sha256: str | None = None
    sha512: str | None = None
