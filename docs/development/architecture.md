---
description: pyfj's public surface, runtime behaviour, and the policies that constrain them.
---

# pyfj architecture

pyfj is a fully typed Python client for the Forgejo API: complete coverage of the vendored Forgejo 16 Spec, async-first with a complete sync mirror, generated from the Spec and tested against a real Forgejo container. It is published on PyPI as `forgejo-python`; the import name stays `pyfj`.

This is the reference for what pyfj is: its public surface, runtime behaviour, and the policies that constrain both. The generator is specified in [codegen.md](codegen.md).

## Goals

- Every Operation in the Spec is callable and documented.
- Fully typed: pydantic v2 models for every schema, annotations everywhere, `py.typed`.
- `Forgejo` and `AsyncForgejo` expose identical surfaces over httpx2.
- Ergonomic: resource namespaces, keyword arguments, lazy pagination, typed exceptions.
- Reproducible: the generated surface is committed; CI verifies it matches the Spec.
- Honest: every Operation is either generated or excluded with a documented reason.

## Non-goals (v1)

- OAuth2 authorization flows (token and basic auth only; the raw OAuth2 endpoints remain callable as Operations).
- Automatic retries or rate limiting (inject an httpx2 client for transport-level control).
- Gitea-specific compatibility work (the API lineage is shared; differences are documented, not catered to).
- More than one supported Forgejo major at a time.

## Public surface

### Clients

`Forgejo` and `AsyncForgejo` are the entry points: context managers (`with` / `async with`, plus `close()` / `aclose()`) over httpx2, with identical constructor arguments and methods. The constructor takes the instance root — `https://codeberg.org`, or a subpath mount such as `https://host/forgejo`; a URL that already ends in `/api/v1` is accepted and normalised, and invalid URLs raise immediately.

Credentials are explicit arguments, never environment variables: `token=` is sent as `Authorization: token <value>`, `auth=(user, pass)` enables BasicAuth, and `otp=` sets `X-FORGEJO-OTP`; token and BasicAuth are mutually exclusive. Impersonation is client-scoped rather than a per-method argument — `sudo=` sets the constructor default, `client.sudo` reads or replaces it for the current context, and `client.sudo_as(username)` scopes an override to a `with` / `async with` block that restores the previous value on exit (nesting-safe). Overrides are context-local, not process-global: each client owns a `ContextVar`, so sibling asyncio tasks and threads are isolated, and child tasks created with `asyncio.create_task` inherit the value at creation time.

Passing `client=` injects a preconfigured `httpx2.Client` / `AsyncClient`; transport arguments (`timeout`, `verify`, ...) are rejected unless left at their defaults, so the injected client's own configuration applies and is not silently overridden. The generated [client reference](../reference/clients.md) carries the full signatures.

### Namespaces

Operations are grouped into resource namespaces derived from the Spec's path structure — not from the Spec's tags, which bundle most of the surface into one.

- [repos](../reference/namespaces/repos/index.md) — repositories, issues, pull requests, releases, and everything under them
- [user](../reference/namespaces/user/index.md) — the authenticated user
- [users](../reference/namespaces/users/index.md) — other users
- [orgs](../reference/namespaces/orgs/index.md) — organizations
- [teams](../reference/namespaces/teams/index.md) — teams, their members, and their repositories
- [admin](../reference/namespaces/admin/index.md) — instance administration
- [notifications](../reference/namespaces/notifications/index.md) — notification threads
- [packages](../reference/namespaces/packages/index.md) — package registries and their files
- [settings](../reference/namespaces/settings/index.md) — instance settings
- [activitypub](../reference/namespaces/activitypub/index.md) — federation endpoints
- [misc](../reference/namespaces/misc/index.md) — standalone endpoints (version, licenses, markdown, markup, gitignore, label, nodeinfo, signing-key, topics, actions, ...)

Sub-resources nest further: [`client.repos.issues.create(...)`](../reference/namespaces/repos/issues/index.md), [`client.repos.issues.comments.update(...)`](../reference/namespaces/repos/issues/comments/index.md). The exact mapping is a reviewed artifact (`codegen/mapping.toml` plus a naming report), governed by [codegen.md](codegen.md). Every Operation is reachable exactly once; deprecated Operations are generated and flagged; Operations that cannot work are excluded with a documented reason in `codegen/registry.toml`.

### Method signatures

- Path parameters are positional: `client.repos.get(owner, repo)`.
- Everything else is keyword-only: query parameters, body fields, pagination controls.
- Query parameters whose value is `None` are omitted.

### Bodies

Body operations take flat keyword-only arguments generated from the body
model; bodies are serialized with wire aliases and `None`-valued fields are
omitted:

```python
client.repos.issues.create("owner", "repo", title="Bug", body="...")
```

- When the body's model has required fields, those become required
  keyword-only parameters and the body is always sent — regardless of whether
  the Spec marks the body required. Required fields are enforced statically by
  the signature, not by pydantic validation after the fact.
- Bodies whose models have no required fields are optional: every flat field
  is `X | None = None` and no body is sent when all of them are `None`.
- A body field whose name collides with a path, query, or form parameter is
  exposed with a mechanical `body_` prefix (`body_owner`, `body_repo`,
  `body_index`, `body_username`), and the method docstring names its wire
  field.

### Pagination

List operations return `Paginated[T]` (sync) / `AsyncPaginated[T]` (async):

- Iterating walks pages transparently; `limit` controls page size (the server caps it, 50 by default).
- `.total_count` is populated from `X-Total-Count` when the server sends it, else `None`.
- `.page(n)` fetches a single page explicitly; passing `page=` starts iteration at that page.

Pagination metadata is not modelled in the Spec (`X-Total-Count` is runtime-only); behaviour is pinned by integration tests.

### Responses

- Success responses decode to their model type; 204/205 → `None`; `text/*` and `text/html` → `str`; `application/zip` and octet-stream → `bytes`.
- JSON scalars and containers of scalars also decode through the same hook: `bool`, `int`, `float`, `list[str]`, and string-keyed maps of scalars.
- A documented response that cannot be decoded raises `DecodeError`.
- Non-2xx responses raise the mapped exception (below); they are never returned.

### Errors

```
ForgejoError
├── TransportError            network/timeout; wraps httpx2.TransportError
├── DecodeError               response did not match the Spec
└── APIError                  any non-2xx; carries status_code, body, response
    ├── BadRequestError           400
    ├── UnauthorizedError         401
    ├── ForbiddenError            403
    ├── NotFoundError             404
    ├── MethodNotAllowedError     405
    ├── ConflictError             409
    ├── PreconditionFailedError   412
    ├── PayloadTooLargeError      413
    ├── UnprocessableEntityError  422
    ├── LockedError               423
    ├── ServerError               5xx
    └── (other statuses map to APIError itself)
```

`APIError` always carries the raw `httpx2.Response`; `body` holds parsed JSON when possible, else text. Pydantic validation of user input raises pydantic's `ValidationError` (not wrapped). The generated [errors and pagination reference](../reference/runtime.md) documents every class.

### Models

- pydantic v2, `extra="allow"` (new server fields do not break parsing), `populate_by_name=True`.
- Field names snake_case; wire aliases preserved where they differ.
- String enums become `StrEnum`; `date-time`/`date` become `datetime`/`date`.
- All models are re-exported from `pyfj` and importable from `pyfj.models`.
- One deliberate shadow: the Spec also defines an `APIError` model; `pyfj.APIError` is the runtime exception, so the model stays importable as `pyfj.models.APIError`.
- Every model carries the Spec's description as a docstring; every field carries it as a pydantic `Field(description=...)` value (visible in `model_fields[...].description` and JSON Schema).

### Escape hatch

`client.request(method, path, *, params=None, json=None, data=None, files=None, headers=None) -> httpx2.Response` returns the raw response without error mapping — for endpoints newer than the vendored Spec.

## Runtime

### Session defaults (all overridable)

| Concern | Default | Notes |
|---|---|---|
| Timeout | 30s | httpx2's 5s default is too tight for forge operations |
| Retries | none | inject an httpx2 transport for connection-level retries |
| Redirects | not followed | documented 303/304 responses surface as `APIError` |
| TLS | verified via the OS trust store (`truststore`; `SSL_CERT_FILE`/`SSL_CERT_DIR` honored) | custom CAs via `verify=ssl.SSLContext` (string paths are deprecated; the injected client remains the escape hatch for full transport control) |
| User-Agent | `pyfj/<version>` | |
| Rate limiting | none | Forgejo does not rate-limit by default |
| Sudo | none | constructor `sudo=` default; `client.sudo` and `client.sudo_as()` override it per client context, resolved when each request is built |

### Runtime ↔ generated contract

Generated namespace methods never touch httpx2. They build parameters and call the Client's request hook, which applies auth and session policy, then maps non-2xx responses to exceptions; decoding goes through a shared helper. The exact hook signatures are frozen in the module docstring of `src/pyfj/_runtime/client.py`; generated code binds to them.

Sketch (the module docstring carries the full contract, including the namespace-binding contract):

```python
# sync
response = client._request("GET", f"/repos/{owner}/{repo}/issues", params=query)
return decode(response, Issue)  # also: list[Issue], str, bytes, None (204/205)

# pagination
return client._paginate("GET", f"/repos/{owner}/{repo}/issues", model=Issue, params=query, page=page, limit=limit)
```

The hooks read `client.sudo` when they compose headers, so impersonation resolves at send time; pagination therefore picks up the effective value on every page fetch.

## Dependency floors

| Dependency | Floor | Why |
|---|---|---|
| Python | 3.11 | `StrEnum`, `Self`; matches the ecosystem |
| pydantic | 2.7 | latest is 2.13; generated code avoids APIs newer than 2.7 |
| httpx2 | 2.0 | current stable line; older releases are out of support scope |

## Compatibility and versioning

- pyfj versions itself with SemVer; `0.x` until the surface is proven, then `1.0`.
- Forgejo **16.x** is the supported major. Forgejo guarantees API compatibility within a major; the vendored Spec is refreshed on Forgejo minor/patch releases and integration tests catch drift.
- A new Forgejo major arrives as a dedicated PR: swap the Spec, regenerate, publish the compatibility report (operations added/removed/changed) derived from the diff. Minor pyfj release — or major if operations broke.
- Deprecated Operations are generated and flagged; they disappear when upstream removes them.

## Documentation

The site is built from `docs/` with [Zensical](https://zensical.org) and mkdocstrings-python, configured in `mkdocs.yml`. It is versioned with mike and deployed to GitHub Pages: `main` publishes the `dev` alias, release tags publish `X.Y` plus the `stable` alias. Link validation is strict, so broken internal links fail CI.

- User docs: `docs/` — `index.md`, `getting-started.md`, and `docs/guides/`; the generated API reference lives under `docs/reference/`
- Engineering reference: `docs/development/`
- Human contributor workflow: `CONTRIBUTING.md`; agent contract: `AGENTS.md`
