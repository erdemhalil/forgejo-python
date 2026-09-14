---
description: Reach endpoints newer than the vendored Spec with raw client.request calls.
---

# Escape hatch

The generated surface tracks the vendored Forgejo 16 Spec. When an endpoint is newer than the Spec — or you need the raw response for another reason — `client.request(...)` sends it and hands you the `httpx.Response`.

## Raw requests

`request(method, path, *, params=None, json=None, data=None, files=None, headers=None)` applies pyfj's session headers (credentials, `User-Agent`, and `Sudo`) and drops `None`-valued query parameters, but performs no status mapping and no decoding. Transport failures propagate as httpx exceptions:

```python
response = client.request("GET", "/repos/forgejo/forgejo/actions/tasks")

print(response.status_code)
tasks = response.json()
```

A leading slash is optional. Use `response.raise_for_status()` for httpx's own error handling; pyfj's [typed errors](errors.md) do not apply here.

## Bodies and async

Send JSON bodies with `json=`, and form or multipart data with `data=` and `files=`:

```python
response = client.request(
    "POST",
    "/repos/forgejo/playground/hooks",
    json={"type": "gitea", "config": {"url": "https://example.com/hook"}},
)
```

On `AsyncForgejo`, `request` is awaited:

```python
response = await client.request("GET", "/repos/forgejo/forgejo/actions/tasks")
```
