---
description: Install forgejo-python, create a client, and make your first Forgejo API requests.
---

# Getting started

## Install

```bash
uv add forgejo-python
```

or with pip:

```bash
pip install forgejo-python
```

The distribution is `forgejo-python`; the import name is `pyfj`, so import from `pyfj` in your code. Check it worked:

```bash
python -c "from pyfj import Forgejo"
```

## Create a client

Point the client at the instance root — the `/api/v1` path is resolved for you:

```python
from pyfj import Forgejo

client = Forgejo("https://codeberg.org")
```

Close it explicitly, or use it as a context manager:

```python
with Forgejo("https://codeberg.org") as client:
    ...
```

Credentials go in the constructor; [Authentication](guides/authentication.md) covers tokens, basic auth, and one-time passwords.

## Make a request

Path parameters are positional; everything else is keyword-only:

```python
repo = client.repos.get("forgejo", "forgejo")

client.repos.issues.create(
    "forgejo",
    "forgejo",
    title="Document the quickstart",
    body="Tracked from the docs.",
)
```

## Sync and async

Use `Forgejo` in synchronous code and `AsyncForgejo` in asynchronous code; the surfaces are identical, so moving between them is mechanical. The async client never blocks the event loop, which makes it the default choice for servers and concurrent scripts.

`AsyncForgejo` mirrors `Forgejo` operation for operation:

```python
from pyfj import AsyncForgejo

async with AsyncForgejo("https://codeberg.org", token="...") as client:
    repo = await client.repos.get("forgejo", "forgejo")

    issues = await client.repos.issues.list("forgejo", "forgejo", state="open")
    async for issue in issues:
        print(issue.title)
```

## Next

- [Guides](guides/index.md) — authentication, pagination, errors, impersonation, and the escape hatch.
- [API reference](reference/index.md) — clients, namespaces, and models.
- [Clients](reference/clients.md) — constructor arguments and session behaviour.
