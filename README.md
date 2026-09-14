# pyfj

A fully typed Python client for the [Forgejo](https://forgejo.org) API — async-first, with a complete sync mirror.

## Install

```bash
uv add forgejo-python
```

or with pip:

```bash
pip install forgejo-python
```

The distribution is `forgejo-python`; the import name is `pyfj`:

```python
from pyfj import Forgejo

with Forgejo("https://codeberg.org", token="...") as client:
    repo = client.repos.get("forgejo", "forgejo")
    for issue in client.repos.issues.list("forgejo", "forgejo", state="open"):
        print(f"#{issue.number} {issue.title}")
```

## What it is

- **Complete**: every operation in the Forgejo 16 API is callable, generated from a vendored spec.
- **Typed**: pydantic v2 models for every schema, annotations everywhere, `py.typed`.
- **Dual**: `Forgejo` (sync) and `AsyncForgejo` (async) over httpx, identical surfaces.
- **Ergonomic**: resource namespaces (`client.repos.issues.create(...)`), keyword arguments, lazy `Paginated[T]` lists, typed exceptions.
- **Reproducible**: the generated surface is committed and CI fails on drift from the spec.
- **Tested against a real forge**: unit tests plus integration tests against a Forgejo container.

## Documentation

The documentation site lives at <https://erdemhalil.github.io/forgejo-python/>: getting started, guides, the generated API reference, and the engineering docs. It is versioned — `stable` tracks releases, `dev` tracks `main`.

In-repo references:

- [Architecture](docs/development/architecture.md) — public surface, runtime behaviour, policies
- [Code generation](docs/development/codegen.md) — how the spec becomes the surface
- [Contributing](CONTRIBUTING.md) — setup, checks, and PR expectations

## License

MIT
