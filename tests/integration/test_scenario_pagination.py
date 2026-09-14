"""Pagination edge cases: empty, single, multi page, and ``X-Total-Count``.

Pins the runtime contract from docs/development/architecture.md: ``total_count`` mirrors
``X-Total-Count`` or is ``None`` when the instance does not send it, iteration
walks pages until an empty page, and ``.page(n)`` fetches one page explicitly.
The multi-page walk is parameterized over the sync and async clients through a
small adapter so both transports run the same flow.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

import pytest

if TYPE_CHECKING:
    from harness import RepoRef, Seed

    import pyfj

pytestmark = pytest.mark.integration


def _repo_with_issues(seed: Seed, key: str, count: int) -> RepoRef:
    repo = seed.repo_for(f"pagination-{key}")
    for number in range(count):
        seed.admin.repos.issues.create(repo.owner, repo.name, title=f"pagination issue {number}")
    return repo


class _ClientAdapter(Protocol):
    """The subset of list behaviour the parameterized walk needs."""

    suffix: str

    async def create_issue(self, owner: str, repo: str, title: str) -> None: ...

    async def total_count(self, owner: str, repo: str, limit: int) -> int | None: ...

    async def iter_titles(self, owner: str, repo: str, limit: int) -> list[str]: ...

    async def page_titles(self, owner: str, repo: str, limit: int, number: int) -> list[str]: ...


class _SyncAdapter:
    """Presents the sync client through the async adapter protocol."""

    suffix = "sync"

    def __init__(self, client: pyfj.Forgejo) -> None:
        self._client = client

    async def create_issue(self, owner: str, repo: str, title: str) -> None:
        self._client.repos.issues.create(owner, repo, title=title)

    async def total_count(self, owner: str, repo: str, limit: int) -> int | None:
        return self._client.repos.issues.list(owner, repo, limit=limit).total_count

    async def iter_titles(self, owner: str, repo: str, limit: int) -> list[str]:
        return [
            issue.title for issue in self._client.repos.issues.list(owner, repo, limit=limit) if issue.title is not None
        ]

    async def page_titles(self, owner: str, repo: str, limit: int, number: int) -> list[str]:
        paginated = self._client.repos.issues.list(owner, repo, limit=limit)
        return [issue.title for issue in paginated.page(number) if issue.title is not None]


class _AsyncAdapter:
    """Presents the async client through the same protocol."""

    suffix = "async"

    def __init__(self, client: pyfj.AsyncForgejo) -> None:
        self._client = client

    async def create_issue(self, owner: str, repo: str, title: str) -> None:
        await self._client.repos.issues.create(owner, repo, title=title)

    async def total_count(self, owner: str, repo: str, limit: int) -> int | None:
        paginated = await self._client.repos.issues.list(owner, repo, limit=limit)
        return paginated.total_count

    async def iter_titles(self, owner: str, repo: str, limit: int) -> list[str]:
        paginated = await self._client.repos.issues.list(owner, repo, limit=limit)
        return [issue.title async for issue in paginated if issue.title is not None]

    async def page_titles(self, owner: str, repo: str, limit: int, number: int) -> list[str]:
        paginated = await self._client.repos.issues.list(owner, repo, limit=limit)
        return [issue.title for issue in await paginated.page(number) if issue.title is not None]


@pytest.fixture(params=["sync", "async"])
async def any_client(
    request: pytest.FixtureRequest,
    admin_client: pyfj.Forgejo,
    async_admin_client: pyfj.AsyncForgejo,
) -> _ClientAdapter:
    """The seeded admin client, presented as sync or async."""
    if request.param == "sync":
        return _SyncAdapter(admin_client)
    return _AsyncAdapter(async_admin_client)


async def test_parameterized_multi_page_walk(any_client: _ClientAdapter, seed: Seed) -> None:
    repo = seed.repo_for(f"pagination-parameterized-{any_client.suffix}")
    for number in range(7):
        await any_client.create_issue(repo.owner, repo.name, f"parameterized issue {number}")

    assert await any_client.total_count(repo.owner, repo.name, 3) == 7
    titles = await any_client.iter_titles(repo.owner, repo.name, 3)
    assert len(titles) == 7
    assert len(set(titles)) == 7

    assert len(await any_client.page_titles(repo.owner, repo.name, 3, 1)) == 3
    assert len(await any_client.page_titles(repo.owner, repo.name, 3, 2)) == 3
    assert len(await any_client.page_titles(repo.owner, repo.name, 3, 3)) == 1
    assert await any_client.page_titles(repo.owner, repo.name, 3, 4) == []


def test_empty_page(admin_client: pyfj.Forgejo, seed: Seed) -> None:
    repo = seed.repo_for("pagination-empty")
    issues = admin_client.repos.issues.list(repo.owner, repo.name)
    assert issues.total_count == 0
    assert issues.page(1) == []
    assert list(issues) == []


def test_single_page(admin_client: pyfj.Forgejo, seed: Seed) -> None:
    repo = _repo_with_issues(seed, "single", 1)
    issues = admin_client.repos.issues.list(repo.owner, repo.name)
    assert issues.total_count == 1
    collected = list(issues)
    assert len(collected) == 1
    assert collected[0].title == "pagination issue 0"
    assert issues.page(2) == []


def test_iteration_can_start_at_an_explicit_page(admin_client: pyfj.Forgejo, seed: Seed) -> None:
    repo = _repo_with_issues(seed, "start", 5)
    issues = admin_client.repos.issues.list(repo.owner, repo.name, limit=2, page=3)
    assert issues.total_count == 5  # X-Total-Count reports items, not pages
    assert len(list(issues)) == 1


def test_page_numbers_are_validated(admin_client: pyfj.Forgejo, seed: Seed) -> None:
    repo = seed.repo.args
    with pytest.raises(ValueError, match="1-based"):
        admin_client.repos.issues.list(*repo, page=0)
    paginated = admin_client.repos.issues.list(*repo)
    with pytest.raises(ValueError, match="1-based"):
        paginated.page(0)


def test_total_count_is_present_for_standard_lists(admin_client: pyfj.Forgejo, seed: Seed) -> None:
    assert seed.issue_index >= 1  # make sure the baseline repository has at least one issue
    issues = admin_client.repos.issues.list(*seed.repo.args)
    assert issues.total_count is not None
    assert issues.total_count >= 1


def test_total_count_is_none_when_header_is_absent(admin_client: pyfj.Forgejo, seed: Seed) -> None:
    # Forgejo's dependency and blocking lists return the items without
    # X-Total-Count; ``total_count`` must stay None rather than guessing.
    repo = seed.repo_for("pagination-no-header")
    issue = seed.issue(repo, "no-header")
    dependencies = admin_client.repos.issues.dependencies.list(repo.owner, repo.name, issue.index)
    assert dependencies.total_count is None
    assert dependencies.page(1) == []
