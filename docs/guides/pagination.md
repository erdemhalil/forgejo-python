---
description: Walk list results lazily with Paginated and AsyncPaginated, and fetch single pages explicitly.
---

# Pagination

Every list operation returns a lazy pagination object: `Paginated[T]` in sync code, `AsyncPaginated[T]` in async code. The first page is fetched eagerly — so errors surface immediately and `total_count` is already known — and later pages are fetched only as you iterate.

## Iterate all pages

```python
issues = client.repos.issues.list("forgejo", "forgejo", state="open")

for issue in issues:  # walks pages transparently
    print(f"#{issue.number} {issue.title}")
```

Iteration stops when a page comes back empty. Do not stop early on a short page: the instance caps `limit` server-side, so a page can be smaller than you asked for while more pages remain.

`limit=` sets the page size and `page=` starts iteration at a 1-based page number; both are passed through to the instance, which caps them.

## Count and fetch pages explicitly

`total_count` mirrors the `X-Total-Count` response header and is `None` when the instance does not send it. `page(n)` fetches a single 1-based page and returns its items without moving the iteration cursor:

```python
issues = client.repos.issues.list("forgejo", "forgejo", limit=10)

print(issues.total_count)
second_page = issues.page(2)
```

Asking for page 0 raises `ValueError`.

Both wrappers are documented in the [errors and pagination reference](../reference/runtime.md).

## Async pagination

The async types mirror the sync ones: the operation itself must be awaited to get the iterator, `page(n)` must be awaited, and iteration uses `async for`:

```python
from pyfj import AsyncForgejo

async with AsyncForgejo("https://codeberg.org", token="...") as client:
    issues = await client.repos.issues.list("forgejo", "forgejo", state="open")

    async for issue in issues:
        print(issue.title)

    first_page = await issues.page(1)
```
