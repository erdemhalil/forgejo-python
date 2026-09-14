"""Generated from spec/openapi.json (NotificationThread). Do not edit by hand."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict

from pyfj._generated.models.notification_subject import NotificationSubject
from pyfj._generated.models.repository import Repository


class NotificationThread(BaseModel):
    """NotificationThread expose Notification on API"""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int | None = None
    pinned: bool | None = None
    repository: Repository | None = None
    subject: NotificationSubject | None = None
    unread: bool | None = None
    updated_at: datetime | None = None
    url: str | None = None
