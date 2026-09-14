"""Generated from spec/openapi.json (CreateHookOption). Do not edit by hand."""

from __future__ import annotations

from enum import StrEnum

from pydantic import BaseModel, ConfigDict

from pyfj._generated.models.create_hook_option_config import CreateHookOptionConfig


class CreateHookOptionType(StrEnum):
    FORGEJO = "forgejo"
    DINGTALK = "dingtalk"
    DISCORD = "discord"
    GITEA = "gitea"
    GOGS = "gogs"
    MSTEAMS = "msteams"
    SLACK = "slack"
    TELEGRAM = "telegram"
    FEISHU = "feishu"
    WECHATWORK = "wechatwork"
    PACKAGIST = "packagist"


class CreateHookOption(BaseModel):
    """CreateHookOption options when create a hook"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    active: bool | None = None
    authorization_header: str | None = None
    branch_filter: str | None = None
    config: CreateHookOptionConfig
    events: list[str] | None = None
    type: CreateHookOptionType
