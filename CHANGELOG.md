# Changelog

## [Unreleased]

### Changed

- **Breaking:** HTTP transport moved from `httpx` to `httpx2`. Requires `httpx2 2.0+`. Injected clients, raw `request(...)` responses, and `APIError.response` / `decode(...)` inputs are now `httpx2` types; rebuild injected `httpx.Client` / `AsyncClient` objects as `httpx2.Client` / `httpx2.AsyncClient` and update `except httpx.*` clauses. TLS verification now uses the OS trust store via `truststore` (`SSL_CERT_FILE`/`SSL_CERT_DIR` honored; `verify=` still explicit); network loggers are `httpx2` and `httpcore2.*`.

## [0.1.0] - 2026-09-14

Initial release. Requires Python 3.11+, pydantic 2.7+, and httpx 0.28.1+.

### Added

- Full Forgejo 16 API coverage from `spec/openapi.json` — one Actions operation is excluded because it needs the job token.
- Sync (`Forgejo`) and async (`AsyncForgejo`) clients over httpx with identical surfaces.
- Token, basic-auth, and one-time-password credentials, plus client-scoped impersonation (`client.sudo`, `client.sudo_as(...)`).
- Typed pydantic v2 models for every schema, re-exported from `pyfj` and `pyfj.models`.
- Resource namespaces, keyword-only arguments, lazy `Paginated[T]` lists, and typed exceptions.
- Multipart uploads, `str`/`bytes` responses, and the `client.request(...)` escape hatch.

[0.1.0]: https://github.com/erdemhalil/forgejo-python/releases/tag/v0.1.0
