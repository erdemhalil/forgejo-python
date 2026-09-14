"""Generated resource namespaces for the ``settings`` group. Do not edit by hand.

Regenerate with ``python -m codegen``; see docs/development/codegen.md.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from pyfj._generated.models.general_api_settings import GeneralAPISettings
from pyfj._generated.models.general_attachment_settings import GeneralAttachmentSettings
from pyfj._generated.models.general_repo_settings import GeneralRepoSettings
from pyfj._generated.models.general_ui_settings import GeneralUISettings
from pyfj._runtime import decode

if TYPE_CHECKING:
    from pyfj._runtime import AsyncForgejo as _RuntimeAsyncForgejo
    from pyfj._runtime import Forgejo as _RuntimeForgejo


class Settings:
    """The ``settings`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def api(self) -> GeneralAPISettings:
        """
        Get instance's global settings for api.

        Returns:
            GeneralAPISettings.

        Operation ID: getGeneralAPISettings
        """
        _response = self._client._request("GET", "/settings/api")
        return decode(_response, GeneralAPISettings)

    def attachment(self) -> GeneralAttachmentSettings:
        """
        Get instance's global settings for Attachment.

        Returns:
            GeneralAttachmentSettings.

        Operation ID: getGeneralAttachmentSettings
        """
        _response = self._client._request("GET", "/settings/attachment")
        return decode(_response, GeneralAttachmentSettings)

    def repository(self) -> GeneralRepoSettings:
        """
        Get instance's global settings for repositories.

        Returns:
            GeneralRepoSettings.

        Operation ID: getGeneralRepositorySettings
        """
        _response = self._client._request("GET", "/settings/repository")
        return decode(_response, GeneralRepoSettings)

    def ui(self) -> GeneralUISettings:
        """
        Get instance's global settings for ui.

        Returns:
            GeneralUISettings.

        Operation ID: getGeneralUISettings
        """
        _response = self._client._request("GET", "/settings/ui")
        return decode(_response, GeneralUISettings)


class AsyncSettings:
    """The ``settings`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def api(self) -> GeneralAPISettings:
        """
        Get instance's global settings for api.

        Returns:
            GeneralAPISettings.

        Operation ID: getGeneralAPISettings
        """
        _response = await self._client._request("GET", "/settings/api")
        return decode(_response, GeneralAPISettings)

    async def attachment(self) -> GeneralAttachmentSettings:
        """
        Get instance's global settings for Attachment.

        Returns:
            GeneralAttachmentSettings.

        Operation ID: getGeneralAttachmentSettings
        """
        _response = await self._client._request("GET", "/settings/attachment")
        return decode(_response, GeneralAttachmentSettings)

    async def repository(self) -> GeneralRepoSettings:
        """
        Get instance's global settings for repositories.

        Returns:
            GeneralRepoSettings.

        Operation ID: getGeneralRepositorySettings
        """
        _response = await self._client._request("GET", "/settings/repository")
        return decode(_response, GeneralRepoSettings)

    async def ui(self) -> GeneralUISettings:
        """
        Get instance's global settings for ui.

        Returns:
            GeneralUISettings.

        Operation ID: getGeneralUISettings
        """
        _response = await self._client._request("GET", "/settings/ui")
        return decode(_response, GeneralUISettings)
