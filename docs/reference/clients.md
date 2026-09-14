---
title: "Clients"
description: "The synchronous and asynchronous entry points."
---

# Clients

The two entry points. Both are context managers and expose identical surfaces.

=== "Sync"

    ::: pyfj.Forgejo
        options:
          inherited_members: true
          merge_init_into_class: true
          members:
            - request
            - close
            - sudo
            - sudo_as

=== "Async"

    ::: pyfj.AsyncForgejo
        options:
          inherited_members: true
          merge_init_into_class: true
          members:
            - request
            - aclose
            - sudo
            - sudo_as

## Namespaces

Both clients expose one attribute per resource namespace:

- [`client.activitypub`](namespaces/activitypub/index.md) — Federation endpoints
- [`client.admin`](namespaces/admin/index.md) — Instance administration
- [`client.misc`](namespaces/misc/index.md) — Standalone endpoints (version, licenses, markdown, markup, gitignore, label, nodeinfo, signing-key, topics, actions, ...)
- [`client.notifications`](namespaces/notifications/index.md) — Notification threads
- [`client.orgs`](namespaces/orgs/index.md) — Organizations
- [`client.packages`](namespaces/packages/index.md) — Package registries and their files
- [`client.repos`](namespaces/repos/index.md) — Repositories, issues, pull requests, releases, and everything under them
- [`client.settings`](namespaces/settings/index.md) — Instance settings
- [`client.teams`](namespaces/teams/index.md) — Teams, their members, and their repositories
- [`client.user`](namespaces/user/index.md) — The authenticated user
- [`client.users`](namespaces/users/index.md) — Other users
