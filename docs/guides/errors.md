---
description: The typed exception hierarchy raised by pyfj and what each error carries.
---

# Errors

Every HTTP, transport, or decode failure raises a typed exception descending from `ForgejoError`. The [escape hatch](escape-hatch.md) is the exception to the rule: raw requests report whatever httpx2 reports.

## HTTP failures

A non-2xx response raises an `APIError`. Common statuses have dedicated subclasses — `BadRequestError` (400), `UnauthorizedError` (401), `ForbiddenError` (403), `NotFoundError` (404), `MethodNotAllowedError` (405), `ConflictError` (409), `PreconditionFailedError` (412), `PayloadTooLargeError` (413), `UnprocessableEntityError` (422), and `LockedError` (423) — while every 5xx raises `ServerError` and any other status maps to `APIError` itself.

`APIError` carries the `status_code`, the parsed `body` (JSON when the response parses, otherwise the response text), and the raw `httpx2.Response` as `response`:

```python
from pyfj import NotFoundError

try:
    client.repos.get("forgejo", "does-not-exist")
except NotFoundError as error:
    print(error.status_code, error.body)
```

## Transport and decode failures

- `TransportError` — the request produced no HTTP response (connection failure or timeout). It carries `method`, `url`, and the wrapped `cause`, and is chained with `raise ... from`.
- `DecodeError` — the response could not be decoded into the operation's declared type: invalid JSON, a pydantic validation failure, or an unexpected JSON shape. It carries the offending `response` and `reason`.

Catching the base class handles all of them:

```python
from pyfj import ForgejoError, TransportError

try:
    user = client.user.get()
except TransportError as error:
    print(f"no response from the instance: {error}")
except ForgejoError as error:
    print(f"request failed: {error}")
```

All error classes are importable from `pyfj`; the same names are what the generated namespace docstrings list under `Raises`. The full hierarchy, attribute by attribute, is in the [errors and pagination reference](../reference/runtime.md).
