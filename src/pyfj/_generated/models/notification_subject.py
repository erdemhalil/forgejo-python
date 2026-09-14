"""Generated from spec/openapi.json (NotificationSubject). Do not edit by hand."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict

from pyfj._generated.models.notify_subject_type import NotifySubjectType
from pyfj._generated.models.state_type import StateType


class NotificationSubject(BaseModel):
    """NotificationSubject contains the notification subject (Issue/Pull/Commit)"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    html_url: str | None = None
    latest_comment_html_url: str | None = None
    latest_comment_url: str | None = None
    state: StateType | None = None
    title: str | None = None
    type: NotifySubjectType | None = None
    url: str | None = None
