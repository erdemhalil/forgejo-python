# Changelog

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
