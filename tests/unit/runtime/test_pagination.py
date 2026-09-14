"""Pagination: multi-page walking, total_count, explicit pages, page/limit controls."""

from __future__ import annotations

import httpx
import pytest
from _helpers import Handler, Issue, async_client, sync_client

from pyfj._runtime import DecodeError, NotFoundError


def _items(count: int) -> list[dict[str, object]]:
    return [{"id": number, "title": f"issue-{number}"} for number in range(1, count + 1)]


def paginated_server(
    items: list[dict[str, object]],
    *,
    page_size: int,
    send_total_count: bool = True,
) -> tuple[list[httpx.Request], Handler]:
    """Serve ``items`` in fixed-size pages; page 1 is ``page=1``."""
    seen: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        page = int(request.url.params.get("page", "1"))
        start = (page - 1) * page_size
        window = items[start : start + page_size]
        headers = {"X-Total-Count": str(len(items))} if send_total_count else None
        return httpx.Response(200, json=window, headers=headers, request=request)

    return seen, handler


def test_iteration_walks_all_pages() -> None:
    seen, handler = paginated_server(_items(5), page_size=2)
    with sync_client(handler) as client:
        paginated = client._paginate("GET", "/issues", model=Issue)
        issues = list(paginated)
    assert [issue.id for issue in issues] == [1, 2, 3, 4, 5]
    assert [int(request.url.params["page"]) for request in seen] == [1, 2, 3, 4]


def test_total_count_from_header_is_available_before_iteration() -> None:
    _, handler = paginated_server(_items(5), page_size=2)
    with sync_client(handler) as client:
        paginated = client._paginate("GET", "/issues", model=Issue)
        assert paginated.total_count == 5
        assert len(list(paginated)) == 5


def test_total_count_is_none_without_header() -> None:
    _, handler = paginated_server(_items(3), page_size=2, send_total_count=False)
    with sync_client(handler) as client:
        paginated = client._paginate("GET", "/issues", model=Issue)
        assert paginated.total_count is None


def test_total_count_is_none_when_header_is_malformed() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        headers = {"X-Total-Count": "many"}
        return httpx.Response(200, json=_items(2), headers=headers, request=request)

    with sync_client(handler) as client:
        paginated = client._paginate("GET", "/issues", model=Issue)
        assert paginated.total_count is None


def test_explicit_page_fetches_one_page_without_disturbing_iteration() -> None:
    seen, handler = paginated_server(_items(5), page_size=2)
    with sync_client(handler) as client:
        paginated = client._paginate("GET", "/issues", model=Issue)
        assert [issue.id for issue in paginated.page(1)] == [1, 2]
        assert [issue.id for issue in paginated.page(2)] == [3, 4]
        assert [issue.id for issue in paginated.page(3)] == [5]
        assert paginated.total_count == 5
        assert [issue.id for issue in paginated] == [1, 2, 3, 4, 5]
    assert [int(request.url.params["page"]) for request in seen] == [1, 1, 2, 3, 2, 3, 4]


@pytest.mark.parametrize("page", [0, -1])
def test_explicit_page_is_one_based(page: int) -> None:
    _, handler = paginated_server(_items(5), page_size=2)
    with sync_client(handler) as client:
        paginated = client._paginate("GET", "/issues", model=Issue)
        with pytest.raises(ValueError, match="1-based"):
            paginated.page(page)


@pytest.mark.parametrize("page", [0, -1])
def test_start_page_is_one_based(page: int) -> None:
    _, handler = paginated_server(_items(5), page_size=2)
    with sync_client(handler) as client, pytest.raises(ValueError, match="1-based"):
        client._paginate("GET", "/issues", model=Issue, page=page)


def test_page_and_limit_are_forwarded_on_every_request() -> None:
    seen, handler = paginated_server(_items(6), page_size=2)
    with sync_client(handler) as client:
        paginated = client._paginate("GET", "/issues", model=Issue, params={"state": "open"}, page=2, limit=2)
        issues = list(paginated)
    assert [issue.id for issue in issues] == [3, 4, 5, 6]
    assert [int(request.url.params["page"]) for request in seen] == [2, 3, 4]
    assert all(request.url.params["limit"] == "2" for request in seen)
    assert all(request.url.params["state"] == "open" for request in seen)


def test_iteration_stops_on_an_empty_page_despite_a_server_side_cap() -> None:
    """The server may cap ``limit``; a short page must not truncate iteration."""
    seen, handler = paginated_server(_items(6), page_size=2)
    with sync_client(handler) as client:
        paginated = client._paginate("GET", "/issues", model=Issue, limit=100)
        issues = list(paginated)
    assert [issue.id for issue in issues] == [1, 2, 3, 4, 5, 6]
    assert [int(request.url.params["page"]) for request in seen] == [1, 2, 3, 4]


def test_first_page_error_surfaces_at_call_time() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(404, json={"message": "no issues"}, request=request)

    with sync_client(handler) as client, pytest.raises(NotFoundError):
        client._paginate("GET", "/issues", model=Issue)


def test_invalid_page_payload_raises_decode_error() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, json={"not": "a list"}, request=request)

    with sync_client(handler) as client, pytest.raises(DecodeError):
        client._paginate("GET", "/issues", model=Issue)


async def test_async_iteration_total_count_and_explicit_page() -> None:
    seen, handler = paginated_server(_items(5), page_size=2)
    async with async_client(handler) as client:
        paginated = await client._paginate("GET", "/issues", model=Issue)
        assert paginated.total_count == 5
        issues = [issue async for issue in paginated]
        second = await paginated.page(2)
    assert [issue.id for issue in issues] == [1, 2, 3, 4, 5]
    assert [issue.id for issue in second] == [3, 4]
    assert [int(request.url.params["page"]) for request in seen] == [1, 2, 3, 4, 2]


async def test_async_iteration_stops_on_an_empty_page_despite_a_server_side_cap() -> None:
    _, handler = paginated_server(_items(6), page_size=2)
    async with async_client(handler) as client:
        paginated = await client._paginate("GET", "/issues", model=Issue, limit=100)
        issues = [issue async for issue in paginated]
    assert [issue.id for issue in issues] == [1, 2, 3, 4, 5, 6]


async def test_async_explicit_page_is_one_based() -> None:
    _, handler = paginated_server(_items(5), page_size=2)
    async with async_client(handler) as client:
        paginated = await client._paginate("GET", "/issues", model=Issue)
        with pytest.raises(ValueError, match="1-based"):
            await paginated.page(0)
