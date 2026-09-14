"""Generated resource namespaces for the ``packages`` group. Do not edit by hand.

Regenerate with ``python -m codegen``; see docs/development/codegen.md.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from pyfj._generated.models.package import Package
from pyfj._generated.models.package_file import PackageFile
from pyfj._runtime import decode

if TYPE_CHECKING:
    import builtins
    from typing import Literal

    from pyfj._runtime import AsyncForgejo as _RuntimeAsyncForgejo
    from pyfj._runtime import AsyncPaginated, Paginated
    from pyfj._runtime import Forgejo as _RuntimeForgejo


class Packages:
    """The ``packages`` namespace."""

    def __init__(self, client: _RuntimeForgejo) -> None:
        self._client = client

    def list(
        self,
        owner: str,
        *,
        type: Literal[
            "alpine",
            "cargo",
            "chef",
            "composer",
            "conan",
            "conda",
            "container",
            "cran",
            "debian",
            "generic",
            "go",
            "helm",
            "maven",
            "npm",
            "nuget",
            "pub",
            "pypi",
            "rpm",
            "rubygems",
            "swift",
            "vagrant",
        ]
        | None = None,
        q: str | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> Paginated[Package]:
        """
        Gets all packages of an owner.

        Args:
            owner: owner of the packages
            type: package type filter
            q: name filter
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            PackageList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: listPackages
        """
        _query: dict[str, object] = {"type": type, "q": q}

        return self._client._paginate("GET", f"/packages/{owner}", model=Package, params=_query, page=page, limit=limit)

    def link(self, owner: str, type: str, name: str, repo_name: str) -> None:
        """
        Link a package to a repository.

        Args:
            owner: owner of the package
            type: type of the package
            name: name of the package
            repo_name: name of the repository to link.

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: linkPackage
        """
        _response = self._client._request("POST", f"/packages/{owner}/{type}/{name}/-/link/{repo_name}")
        return decode(_response, None)

    def unlink(self, owner: str, type: str, name: str) -> None:
        """
        Unlink a package from a repository.

        Args:
            owner: owner of the package
            type: type of the package
            name: name of the package

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: unlinkPackage
        """
        _response = self._client._request("POST", f"/packages/{owner}/{type}/{name}/-/unlink")
        return decode(_response, None)

    def get(self, owner: str, type: str, name: str, version: str) -> Package:
        """
        Gets a package.

        Args:
            owner: owner of the package
            type: type of the package
            name: name of the package
            version: version of the package

        Returns:
            Package.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: getPackage
        """
        _response = self._client._request("GET", f"/packages/{owner}/{type}/{name}/{version}")
        return decode(_response, Package)

    def delete(self, owner: str, type: str, name: str, version: str) -> None:
        """
        Delete a package.

        Args:
            owner: owner of the package
            type: type of the package
            name: name of the package
            version: version of the package

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: deletePackage
        """
        _response = self._client._request("DELETE", f"/packages/{owner}/{type}/{name}/{version}")
        return decode(_response, None)

    def files(self, owner: str, type: str, name: str, version: str) -> builtins.list[PackageFile]:
        """
        Gets all files of a package.

        Args:
            owner: owner of the package
            type: type of the package
            name: name of the package
            version: version of the package

        Returns:
            PackageFileList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: listPackageFiles
        """
        _response = self._client._request("GET", f"/packages/{owner}/{type}/{name}/{version}/files")
        return decode(_response, list[PackageFile])


class AsyncPackages:
    """The ``packages`` namespace."""

    def __init__(self, client: _RuntimeAsyncForgejo) -> None:
        self._client = client

    async def list(
        self,
        owner: str,
        *,
        type: Literal[
            "alpine",
            "cargo",
            "chef",
            "composer",
            "conan",
            "conda",
            "container",
            "cran",
            "debian",
            "generic",
            "go",
            "helm",
            "maven",
            "npm",
            "nuget",
            "pub",
            "pypi",
            "rpm",
            "rubygems",
            "swift",
            "vagrant",
        ]
        | None = None,
        q: str | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> AsyncPaginated[Package]:
        """
        Gets all packages of an owner.

        Args:
            owner: owner of the packages
            type: package type filter
            q: name filter
            page: 1-based page to start iteration at.
            limit: Page size; the instance caps it server-side.

        Returns:
            PackageList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: listPackages
        """
        _query: dict[str, object] = {"type": type, "q": q}

        return await self._client._paginate(
            "GET", f"/packages/{owner}", model=Package, params=_query, page=page, limit=limit
        )

    async def link(self, owner: str, type: str, name: str, repo_name: str) -> None:
        """
        Link a package to a repository.

        Args:
            owner: owner of the package
            type: type of the package
            name: name of the package
            repo_name: name of the repository to link.

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: linkPackage
        """
        _response = await self._client._request("POST", f"/packages/{owner}/{type}/{name}/-/link/{repo_name}")
        return decode(_response, None)

    async def unlink(self, owner: str, type: str, name: str) -> None:
        """
        Unlink a package from a repository.

        Args:
            owner: owner of the package
            type: type of the package
            name: name of the package

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: unlinkPackage
        """
        _response = await self._client._request("POST", f"/packages/{owner}/{type}/{name}/-/unlink")
        return decode(_response, None)

    async def get(self, owner: str, type: str, name: str, version: str) -> Package:
        """
        Gets a package.

        Args:
            owner: owner of the package
            type: type of the package
            name: name of the package
            version: version of the package

        Returns:
            Package.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: getPackage
        """
        _response = await self._client._request("GET", f"/packages/{owner}/{type}/{name}/{version}")
        return decode(_response, Package)

    async def delete(self, owner: str, type: str, name: str, version: str) -> None:
        """
        Delete a package.

        Args:
            owner: owner of the package
            type: type of the package
            name: name of the package
            version: version of the package

        Returns:
            No content.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: deletePackage
        """
        _response = await self._client._request("DELETE", f"/packages/{owner}/{type}/{name}/{version}")
        return decode(_response, None)

    async def files(self, owner: str, type: str, name: str, version: str) -> builtins.list[PackageFile]:
        """
        Gets all files of a package.

        Args:
            owner: owner of the package
            type: type of the package
            name: name of the package
            version: version of the package

        Returns:
            PackageFileList.

        Raises:
            NotFoundError: 404. APINotFound is a not found error response.

        Operation ID: listPackageFiles
        """
        _response = await self._client._request("GET", f"/packages/{owner}/{type}/{name}/{version}/files")
        return decode(_response, list[PackageFile])
