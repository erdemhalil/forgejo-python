"""Generated resource namespaces for the ``admin`` group. Do not edit by hand.

Regenerate with ``python -m codegen``; see docs/development/codegen.md.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from pyfj._generated.models.search_results import SearchResults
from pyfj._runtime import decode

if TYPE_CHECKING:
    import builtins

    from pyfj._runtime import AsyncForgejo as _RuntimeAsyncForgejo
    from pyfj._runtime import Forgejo as _RuntimeForgejo


class Admin:
    """The ``admin`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client
        self.reports: AdminReports = AdminReports(client)

    def search(self, *, q: str, page: int | None = None, limit: int | None = None) -> SearchResults:
        """
        Search wrapped results.

        Args:
            q: Query string.
            page:
            limit:

        Returns:
            Search results.

        Operation ID: adminSearch
        """
        _query: dict[str, object] = {"q": q, "page": page, "limit": limit}

        _response = self._client._request("GET", "/admin/search", params=_query)
        return decode(_response, SearchResults)


class AsyncAdmin:
    """The ``admin`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client
        self.reports: AsyncAdminReports = AsyncAdminReports(client)

    async def search(self, *, q: str, page: int | None = None, limit: int | None = None) -> SearchResults:
        """
        Search wrapped results.

        Args:
            q: Query string.
            page:
            limit:

        Returns:
            Search results.

        Operation ID: adminSearch
        """
        _query: dict[str, object] = {"q": q, "page": page, "limit": limit}

        _response = await self._client._request("GET", "/admin/search", params=_query)
        return decode(_response, SearchResults)


class AdminReports:
    """The ``admin.reports`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def flags(self) -> builtins.list[str]:
        """
        Read a list of flags.

        Returns:
            Flag names.

        Operation ID: adminReportFlags
        """
        _response = self._client._request("GET", "/admin/reports/flags")
        return decode(_response, list[str])

    def languages(self) -> dict[str, int]:
        """
        Read language statistics.

        Returns:
            Bytes per language.

        Operation ID: adminReportLanguages
        """
        _response = self._client._request("GET", "/admin/reports/languages")
        return decode(_response, dict[str, int])

    def summary(self) -> bool:
        """
        Read a boolean report.

        Returns:
            The summary flag.

        Operation ID: adminReportSummary
        """
        _response = self._client._request("GET", "/admin/reports/summary")
        return decode(_response, bool)


class AsyncAdminReports:
    """The ``admin.reports`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def flags(self) -> builtins.list[str]:
        """
        Read a list of flags.

        Returns:
            Flag names.

        Operation ID: adminReportFlags
        """
        _response = await self._client._request("GET", "/admin/reports/flags")
        return decode(_response, list[str])

    async def languages(self) -> dict[str, int]:
        """
        Read language statistics.

        Returns:
            Bytes per language.

        Operation ID: adminReportLanguages
        """
        _response = await self._client._request("GET", "/admin/reports/languages")
        return decode(_response, dict[str, int])

    async def summary(self) -> bool:
        """
        Read a boolean report.

        Returns:
            The summary flag.

        Operation ID: adminReportSummary
        """
        _response = await self._client._request("GET", "/admin/reports/summary")
        return decode(_response, bool)
