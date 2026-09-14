"""Generated from spec/openapi.json (User). Do not edit by hand."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class User(BaseModel):
    """User represents a user"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    active: bool | None = Field(default=None, description="Is user active")
    avatar_url: str | None = Field(default=None, description="URL to the user's avatar")
    created: datetime | None = None
    description: str | None = Field(default=None, description="the user's description")
    email: str | None = None
    followers_count: int | None = Field(default=None, description="user counts")
    following_count: int | None = None
    full_name: str | None = Field(default=None, description="the user's full name")
    html_url: str | None = Field(default=None, description="URL to the user's profile page")
    id: int | None = Field(default=None, description="the user's id")
    is_admin: bool | None = Field(default=None, description="Is the user an administrator")
    language: str | None = Field(default=None, description="User locale")
    last_login: datetime | None = None
    location: str | None = Field(default=None, description="the user's location")
    login: str | None = Field(default=None, description="the user's username")
    login_name: str | None = Field(default=None, description="the user's authentication sign-in name.")
    prohibit_login: bool | None = Field(default=None, description="Is user login prohibited")
    pronouns: str | None = Field(default=None, description="the user's pronouns")
    restricted: bool | None = Field(default=None, description="Is user restricted")
    source_id: int | None = Field(default=None, description="The ID of the user's Authentication Source")
    starred_repos_count: int | None = None
    visibility: str | None = Field(default=None, description="User visibility level option: public, limited, private")
    website: str | None = Field(default=None, description="the user's website")
