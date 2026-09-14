---
title: "Contributing"
description: "How to set up, test, and contribute to pyfj."
---

# Contributing to pyfj

Thanks for considering a contribution. This page covers setup, the checks every change must pass, and the rules that are specific to this repository.

## Setup

pyfj targets Python 3.11+ and is managed with [uv](https://docs.astral.sh/uv/):

```bash
git clone https://github.com/erdemhalil/forgejo-python
cd forgejo-python
uv sync
```

Documentation work additionally needs the docs group:

```bash
uv sync --group docs
uv run zensical serve
```

## Checks

Every change must leave the tree green:

```bash
uv run ruff check . && uv run ruff format --check .
uv run ty check
uv run pytest                    # unit tests; no network, no Docker
uv run pytest -m integration     # Docker and a Forgejo container
uv run zensical build --strict   # documentation changes
```

CI runs the same checks plus a Python 3.11–3.14 matrix, codegen drift, and the docs build.

## Generated code

`src/pyfj/_generated/**` is generated. Never edit it by hand: change `codegen/` (or `codegen/mapping.toml`), then run

```bash
uv run python -m codegen
```

and commit both sides together. `spec/openapi.json` is vendored and never hand-edited — the Spec is the source of truth.

Generated diffs are reviewed deliberately: a naming-report change is a public API change.

## Documentation

The site is built from `docs/` and deployed from CI. User pages live at the top level, engineering reference under `development/`. The API reference under `reference/**` is generated — edit `scripts/gen_docs.py`, never the pages.

[CONTRIBUTING.md](https://github.com/erdemhalil/forgejo-python/blob/main/CONTRIBUTING.md) is the canonical contributor page; the docs generator copies it into the site.

## Pull requests

- Write imperative, sentence-case commit subjects.
- Keep one logical change per commit; generated code and the generator change that produced it ship together.
- Describe the user-visible effect in the pull request, and link the issue it closes when there is one.

## License

pyfj is MIT-licensed. By contributing, you agree that your contribution is licensed under the same terms.
