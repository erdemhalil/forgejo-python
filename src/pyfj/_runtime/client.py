"""HTTP clients and the frozen generated-code contract.

The public clients are :class:`Forgejo` (sync) and :class:`AsyncForgejo`
(async): thin, fully typed wrappers over :mod:`httpx` that apply credentials,
session policy, error mapping, pagination, and decoding.

Frozen generated-code contract
==============================

Generated namespace methods never touch httpx. They format the path, build
parameters, call a request hook, and decode through
:func:`pyfj._runtime.decode.decode`. The hook signatures below are frozen;
generated code is written against them.

Sync hooks::

    def _request(
        self,
        method: str,
        path: str,  # pre-formatted, e.g. f"/repos/{owner}/{repo}/issues"
        *,
        params: Mapping[str, object] | None = None,  # query parameters; None values are dropped
        json: object | None = None,  # JSON body, e.g. params.model_dump(mode="json")
        data: Mapping[str, object] | None = None,  # urlencoded or multipart form fields
        files: Mapping[str, object] | None = None,  # multipart file parts
        content: bytes | str | None = None,  # raw request body
        headers: Mapping[str, str] | None = None,  # extra request headers (e.g. Accept)
    ) -> httpx.Response: ...


    def _paginate(
        self,
        method: str,
        path: str,  # pre-formatted
        *,
        model: type[Issue],  # element model
        params: Mapping[str, object] | None = None,  # other query parameters
        page: int | None = None,  # start page (1-based)
        limit: int | None = None,  # page size
    ) -> Paginated[Issue]: ...

Usage::

    response = client._request("GET", f"/repos/{owner}/{repo}/issues", params=query)
    return decode(response, Issue)  # also: list[Issue], str, bytes, None (204/205)

    issues = client._paginate("GET", f"/repos/{owner}/{repo}/issues", model=Issue, params=query, page=page, limit=limit)

Impersonation is client-scoped, never a hook argument: ``sudo=`` sets the
constructor default, :attr:`_BaseClient.sudo` overrides it in the current
context, and :meth:`_BaseClient.sudo_as` scopes an override to a ``with`` /
``async with`` block. The hooks read the effective value when they compose
the ``Sudo`` header, so pagination picks it up on every page fetch.

The async hooks mirror the sync ones -- ``async def _request(...)`` and
``async def _paginate(...)``, the latter returning ``AsyncPaginated[Issue]``
and pulled with ``async for``. ``decode`` is shared by both.

``_request`` and ``_paginate`` raise a mapped :class:`APIError` for any
non-2xx status and :class:`TransportError` for network failures; they always
return a 2xx response otherwise. ``client.request(...)`` is the escape hatch:
it applies auth and session headers, returns the raw ``httpx.Response``, and
performs no status or transport mapping.

Namespace-binding contract
==========================

The runtime clients expose no resource attributes and never import
``pyfj._generated``. Generated code owns the assembled public clients:

* ``pyfj._generated.api`` defines ``Forgejo`` and ``AsyncForgejo`` as
  subclasses of ``pyfj._runtime.Forgejo`` / ``pyfj._runtime.AsyncForgejo``,
  with one typed attribute per namespace (``repos``, ``user``, ...). The
  public package re-exports those classes as ``pyfj.Forgejo`` /
  ``pyfj.AsyncForgejo``.
* Every namespace class is a plain class constructed as ``Namespace(client)``
  where ``client`` is the assembled client instance; it stores the client
  (conventionally ``self._client``) and exposes child namespaces the same
  way. Namespace methods perform no I/O themselves: they call the client
  hooks above and ``decode``.
* Namespace classes type their client parameter as the runtime base
  (``pyfj._runtime.Forgejo`` / ``AsyncForgejo``) to avoid an import cycle
  with the assembled clients; the assembled clients are subclasses.
* Namespace attributes may be instance attributes assigned in ``__init__``
  or ``functools.cached_property``; both keep the surface statically typed.
  The runtime imposes no further constraints.

Example generated shape::

    # _generated/api/repos.py
    class Repos:
        def __init__(self, client: _RuntimeForgejo) -> None:
            self._client = client
            self.issues = Issues(client)

        def get(self, owner: str, repo: str) -> Repository:
            response = self._client._request("GET", f"/repos/{owner}/{repo}")
            return decode(response, Repository)


    # _generated/api/__init__.py
    class Forgejo(_RuntimeForgejo):
        @cached_property
        def repos(self) -> Repos: ...
"""

from __future__ import annotations

import importlib.metadata
from collections.abc import Mapping, Sequence
from contextvars import ContextVar
from typing import TYPE_CHECKING, ClassVar, Generic, Self, TypeVar, cast
from urllib.parse import urlsplit, urlunsplit

import httpx
from pydantic import BaseModel

from pyfj._runtime.auth import Auth
from pyfj._runtime.decode import _decode_list
from pyfj._runtime.errors import TransportError, api_error
from pyfj._runtime.pagination import AsyncPaginated, Page, Paginated, parse_total_count

if TYPE_CHECKING:
    import ssl
    from contextvars import Token
    from types import TracebackType

__all__ = ["API_PATH", "AsyncForgejo", "Forgejo"]

API_PATH = "/api/v1"
SUDO_HEADER = "Sudo"
_DEFAULT_TIMEOUT: float = 30.0
_DEFAULT_FOLLOW_REDIRECTS = False
_DEFAULT_VERIFY = True

ModelT = TypeVar("ModelT", bound=BaseModel)
_ClientT = TypeVar("_ClientT", httpx.Client, httpx.AsyncClient)

# Accepted query-parameter values; None-valued entries are dropped by the hooks.
QueryValue = str | int | float | bool | None | Sequence[str | int | float | bool | None]
QueryParams = Mapping[str, QueryValue]

# Accepted multipart file values, mirroring httpx's file-tuple shapes.
FileContent = bytes | str
FilePart = (
    FileContent
    | tuple[str | None, FileContent]
    | tuple[str | None, FileContent, str | None]
    | tuple[str | None, FileContent, str | None, Mapping[str, str]]
)
FileParts = Mapping[str, FilePart]


def _library_version() -> str:
    """Return the installed version of the ``forgejo-python`` distribution, falling back when metadata is missing."""
    try:
        return importlib.metadata.version("forgejo-python")
    except importlib.metadata.PackageNotFoundError:
        return "0.0.0"


def _api_root(instance_url: str) -> str:
    """Normalise an instance root to the ``/api/v1`` URL requests are based on."""
    parts = urlsplit(instance_url.strip())
    if parts.scheme not in {"http", "https"} or not parts.netloc:
        message = f"invalid instance URL: {instance_url!r}; expected an http(s) instance root"
        raise ValueError(message)
    if parts.query or parts.fragment:
        message = f"invalid instance URL: {instance_url!r}; query strings and fragments are not supported"
        raise ValueError(message)
    path = parts.path.rstrip("/")
    path = path.removesuffix(API_PATH)
    return urlunsplit((parts.scheme, parts.netloc, path, "", "")) + API_PATH


def _clean_params(params: Mapping[str, object] | None) -> dict[str, object] | None:
    """Drop ``None``-valued query parameters (httpx would coerce them to "")."""
    if params is None:
        return None
    return {key: value for key, value in params.items() if value is not None}


class _BaseClient(Generic[_ClientT]):
    """Shared configuration for :class:`Forgejo` and :class:`AsyncForgejo`."""

    _httpx_class: ClassVar[type[httpx.Client | httpx.AsyncClient]]
    _client: _ClientT

    def __init__(
        self,
        instance_url: str,
        *,
        token: str | None = None,
        auth: tuple[str, str] | None = None,
        otp: str | None = None,
        sudo: str | None = None,
        timeout: float | httpx.Timeout = _DEFAULT_TIMEOUT,
        follow_redirects: bool = _DEFAULT_FOLLOW_REDIRECTS,
        verify: bool | ssl.SSLContext = _DEFAULT_VERIFY,
        client: _ClientT | None = None,
    ) -> None:
        self._auth = Auth(token=token, basic=auth, otp=otp)
        self._sudo_default = sudo
        self._sudo_override: ContextVar[str | None] = ContextVar("pyfj-sudo", default=None)
        self._base_url = _api_root(instance_url)
        self._user_agent = f"pyfj/{_library_version()}"
        if client is None:
            self._client = self._create_client(
                timeout=timeout,
                follow_redirects=follow_redirects,
                verify=verify,
            )
            return
        self._check_injected(client, timeout=timeout, follow_redirects=follow_redirects, verify=verify)
        self._client = client

    @classmethod
    def _create_client(
        cls,
        *,
        timeout: float | httpx.Timeout,
        follow_redirects: bool,
        verify: bool | ssl.SSLContext,
    ) -> _ClientT:
        raise NotImplementedError

    def _check_injected(
        self,
        client: _ClientT,
        *,
        timeout: float | httpx.Timeout,
        follow_redirects: bool,
        verify: bool | ssl.SSLContext,
    ) -> None:
        """Reject transport arguments when the caller supplies an httpx client."""
        problems: list[str] = []
        if timeout != _DEFAULT_TIMEOUT:
            problems.append("timeout")
        if follow_redirects is not _DEFAULT_FOLLOW_REDIRECTS:
            problems.append("follow_redirects")
        if verify is not _DEFAULT_VERIFY:
            problems.append("verify")
        if problems:
            arguments = ", ".join(problems)
            message = f"transport arguments cannot be combined with an injected httpx client: {arguments}"
            raise TypeError(message)
        if not isinstance(client, self._httpx_class):
            expected = f"{self._httpx_class.__module__}.{self._httpx_class.__name__}"
            actual = f"{type(client).__module__}.{type(client).__name__}"
            message = f"expected an {expected} instance, got {actual}"
            raise TypeError(message)

    def _url(self, path: str) -> str:
        """Join a path to the API root; a leading slash is optional."""
        if not path.startswith("/"):
            path = f"/{path}"
        return f"{self._base_url}{path}"

    @property
    def sudo(self) -> str | None:
        """The effective ``Sudo`` header value for the current context.

        Returns the context-local override when one is set, else the
        constructor's ``sudo=`` default. Assigning a username sets the
        override for the current context; assigning ``None`` clears it and
        restores the default.

        Overrides are context-local, not process-global: sibling asyncio tasks
        and threads are unaffected, and child tasks created with
        :func:`asyncio.create_task` inherit the value at creation time.
        """
        override = self._sudo_override.get()
        return self._sudo_default if override is None else override

    @sudo.setter
    def sudo(self, username: str | None) -> None:
        self._sudo_override.set(username)

    def sudo_as(self, username: str) -> _SudoScope:
        """Impersonate ``username`` for the duration of a ``with`` block.

        Returns a context manager that sets the sudo override on entry and
        restores the previous value on exit, so scopes nest and an exception
        leaves no residue. Accepts both ``with`` and ``async with`` and
        performs no I/O; the override is context-local (see :attr:`sudo`).
        """
        return _SudoScope(self._sudo_override, username)

    def _headers(self, headers: Mapping[str, str] | None) -> dict[str, str]:
        """Merge session headers (User-Agent, credentials, sudo) with caller headers."""
        merged = {"User-Agent": self._user_agent}
        merged.update(self._auth.headers())
        sudo = self.sudo
        if sudo is not None:
            merged[SUDO_HEADER] = sudo
        if headers is not None:
            merged.update(headers)
        return merged


class _SudoScope:
    """Context-local sudo override returned by :meth:`_BaseClient.sudo_as`.

    Entry sets the override; exit restores the previous value through the
    :class:`~contextvars.ContextVar` token, so nested scopes unwind in order.
    Both the synchronous and asynchronous forms work on either client; there
    is no I/O.
    """

    __slots__ = ("_token", "_username", "_var")

    def __init__(self, var: ContextVar[str | None], username: str) -> None:
        self._var = var
        self._username = username
        self._token: Token[str | None] | None = None

    def __enter__(self) -> Self:
        self._token = self._var.set(self._username)
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        if self._token is not None:
            self._var.reset(self._token)
            self._token = None

    async def __aenter__(self) -> Self:
        return self.__enter__()

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        self.__exit__(exc_type, exc, traceback)


class Forgejo(_BaseClient[httpx.Client]):
    """Synchronous client for one Forgejo instance.

    Args:
        instance_url: instance root, e.g. ``https://codeberg.org`` or a subpath
            mount like ``https://host/forgejo``. A URL already ending in
            ``/api/v1`` is accepted and normalised. Invalid URLs raise
            :class:`ValueError` immediately.
        token: API token; sent as ``Authorization: token <value>``. An existing
            ``token `` prefix is not duplicated.
        auth: ``(username, password)`` pair for HTTP Basic auth. Mutually
            exclusive with ``token``.
        otp: one-time password sent as ``X-FORGEJO-OTP``.
        sudo: default value of the ``Sudo`` header; :attr:`sudo` overrides it
            for the current context and :meth:`sudo_as` scopes it to a block.
        timeout: request timeout; defaults to 30 seconds.
        follow_redirects: whether httpx follows redirects; defaults to
            ``False``, so documented 3xx responses surface as ``APIError``.
        verify: TLS verification; pass an :class:`ssl.SSLContext` for custom
            certificate authorities.
        client: a preconfigured :class:`httpx.Client`. Passing one rejects
            ``timeout`` / ``follow_redirects`` / ``verify`` (their defaults
            excepted) to avoid ambiguity.

    The client is a context manager and exposes :meth:`close`. pyfj never
    reads environment variables; credentials are explicit only. Impersonation
    is context-local: ``client.sudo`` and ``client.sudo_as(...)`` apply to the
    current task or thread only.
    """

    _httpx_class = httpx.Client

    @classmethod
    def _create_client(
        cls,
        *,
        timeout: float | httpx.Timeout,
        follow_redirects: bool,
        verify: bool | ssl.SSLContext,
    ) -> httpx.Client:
        return httpx.Client(timeout=timeout, follow_redirects=follow_redirects, verify=verify)

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Mapping[str, object] | None = None,
        json: object | None = None,
        data: Mapping[str, object] | None = None,
        files: Mapping[str, object] | None = None,
        headers: Mapping[str, str] | None = None,
    ) -> httpx.Response:
        """Send a raw request to the instance and return the raw response.

        Escape hatch for endpoints newer than the vendored Spec: auth and
        session headers are applied, but no status or transport error mapping
        happens.
        """
        request = self._build_request(
            method,
            path,
            params=params,
            json=json,
            data=data,
            files=files,
            headers=headers,
        )
        return self._send(request)

    def _request(
        self,
        method: str,
        path: str,
        *,
        params: Mapping[str, object] | None = None,
        json: object | None = None,
        data: Mapping[str, object] | None = None,
        files: Mapping[str, object] | None = None,
        content: bytes | str | None = None,
        headers: Mapping[str, str] | None = None,
    ) -> httpx.Response:
        """Send a request, raising mapped errors; frozen generated-code hook."""
        request = self._build_request(
            method,
            path,
            params=params,
            json=json,
            data=data,
            files=files,
            content=content,
            headers=headers,
        )
        try:
            response = self._send(request)
        except httpx.TransportError as exc:
            raise TransportError(request.method, str(request.url), exc) from exc
        if not response.is_success:
            raise api_error(response)
        return response

    def _paginate(
        self,
        method: str,
        path: str,
        *,
        model: type[ModelT],
        params: Mapping[str, object] | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> Paginated[ModelT]:
        """Fetch the first page and return a lazy multi-page iterator.

        Each page fetch reads the effective sudo value at send time, so a
        context that changes mid-iteration applies to later pages.
        """
        start_page = 1 if page is None else page
        if start_page < 1:
            message = "page numbers are 1-based"
            raise ValueError(message)

        def fetch(number: int) -> Page[ModelT]:
            query = dict(params or {})
            query["page"] = number
            if limit is not None:
                query["limit"] = limit
            response = self._request(method, path, params=query)
            items = _decode_list(response, model)
            return Page(items=items, total_count=parse_total_count(response))

        first_page = fetch(start_page)
        return Paginated(fetch, first_page, start_page=start_page)

    def _build_request(
        self,
        method: str,
        path: str,
        *,
        params: Mapping[str, object] | None = None,
        json: object | None = None,
        data: Mapping[str, object] | None = None,
        files: Mapping[str, object] | None = None,
        content: bytes | str | None = None,
        headers: Mapping[str, str] | None = None,
    ) -> httpx.Request:
        return self._client.build_request(
            method,
            self._url(path),
            params=cast("QueryParams | None", _clean_params(params)),
            content=content,
            data=data,
            files=cast("FileParts | None", files),
            json=json,
            headers=self._headers(headers),
        )

    def _send(self, request: httpx.Request) -> httpx.Response:
        if self._auth.authorizes_requests:
            # pyfj credentials own the Authorization header; an injected
            # client's own auth flow must not overwrite it.
            return self._client.send(request, auth=None)
        return self._client.send(request)

    def close(self) -> None:
        """Close the underlying httpx client (also when it was injected)."""
        self._client.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        self.close()


class AsyncForgejo(_BaseClient[httpx.AsyncClient]):
    """Asynchronous client for one Forgejo instance.

    Arguments and behaviour mirror :class:`Forgejo`; it is an async context
    manager and exposes :meth:`aclose`.
    """

    _httpx_class = httpx.AsyncClient

    @classmethod
    def _create_client(
        cls,
        *,
        timeout: float | httpx.Timeout,
        follow_redirects: bool,
        verify: bool | ssl.SSLContext,
    ) -> httpx.AsyncClient:
        return httpx.AsyncClient(timeout=timeout, follow_redirects=follow_redirects, verify=verify)

    async def request(
        self,
        method: str,
        path: str,
        *,
        params: Mapping[str, object] | None = None,
        json: object | None = None,
        data: Mapping[str, object] | None = None,
        files: Mapping[str, object] | None = None,
        headers: Mapping[str, str] | None = None,
    ) -> httpx.Response:
        """Send a raw request to the instance and return the raw response.

        Escape hatch for endpoints newer than the vendored Spec: auth and
        session headers are applied, but no status or transport error mapping
        happens.
        """
        request = self._build_request(
            method,
            path,
            params=params,
            json=json,
            data=data,
            files=files,
            headers=headers,
        )
        return await self._send(request)

    async def _request(
        self,
        method: str,
        path: str,
        *,
        params: Mapping[str, object] | None = None,
        json: object | None = None,
        data: Mapping[str, object] | None = None,
        files: Mapping[str, object] | None = None,
        content: bytes | str | None = None,
        headers: Mapping[str, str] | None = None,
    ) -> httpx.Response:
        """Send a request, raising mapped errors; frozen generated-code hook."""
        request = self._build_request(
            method,
            path,
            params=params,
            json=json,
            data=data,
            files=files,
            content=content,
            headers=headers,
        )
        try:
            response = await self._send(request)
        except httpx.TransportError as exc:
            raise TransportError(request.method, str(request.url), exc) from exc
        if not response.is_success:
            raise api_error(response)
        return response

    async def _paginate(
        self,
        method: str,
        path: str,
        *,
        model: type[ModelT],
        params: Mapping[str, object] | None = None,
        page: int | None = None,
        limit: int | None = None,
    ) -> AsyncPaginated[ModelT]:
        """Fetch the first page and return a lazy multi-page async iterator.

        Each page fetch reads the effective sudo value at send time, so a
        context that changes mid-iteration applies to later pages.
        """
        start_page = 1 if page is None else page
        if start_page < 1:
            message = "page numbers are 1-based"
            raise ValueError(message)

        async def fetch(number: int) -> Page[ModelT]:
            query = dict(params or {})
            query["page"] = number
            if limit is not None:
                query["limit"] = limit
            response = await self._request(method, path, params=query)
            items = _decode_list(response, model)
            return Page(items=items, total_count=parse_total_count(response))

        first_page = await fetch(start_page)
        return AsyncPaginated(fetch, first_page, start_page=start_page)

    def _build_request(
        self,
        method: str,
        path: str,
        *,
        params: Mapping[str, object] | None = None,
        json: object | None = None,
        data: Mapping[str, object] | None = None,
        files: Mapping[str, object] | None = None,
        content: bytes | str | None = None,
        headers: Mapping[str, str] | None = None,
    ) -> httpx.Request:
        return self._client.build_request(
            method,
            self._url(path),
            params=cast("QueryParams | None", _clean_params(params)),
            content=content,
            data=data,
            files=cast("FileParts | None", files),
            json=json,
            headers=self._headers(headers),
        )

    async def _send(self, request: httpx.Request) -> httpx.Response:
        if self._auth.authorizes_requests:
            # pyfj credentials own the Authorization header; an injected
            # client's own auth flow must not overwrite it.
            return await self._client.send(request, auth=None)
        return await self._client.send(request)

    async def aclose(self) -> None:
        """Close the underlying httpx client (also when it was injected)."""
        await self._client.aclose()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        await self.aclose()
