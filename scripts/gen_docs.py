"""Generate the API reference pages and the site copies of CONTRIBUTING.md and CHANGELOG.md.

Run from anywhere with ``uv run python scripts/gen_docs.py``. The output is
committed and drift-checked in CI, exactly like the generated package tree.
"""

from __future__ import annotations

import ast
import importlib
import inspect
import json
import re
import shutil
import sys
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable

REPO_ROOT = Path(__file__).resolve().parents[1]
MODELS_DIR = REPO_ROOT / "src" / "pyfj" / "_generated" / "models"
API_DIR = REPO_ROOT / "src" / "pyfj" / "_generated" / "api"
API_PACKAGE = "pyfj._generated.api"
DOCS_DIR = REPO_ROOT / "docs"
REFERENCE_DIR = DOCS_DIR / "reference"
CONTRIBUTING_SOURCE = REPO_ROOT / "CONTRIBUTING.md"
CONTRIBUTING_PAGE = DOCS_DIR / "contributing.md"
CHANGELOG_SOURCE = REPO_ROOT / "CHANGELOG.md"
CHANGELOG_PAGE = DOCS_DIR / "changelog.md"

# CONTRIBUTING.md is written for the repository; the site copy needs site paths.
_LINK_REWRITES: tuple[tuple[str, str], ...] = (
    ("docs/development/", "development/"),
    ("docs/reference/", "reference/"),
    (
        "`CONTRIBUTING.md`",
        "[CONTRIBUTING.md](https://github.com/erdemhalil/forgejo-python/blob/main/CONTRIBUTING.md)",
    ),
)

_CAMEL_BOUNDARY = re.compile(r"(.)([A-Z][a-z]+)")
_ACRONYM_BOUNDARY = re.compile(r"([a-z0-9])([A-Z])")

# Sidebar labels: path segments are code-shaped, so the nav shows friendly names.
_ACRONYMS: dict[str, str] = {"api": "API", "gpg": "GPG", "oauth2": "OAuth2"}
_NAMESPACE_LABELS: dict[str, str] = {"activitypub": "ActivityPub"}
_NAMESPACE_SUMMARIES: dict[str, str] = {
    "activitypub": "Federation endpoints",
    "admin": "Instance administration",
    "misc": (
        "Standalone endpoints (version, licenses, markdown, markup, gitignore, label, nodeinfo, "
        "signing-key, topics, actions, ...)"
    ),
    "notifications": "Notification threads",
    "orgs": "Organizations",
    "packages": "Package registries and their files",
    "repos": "Repositories, issues, pull requests, releases, and everything under them",
    "settings": "Instance settings",
    "teams": "Teams, their members, and their repositories",
    "user": "The authenticated user",
    "users": "Other users",
}


def _humanize(segment: str) -> str:
    """A path segment as a sidebar label: ``public_members`` -> ``Public members``."""
    if segment in _NAMESPACE_LABELS:
        return _NAMESPACE_LABELS[segment]
    return " ".join(_ACRONYMS.get(word, word.capitalize()) for word in segment.split("_"))


def _snake(name: str) -> str:
    """``RepositoryObjectFormatName`` -> ``repository_object_format_name``; ``APIError`` -> ``api_error``."""
    return _ACRONYM_BOUNDARY.sub(r"\1_\2", _CAMEL_BOUNDARY.sub(r"\1_\2", name)).lower()


def _model_exports() -> dict[str, list[str]]:
    """Map each generated model module to the names ``models/__init__.py`` imports from it."""
    tree = ast.parse((MODELS_DIR / "__init__.py").read_text(encoding="utf-8"))
    exports: dict[str, list[str]] = {}
    for node in tree.body:
        if (
            isinstance(node, ast.ImportFrom)
            and node.module is not None
            and node.module.startswith("pyfj._generated.models.")
        ):
            module = node.module.rsplit(".", 1)[-1]
            exports.setdefault(module, []).extend(alias.name for alias in node.names)
    return exports


def _primary_name(module: str, names: Iterable[str]) -> str:
    candidates = list(names)
    match = next((name for name in candidates if _snake(name) == module), None)
    return match or min(candidates)


def _front_matter(title: str, description: str) -> list[str]:
    return [
        "---",
        f"title: {_yaml_string(title)}",
        f"description: {_yaml_string(description)}",
        "---",
        "",
    ]


def _yaml_string(value: str) -> str:
    """A double-quoted YAML scalar (JSON string syntax is a YAML subset)."""
    return json.dumps(value, ensure_ascii=False)


def _model_page(
    module: str, names: list[str], descriptions: dict[str, str], usages: dict[str, list[tuple[str, str, str]]]
) -> str:
    primary = _primary_name(module, names)
    lines = _front_matter(primary, descriptions[primary] or f"Generated model {primary}.")
    lines += [
        f"# {primary}",
        "",
        f"Import from `pyfj` or `pyfj.models` as `{primary}`.",
        "",
    ]
    for name in [primary, *(name for name in names if name != primary)]:
        lines += [f"::: pyfj._generated.models.{module}.{name}", ""]
    lines += _used_by_section(names, usages)
    return "\n".join(lines).rstrip() + "\n"


def _used_by_section(names: list[str], usages: dict[str, list[tuple[str, str, str]]]) -> list[str]:
    grouped: dict[str, list[tuple[str, str]]] = {}
    for name in names:
        for path, method, link in usages.get(name, ()):
            grouped.setdefault(path, []).append((method, link))
    if not grouped:
        return []
    lines = ["## Used by", "", "| Namespace | Operations |", "|---|---|"]
    for path in sorted(grouped):
        operations = " · ".join(f"[`{method}`]({link})" for method, link in sorted(grouped[path]))
        lines.append(f"| [`{path}`](../namespaces/{path.replace('.', '/')}/index.md) | {operations} |")
    lines.append("")
    return lines


def _namespace_page(path: str, module: str, sync_name: str, async_name: str) -> str:
    short_module = module.rsplit(".", 1)[-1]
    short_name = path.rsplit(".", 1)[-1]
    lines = _front_matter(path, f"API reference for `client.{path}` — sync and async.")
    lines += [
        f"# {short_name}",
        "",
        f"Accessed as `client.{path}`; the async client mirrors it.",
        "",
        '=== "Sync"',
        "",
        f"    ::: pyfj._generated.api.{short_module}.{sync_name}",
        "",
        '=== "Async"',
        "",
        f"    ::: pyfj._generated.api.{short_module}.{async_name}",
        "",
    ]
    return "\n".join(lines).rstrip() + "\n"


def _clients_page(top_level: list[str]) -> str:
    lines = _front_matter("Clients", "The synchronous and asynchronous entry points.")
    lines += [
        "# Clients",
        "",
        "The two entry points. Both are context managers and expose identical surfaces.",
        "",
        '=== "Sync"',
        "",
        "    ::: pyfj.Forgejo",
        "        options:",
        "          inherited_members: true",
        "          merge_init_into_class: true",
        "          members:",
        "            - request",
        "            - close",
        "            - sudo",
        "            - sudo_as",
        "",
        '=== "Async"',
        "",
        "    ::: pyfj.AsyncForgejo",
        "        options:",
        "          inherited_members: true",
        "          merge_init_into_class: true",
        "          members:",
        "            - request",
        "            - aclose",
        "            - sudo",
        "            - sudo_as",
        "",
        "## Namespaces",
        "",
        "Both clients expose one attribute per resource namespace:",
        "",
    ]
    for name in top_level:
        summary = _NAMESPACE_SUMMARIES.get(name)
        suffix = f" — {summary}" if summary else ""
        lines.append(f"- [`client.{name}`](namespaces/{name}/index.md){suffix}")
    lines.append("")
    return "\n".join(lines).rstrip() + "\n"


_ERROR_CLASSES: tuple[str, ...] = (
    "ForgejoError",
    "APIError",
    "TransportError",
    "DecodeError",
    "BadRequestError",
    "UnauthorizedError",
    "ForbiddenError",
    "NotFoundError",
    "MethodNotAllowedError",
    "ConflictError",
    "PreconditionFailedError",
    "PayloadTooLargeError",
    "UnprocessableEntityError",
    "LockedError",
    "ServerError",
)


def _runtime_page() -> str:
    lines = _front_matter(
        "Errors and pagination", "The exception hierarchy and the pagination wrappers returned by list operations."
    )
    lines += [
        "# Errors and pagination",
        "",
        "Non-2xx responses raise a typed exception; list operations return a lazy pagination wrapper.",
        "",
        "## Errors",
        "",
        (
            "All exceptions descend from `ForgejoError`. `APIError` carries `status_code`, `body`, and the raw "
            "`httpx2.Response`; transport failures raise `TransportError`, and responses that do not match the Spec "
            "raise `DecodeError`."
        ),
        "",
    ]
    for name in _ERROR_CLASSES:
        lines += [f"::: pyfj.{name}", ""]
    lines += [
        "## Pagination",
        "",
        (
            "List operations return `Paginated[T]` (sync) or `AsyncPaginated[T]` (async): iterating walks pages "
            "transparently, `.total_count` mirrors `X-Total-Count`, and `.page(n)` fetches a single page."
        ),
        "",
        "::: pyfj.Paginated",
        "    options:",
        "      members:",
        "        - total_count",
        "        - page",
        "",
        "::: pyfj.AsyncPaginated",
        "    options:",
        "      members:",
        "        - total_count",
        "        - page",
        "",
    ]
    return "\n".join(lines).rstrip() + "\n"


def _reference_index_page() -> str:
    lines = _front_matter("API reference", "Clients, namespaces, and models generated from the Forgejo 16 Spec.")
    lines += [
        "# API reference",
        "",
        "The generated surface, straight from the vendored Forgejo 16 Spec.",
        "",
        "- [Clients](clients.md) — `Forgejo` and `AsyncForgejo`.",
        "- [Errors and pagination](runtime.md) — the exception hierarchy and `Paginated`/`AsyncPaginated`.",
        "- [Namespaces](namespaces/index.md) — every resource, sync and async.",
        "- [Models](models/index.md) — the full catalogue; every model has its own page.",
        "",
    ]
    return "\n".join(lines).rstrip() + "\n"


def _namespaces_index_page(top_level: list[str]) -> str:
    lines = _front_matter("Namespaces", "Every resource namespace exposed by the clients, sync and async.")
    lines += [
        "# Namespaces",
        "",
        "Each page documents the synchronous class and its async mirror; operations nest under their resource.",
        "",
    ]
    lines += [
        f"- [{name}]({name}/index.md) — {_NAMESPACE_SUMMARIES.get(name, f'`client.{name}`')}" for name in top_level
    ]
    lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def _model_description(obj: object) -> str:
    if isinstance(obj, type):
        if obj.__module__ == "builtins":
            return f"Alias for `{obj.__name__}`."
        doc = inspect.getdoc(obj)
        return doc.splitlines()[0] if doc else ""
    return f"Type alias for `{obj}`."


def _models_catalog(exports: dict[str, list[str]], descriptions: dict[str, str]) -> str:
    rows: list[tuple[str, str, str]] = []
    for module, names in exports.items():
        for name in names:
            description = descriptions[name].replace("|", "\\|")
            rows.append((name, f"{module}.md#pyfj._generated.models.{module}.{name}", description))
    rows.sort(key=lambda row: row[0].casefold())

    lines = _front_matter("Models", "Every model, enum, and type alias generated from the Spec, alphabetically.")
    lines += [
        "# Models",
        "",
        "Every model, enum, and type alias generated from the Spec, alphabetically.",
        "",
    ]
    letters = sorted({name[0].upper() for name, _, _ in rows})
    lines += [" · ".join(f"[{letter}](#{letter.lower()})" for letter in letters), ""]
    current = ""
    for name, link, description in rows:
        letter = name[0].upper()
        if letter != current:
            current = letter
            lines += [f"## {letter}", ""]
        suffix = f" — {description}" if description else ""
        lines.append(f"- [`{name}`]({link}){suffix}")
    lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def _namespace_classes() -> set[type]:
    """Every sync namespace class, wherever it nests (the package only re-exports the top level)."""
    classes: set[type] = set()
    for path in sorted(API_DIR.glob("*.py")):
        if path.stem == "__init__":
            continue
        module = importlib.import_module(f"{API_PACKAGE}.{path.stem}")
        classes.update(
            value
            for value in vars(module).values()
            if isinstance(value, type)
            and value.__module__ == module.__name__
            and not value.__name__.startswith("Async")
        )
    return classes


def _annotation_names(node: ast.expr) -> set[str]:
    return {child.id for child in ast.walk(node) if isinstance(child, ast.Name)}


def _model_usages(pairs: dict[str, tuple[str, str]], model_names: set[str]) -> dict[str, list[tuple[str, str, str]]]:
    """For every model name, the generated operations whose signatures mention it."""
    class_paths = {sync_name: path for path, (_, sync_name) in pairs.items()}
    usages: dict[str, set[tuple[str, str, str]]] = {}
    for source in sorted(API_DIR.glob("*.py")):
        if source.stem == "__init__":
            continue
        tree = ast.parse(source.read_text(encoding="utf-8"))
        for node in tree.body:
            if not isinstance(node, ast.ClassDef) or node.name not in class_paths:
                continue
            path = class_paths[node.name]
            for fn in node.body:
                if not isinstance(fn, ast.FunctionDef) or fn.name == "__init__":
                    continue
                arguments = [*fn.args.posonlyargs, *fn.args.args, *fn.args.kwonlyargs]
                annotations = [argument.annotation for argument in arguments if argument.annotation is not None]
                if fn.returns is not None:
                    annotations.append(fn.returns)
                referenced: set[str] = set()
                for annotation in annotations:
                    referenced |= _annotation_names(annotation)
                anchor = f"pyfj._generated.api.{source.stem}.{node.name}.{fn.name}"
                link = f"../namespaces/{path.replace('.', '/')}/index.md#{anchor}"
                for name in referenced & model_names:
                    usages.setdefault(name, set()).add((path, fn.name, link))
    return {name: sorted(entries) for name, entries in usages.items()}


def _namespace_pairs() -> dict[str, tuple[str, str]]:
    """Every reachable namespace: dotted call path -> (module, sync class name)."""
    from pyfj._generated import api

    namespace_classes = _namespace_classes()

    client = api.Forgejo("https://example.invalid")
    pairs: dict[str, tuple[str, str]] = {}
    try:
        _walk_namespaces(client, "", namespace_classes, pairs)
    finally:
        client.close()
    return pairs


def _namespace_pages(pairs: dict[str, tuple[str, str]]) -> dict[Path, str]:
    pages: dict[Path, str] = {}
    for path in sorted(pairs):
        module, sync_name = pairs[path]
        async_name = f"Async{sync_name}"
        if not hasattr(importlib.import_module(module), async_name):
            message = f"{module}.{sync_name} has no {async_name} counterpart"
            raise ValueError(message)
        target = REFERENCE_DIR / "namespaces" / Path(*path.split(".")) / "index.md"
        pages[target] = _namespace_page(path, module, sync_name, async_name)
        children = '  - "*"\n' if any(other.startswith(f"{path}.") for other in pairs) else ""
        label = _humanize(path.rsplit(".", 1)[-1])
        pages[target.parent / ".nav.yml"] = f"title: {label}\nnav:\n  - index.md\n{children}"

    top_level = sorted(path for path in pairs if "." not in path)
    pages[REFERENCE_DIR / "namespaces" / "index.md"] = _namespaces_index_page(top_level)
    pages[REFERENCE_DIR / "namespaces" / ".nav.yml"] = 'nav:\n  - index.md\n  - "*"\n'
    return pages


def _walk_namespaces(obj: object, prefix: str, namespace_classes: set[type], pairs: dict[str, tuple[str, str]]) -> None:
    for attr in dir(obj):
        if attr.startswith("_"):
            continue
        try:
            value = getattr(obj, attr)
        except Exception:  # noqa: BLE001, S112 - namespace attributes are plain cached properties; skip anything else
            continue
        cls = type(value)
        if cls not in namespace_classes:
            continue
        path = f"{prefix}.{attr}" if prefix else attr
        if path in pairs:
            continue
        pairs[path] = (cls.__module__, cls.__name__)
        _walk_namespaces(value, path, namespace_classes, pairs)


def _contributing_page() -> str:
    text = CONTRIBUTING_SOURCE.read_text(encoding="utf-8")
    for source, target in _LINK_REWRITES:
        text = text.replace(source, target)
    return "\n".join(_front_matter("Contributing", "How to set up, test, and contribute to pyfj.")) + "\n" + text


def _changelog_page() -> str:
    text = CHANGELOG_SOURCE.read_text(encoding="utf-8")
    return "\n".join(_front_matter("Changelog", "Release notes for pyfj.")) + "\n" + text


def generate() -> list[Path]:
    """Regenerate reference pages plus the contributing/changelog copies; return written paths."""
    if REFERENCE_DIR.exists():
        shutil.rmtree(REFERENCE_DIR)

    pages: dict[Path, str] = {
        REFERENCE_DIR / "index.md": _reference_index_page(),
        REFERENCE_DIR / "runtime.md": _runtime_page(),
        REFERENCE_DIR / ".nav.yml": (
            "nav:\n  - index.md\n  - clients.md\n  - runtime.md\n  - namespaces\n  - models\n"
        ),
        REFERENCE_DIR / "models" / ".nav.yml": "nav:\n  - index.md\nappend_unmatched: false\n",
    }

    from pyfj import models as model_package

    exports = _model_exports()
    model_names = {name for names in exports.values() for name in names}
    pairs = _namespace_pairs()
    top_level = sorted(path for path in pairs if "." not in path)
    usages = _model_usages(pairs, model_names)
    descriptions = {
        name: _model_description(getattr(model_package, name)) for names in exports.values() for name in names
    }

    pages[REFERENCE_DIR / "clients.md"] = _clients_page(top_level)
    for module, names in exports.items():
        pages[REFERENCE_DIR / "models" / f"{module}.md"] = _model_page(module, names, descriptions, usages)
    pages[REFERENCE_DIR / "models" / "index.md"] = _models_catalog(exports, descriptions)

    pages.update(_namespace_pages(pairs))
    pages[CONTRIBUTING_PAGE] = _contributing_page()
    pages[CHANGELOG_PAGE] = _changelog_page()

    written: list[Path] = []
    for path in sorted(pages):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(pages[path], encoding="utf-8", newline="\n")
        written.append(path)
    return written


def main() -> int:
    written = generate()
    sys.stdout.write(f"generated {len(written)} docs files\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
