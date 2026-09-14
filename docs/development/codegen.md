---
description: How the vendored Forgejo Spec becomes pyfj's typed surface.
---

# pyfj code generator

The generator turns the vendored Spec into pyfj's typed surface. This document specifies it. The surface it must produce is [architecture.md](architecture.md).

## Principles

- **Offline and deterministic**: reads `spec/openapi.json` only; no network; same input → byte-identical output.
- **No hand-editing**: `src/pyfj/_generated/**` is produced. Humans edit `codegen/` and regenerate.
- **Drift-checked**: CI runs the generator and fails if the working tree changes.
- **Reviewable**: every Operation's namespace/method assignment is visible in `codegen/naming-report.md`; deviations live in `codegen/mapping.toml`.
- **Complete**: every Operation is either generated or excluded in `codegen/registry.toml` with a reason; a test enforces this.

## Inputs

- `spec/openapi.json` — Swagger 2.0, Forgejo 16.0.4.
- `codegen/mapping.toml` — curated overrides:

```toml
# Namespace override for a path prefix
[namespaces."/user"]
name = "user"

# Method name overrides, keyed by operationId
[methods.createOrgRepoDeprecated]
name = "create"
deprecated = true

# Model name overrides, keyed by definition name
[models."SomeAwkwardName"]
class_name = "AwkwardName"
```

- `codegen/registry.toml` — exclusions from generation:

```toml
[[exclusions]]
operation = "getActionsRun"
reason = "Requires the automatic Actions job token; not usable with user credentials."
```

## Pipeline

1. Load and validate the Spec (Swagger 2.0; fail loudly on unknown shapes).
2. Resolve `$ref`s — definitions, parameters, and top-level reusable responses.
3. Build the IR: models, operations (method, path segments, parameters, body, responses, produces, deprecated flag).
4. Assign namespaces and method names (algorithm below), apply `mapping.toml`, emit `naming-report.md`.
5. Emit `_generated/models/` — one module per model.
6. Emit `_generated/api/` — one module per namespace, sync and async methods from the same IR.
7. Format with ruff.

The generator is importable and testable; `uv run python -m codegen` runs it end to end.

## Naming

Names must be Pythonic, stable, and collision-free. The algorithm below is the starting point; the naming report is reviewed, and overrides land in `mapping.toml`.

- **Namespaces** come from static path segments: `repos`, `orgs`, `user`, `users`, `teams`, `admin`, `notifications`, `packages`, `settings`, `activitypub`; sub-resources nest (`repos.issues`, `repos.issues.comments`). Standalone endpoints fall into `misc`.
- **Singular parameter segments** (`{index}`, `{id}`) never become namespaces; they become method parameters (`index=`) on the resource's methods.
- **Method verb**, from HTTP method and path shape:
  - `GET` collection → `list`; `GET` item → `get`
  - `POST` collection → `create`; action-style `POST` → verb from the operationId (`merge`, `fork`, `sync`, `add`, ...)
  - `PATCH`/`PUT` → `update`; `DELETE` → `delete`
  - A trailing static segment that is not a sub-resource names the method: `.../pulls/{index}/merge` → `client.repos.pulls.merge(...)`
- **Collisions** are resolved in `mapping.toml`; the generator fails on unresolved ones.
- **Deprecated Operations** are generated and flagged (`@deprecated` is deferred until the Python floor reaches 3.13; today they carry a docstring note and the report's deprecated column).

Worked examples:

| Operation | Call site |
|---|---|
| `repoGet` `GET /repos/{owner}/{repo}` | `client.repos.get(owner, repo)` |
| `issueCreateIssue` `POST /repos/{owner}/{repo}/issues` | `client.repos.issues.create(owner, repo, title=..., body=...)` |
| `issueListComments` `GET /repos/{owner}/{repo}/issues/{index}/comments` | `client.repos.issues.comments.list(owner, repo, index)` |
| `repoMergePullRequest` `POST /repos/{owner}/{repo}/pulls/{index}/merge` | `client.repos.pulls.merge(owner, repo, index)` |

## Spec quirks the emitter must handle

The shapes the emitter must tolerate:

- **Bodies**: nearly all use `$ref`'d schemas, with only one inline; most schemas have no required fields, and bodies whose models do have required fields are emitted as effectively required. A handful of operations have body fields colliding with path parameters (`owner`/`repo`/`index` in the issue block/dependency endpoints; `username` in admin org creation) — those fields are exposed flat with a mechanical `body_` prefix (`body_owner`, `body_repo`, `body_index`, `body_username`).
- **Multipart**: file-upload operations (issue comment attachment, issue attachment, release attachment).
- **Non-JSON produces**: `text/html` (markdown, markup) and `text/plain` (job logs, commit/PR diffs, signing keys, gpg key token) → `str`; `application/zip`, `application/octet-stream`, `application/gzip` (artifacts, archives, raw/media content) → `bytes`.
- **Odd success codes**: `202`, `205` (→ `None`), and `206` (job logs → `str`, the same text body as its 200).
- **Primitive JSON responses**: `bool`, `list[str]`, `dict[str, str]`, `dict[str, int]` decode through the runtime's `decode` overloads, like models and text.
- **3xx in the Spec**: `303` (org member GET), `304` (issue subscription PUT/DELETE) — surfaced as `APIError` since redirects are not followed.
- **Deprecated operations**: generated and flagged.
- **Parameters**: paginated list operations accept `page` + `limit`; some operations take none.
- **operationIds**: unique across the Spec — usable as stable keys for overrides and reports.
- **Security**: declared globally only, with no per-operation overrides; pyfj authenticates whenever credentials are configured, and endpoints that allow anonymous access work without them.

## Model emission rules

- One module per definition (`_generated/models/repository.py` → `Repository`), re-exported from `pyfj.models` and `pyfj`.
- `model_config = ConfigDict(extra="allow", populate_by_name=True)`.
- Optionality/nullability follows the Spec; string enums → `StrEnum`; integer enums → `IntEnum`; `date-time` → `datetime`; `date` → `date`.
- Spec descriptions become class docstrings; field descriptions become pydantic `Field(description=...)` values.
- A generated model never imports from `_generated.api`.

## Endpoint emission rules

- Signatures, bodies, pagination, and error behaviour follow [architecture.md](architecture.md) exactly.
- Body requiredness follows the model, not the Spec's `required` flag: a body whose model has required fields is always sent, and those fields are required keyword-only parameters. Bodies whose models have no required fields keep the any-field-provided guard (and send no body when all flat fields are `None`). No `cast(...)` or `# ty: ignore` is ever needed: parameters that feed required model fields are declared required.
- Methods call the runtime request hook; they perform no I/O themselves.
- Impersonation is never a generated keyword: `sudo` is client-scoped runtime state (`client.sudo`, `client.sudo_as()`), and the hook reads it when it builds the request. No method signature, docstring, or call site carries it.
- Every method docstring carries: one-line summary, description (HTML stripped), `Args` (from parameter descriptions), `Returns`, `Raises` (the mapped statuses), a deprecation note when applicable, and the `operationId` for tracing back to the Spec. `Returns` carries the Spec's response description only: the return type lives in the annotation on the signature, empty (204/205) responses read `No content.` instead of the Spec's schema boilerplate, and the section is omitted when there is nothing to say. `Args`/`Raises` entries are Google-style `name: description` pairs, and wrapped continuations are indented deeper than the entry so docstring parsers such as griffe do not read them as new entries.
- Generated modules import only from `pyfj._runtime`, `pyfj._generated.models`, and the standard library.

### Why `builtins.list` appears

This is deliberate, not a leftover:

- **`builtins.list[...]` in annotations**: namespace classes define a method named `list`, and type checkers resolve annotation names in class scope — plain `list[Model]` in such a class resolves to the method, not the builtin. The qualified form is the workaround. Renaming the `list` methods (a public API change) or using the deprecated `typing.List` style are the only alternatives; both were rejected.

## Regeneration workflow

```bash
uv run python -m codegen                 # regenerate
git diff --stat -- src/pyfj/_generated   # review
```

- Changes under `_generated/` are committed together with the generator/config change that caused them (or with the Spec bump).
- The CI `codegen-drift` job re-runs the generator and fails on any diff.

## Generator tests

- Unit: Spec loading, `$ref` resolution, IR edge cases; naming (collisions, overrides, deprecated); emission golden files against a synthetic mini-spec covering: required and optional flat bodies, `body_` collision prefixes, multipart, 204/205, text/plain, bytes, enums, dates, deprecated operations, collisions.
- Determinism: running the generator twice yields identical bytes.
- Drift: running on the real Spec reproduces the committed tree.

## Acceptance criteria

- [ ] Every operation accounted for: generated or excluded with a reason.
- [ ] `naming-report.md` reviewed; `mapping.toml` complete and commented.
- [ ] Golden tests cover every quirk row above.
- [ ] Drift check green in CI.
