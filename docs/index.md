---
description: A fully typed Python client for the Forgejo API — quickstart, guides, and the generated reference.
---

# pyfj

A fully typed Python client for the [Forgejo](https://forgejo.org) API — async-first, with a complete sync mirror.

## Highlights

- **Complete** — every operation in the Forgejo 16 API is callable, generated from a vendored spec.
- **Typed** — pydantic v2 models for every schema, annotations everywhere, and a `py.typed` marker.
- **Dual** — `Forgejo` (sync) and `AsyncForgejo` (async) over httpx2, with identical surfaces.
- **Ergonomic** — resource namespaces, keyword arguments, lazy `Paginated[T]` lists, and typed exceptions.

## Quickstart

```python
from pyfj import Forgejo

with Forgejo("https://codeberg.org", token="...") as client:
    repo = client.repos.get("forgejo", "forgejo")
    print(repo.full_name)

    for issue in client.repos.issues.list("forgejo", "forgejo", state="open"):
        print(f"#{issue.number} {issue.title}")
```

The async flavour is the same code with `AsyncForgejo`, `async with`, and `async for`.

## Where to next

- [Getting started](getting-started.md) — install forgejo-python, authenticate, and make your first requests.
- [Guides](guides/index.md) — authentication, pagination, errors, impersonation, and the escape hatch.
- [Architecture](development/architecture.md) — the public surface and runtime behaviour, in depth.
