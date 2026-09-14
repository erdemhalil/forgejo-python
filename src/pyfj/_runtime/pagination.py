"""Lazy pagination over list operations.

The client's ``_paginate`` hook performs the first request eagerly (so errors
surface at call time and ``total_count`` is known immediately) and returns a
:class:`Paginated` / :class:`AsyncPaginated`. Iterating then walks pages
transparently until the instance returns an empty page.

- ``total_count`` mirrors ``X-Total-Count``, or ``None`` when the instance
  does not send it.
- ``page(n)`` fetches a single 1-based page explicitly and returns its items;
  it does not move the iteration cursor (it refreshes ``total_count`` when the
  instance sends the header).
- Iteration stops on an empty page rather than a short page: the instance
  caps ``limit`` server-side, so the returned page size may be smaller than
  requested even when more pages follow.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Generic, TypeVar

if TYPE_CHECKING:
    from collections.abc import AsyncIterator, Awaitable, Callable, Iterator

    import httpx2

__all__ = ["AsyncPaginated", "Page", "Paginated", "parse_total_count"]

T = TypeVar("T")

TOTAL_COUNT_HEADER = "X-Total-Count"


@dataclass(frozen=True, slots=True)
class Page(Generic[T]):
    """One fetched page of items plus its pagination metadata."""

    items: list[T]
    total_count: int | None = None


def parse_total_count(response: httpx2.Response) -> int | None:
    """Read ``X-Total-Count`` from ``response``; ``None`` when absent or malformed."""
    value = response.headers.get(TOTAL_COUNT_HEADER)
    if value is None:
        return None
    try:
        return int(value)
    except ValueError:
        return None


class Paginated(Generic[T]):
    """Transparent multi-page iterator for sync list operations.

    Args:
        fetch_page: callback fetching the 1-based page number it is given.
        first_page: the page fetched by the client hook before construction.
        start_page: 1-based number of ``first_page``; iteration resumes from
            the page after it.
    """

    def __init__(
        self,
        fetch_page: Callable[[int], Page[T]],
        first_page: Page[T],
        *,
        start_page: int = 1,
    ) -> None:
        self._fetch_page = fetch_page
        self._first_page = first_page
        self._start_page = start_page
        self._total_count = first_page.total_count

    @property
    def total_count(self) -> int | None:
        """Total number of items reported by the instance, if it reported one."""
        return self._total_count

    def page(self, number: int) -> list[T]:
        """Fetch one 1-based page explicitly.

        Raises:
            ValueError: ``number`` is less than 1.
        """
        if number < 1:
            message = "page numbers are 1-based"
            raise ValueError(message)
        return self._fetch(number).items

    def _fetch(self, number: int) -> Page[T]:
        page = self._fetch_page(number)
        if page.total_count is not None:
            self._total_count = page.total_count
        return page

    def __iter__(self) -> Iterator[T]:
        number = self._start_page
        page = self._first_page
        while page.items:
            yield from page.items
            number += 1
            page = self._fetch(number)


class AsyncPaginated(Generic[T]):
    """Transparent multi-page async iterator for async list operations.

    Mirrors :class:`Paginated`; ``page`` must be awaited and iteration uses
    ``async for``.

    Args:
        fetch_page: async callback fetching the 1-based page number it is given.
        first_page: the page fetched by the client hook before construction.
        start_page: 1-based number of ``first_page``; iteration resumes from
            the page after it.
    """

    def __init__(
        self,
        fetch_page: Callable[[int], Awaitable[Page[T]]],
        first_page: Page[T],
        *,
        start_page: int = 1,
    ) -> None:
        self._fetch_page = fetch_page
        self._first_page = first_page
        self._start_page = start_page
        self._total_count = first_page.total_count

    @property
    def total_count(self) -> int | None:
        """Total number of items reported by the instance, if it reported one."""
        return self._total_count

    async def page(self, number: int) -> list[T]:
        """Fetch one 1-based page explicitly.

        Raises:
            ValueError: ``number`` is less than 1.
        """
        if number < 1:
            message = "page numbers are 1-based"
            raise ValueError(message)
        page = await self._fetch(number)
        return page.items

    async def _fetch(self, number: int) -> Page[T]:
        page = await self._fetch_page(number)
        if page.total_count is not None:
            self._total_count = page.total_count
        return page

    def __aiter__(self) -> AsyncIterator[T]:
        return self._iterate()

    async def _iterate(self) -> AsyncIterator[T]:
        number = self._start_page
        page = self._first_page
        while page.items:
            for item in page.items:
                yield item
            number += 1
            page = await self._fetch(number)
