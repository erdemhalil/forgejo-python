---
description: Act as another user with the Forgejo Sudo header, scoped per client and context.
---

# Impersonation

Forgejo lets an administrator act as another user by sending a `Sudo` header naming them. pyfj models this as client-scoped state rather than a per-call argument: the constructor's `sudo=` sets the default, and the effective value is resolved when each request is sent.

## The default and the override

```python
from pyfj import Forgejo

with Forgejo("https://codeberg.org", token="...", sudo="alice") as client:
    client.user.get()  # acts as alice

    client.sudo = "bob"
    client.user.get()  # acts as bob

    client.sudo = None  # clears the override; back to alice
```

Assigning `client.sudo` overrides the default for the current context; assigning `None` clears the override and restores the constructor's default.

## Scope an override to a block

`sudo_as(...)` is a context manager: it applies for the `with` (or `async with`) block and restores the previous value on exit, even when the block raises. Scopes nest:

```python
with client.sudo_as("alice"):
    profile = client.user.get()

    with client.sudo_as("bob"):
        client.repos.issues.create("bob", "notes", title="Delegate the review")
    # alice again
```

## Context-local, not global

Overrides live in a `ContextVar` owned by each client, not in process-global state. Sibling asyncio tasks and threads are unaffected by each other, and tasks created with `asyncio.create_task` inherit the value that was current at creation time. Pagination reads the effective value on every page fetch, so a scope that changes mid-iteration applies to later pages.

`sudo_as` accepts `async with` on either client:

```python
from pyfj import AsyncForgejo

async with AsyncForgejo("https://codeberg.org", token="...") as client:
    async with client.sudo_as("alice"):
        user = await client.user.get()
```
