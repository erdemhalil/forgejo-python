"""Namespace and method naming for the generated API surface.

The algorithm is specified in ``docs/development/codegen.md``: namespaces come from the
path's static segments; parameter segments contribute method parameters, not
namespaces; the method name comes from the HTTP method and the path shape,
with action-style endpoints taking their name from the operationId's verb.
``mapping.toml`` overrides names; unresolved collisions fail the build.

Names are derived structurally, not from the Spec's tags:

- Top-level paths in :data:`TOP_LEVEL_NAMESPACES` keep their group name
  (``repos``, ``user``, ...); everything else is rooted at ``misc``.
- A trailing static segment is part of the namespace when it is a resource:
  it has child paths (``.../comments`` in ``.../comments/{id}``) or sibling
  operations on the same path (``.../forks`` with GET + POST). Otherwise it
  names the method (``.../{index}/merge`` -> ``merge``).
- A path ending in a parameter is item access: GET -> ``get``, PUT/PATCH ->
  ``update``, DELETE -> ``delete``; POST takes its verb from the operationId
  (``adminCronRun`` -> ``run``).
- A path ending in a resource segment derives the method from the HTTP
  method: GET -> ``list``, POST -> ``create`` (or the operationId's action
  verb), PUT/PATCH -> ``update``, DELETE -> ``delete``.
"""

from __future__ import annotations

import keyword
import re
import tomllib
from dataclasses import dataclass, field
from pathlib import Path
from typing import TYPE_CHECKING, Final

from codegen.ir import pascal_case, snake_case
from codegen.spec import SpecError

if TYPE_CHECKING:
    from collections.abc import Iterable, Mapping

    from codegen.ir import IR, Operation

__all__ = [
    "ACTION_VERBS",
    "MISC",
    "TOP_LEVEL_NAMESPACES",
    "EndpointName",
    "MethodOverride",
    "NamespaceOverride",
    "Naming",
    "Overrides",
    "Registry",
    "assign_names",
    "load_mapping",
    "load_registry",
    "operation_verb",
]

#: Path groups that keep their own top-level namespace; everything else is
#: rooted at :data:`MISC`. This is the reviewed grouping from architecture.md.
TOP_LEVEL_NAMESPACES: Final[frozenset[str]] = frozenset(
    {"repos", "user", "users", "orgs", "teams", "admin", "notifications", "packages", "settings", "activitypub"}
)
MISC: Final = "misc"

#: Verbs that name a method directly when the operation is an action.
ACTION_VERBS: Final[frozenset[str]] = frozenset(
    {
        "accept",
        "add",
        "adopt",
        "apply",
        "block",
        "cancel",
        "check",
        "clear",
        "conceal",
        "convert",
        "dismiss",
        "dispatch",
        "download",
        "follow",
        "fork",
        "generate",
        "link",
        "merge",
        "migrate",
        "mirror",
        "move",
        "pin",
        "publicize",
        "read",
        "register",
        "reject",
        "remove",
        "rename",
        "render",
        "replace",
        "reset",
        "run",
        "search",
        "set",
        "start",
        "stop",
        "submit",
        "sync",
        "test",
        "transfer",
        "unblock",
        "unlink",
        "unpin",
        "validate",
        "verify",
    }
)

#: Verbs that describe CRUD access; they never name an action method directly.
_STANDARD_VERBS: Final[frozenset[str]] = frozenset({"create", "delete", "edit", "get", "list", "post", "put", "update"})

_CAMEL_TOKEN: Final[re.Pattern[str]] = re.compile(r"[A-Z]+(?=[A-Z][a-z])|[A-Z]?[a-z0-9]+|[A-Z]+")
_IDENTIFIER: Final[re.Pattern[str]] = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")


@dataclass(frozen=True, slots=True)
class MethodOverride:
    """A ``[methods.<operationId>]`` entry."""

    name: str | None = None
    deprecated: bool | None = None


@dataclass(frozen=True, slots=True)
class NamespaceOverride:
    """A ``[namespaces."<path prefix>"]`` entry.

    ``name`` renames the path segment at that prefix; ``skip`` drops it from
    the namespace path entirely (for action segments that would otherwise
    become empty shells).
    """

    name: str | None = None
    skip: bool = False


@dataclass(frozen=True, slots=True)
class Overrides:
    """The parsed ``mapping.toml``."""

    namespaces: Mapping[str, NamespaceOverride] = field(default_factory=dict)
    methods: Mapping[str, MethodOverride] = field(default_factory=dict)
    models: Mapping[str, str] = field(default_factory=dict)


@dataclass(frozen=True, slots=True)
class Registry:
    """The parsed ``registry.toml``: operationId -> exclusion reason."""

    exclusions: Mapping[str, str] = field(default_factory=dict)


@dataclass(frozen=True, slots=True)
class EndpointName:
    """One operation's reviewed place on the public surface."""

    operation: Operation
    namespace: tuple[str, ...]
    method: str
    module: str
    class_name: str
    async_class_name: str
    deprecated: bool


@dataclass(frozen=True, slots=True)
class Naming:
    """The complete assignment: generated endpoints plus exclusions."""

    endpoints: tuple[EndpointName, ...]
    exclusions: tuple[tuple[Operation, str], ...]


def load_mapping(path: str | Path) -> Overrides:
    """Parse and validate ``mapping.toml`` (empty when the file is missing)."""
    source = Path(path)
    if not source.exists():
        return Overrides()
    raw = _load_toml(source)
    namespaces: dict[str, NamespaceOverride] = {}
    for prefix, entry in _table(raw, "namespaces", source).items():
        if not prefix.startswith("/"):
            message = f"{source}: namespace key {prefix!r} must be a path starting with '/'"
            raise SpecError(message)
        namespaces[prefix] = NamespaceOverride(
            name=_optional_name(entry, "name", f"namespaces.{prefix}", source),
            skip=_optional_bool(entry, "skip", f"namespaces.{prefix}", source),
        )
    methods: dict[str, MethodOverride] = {}
    for operation_id, entry in _table(raw, "methods", source).items():
        methods[operation_id] = MethodOverride(
            name=_optional_name(entry, "name", f"methods.{operation_id}", source),
            deprecated=_optional_bool_value(entry, "deprecated", f"methods.{operation_id}", source),
        )
    models = {name: _string(value, f"models.{name}", source) for name, value in _table(raw, "models", source).items()}
    return Overrides(namespaces=namespaces, methods=methods, models=models)


def load_registry(path: str | Path) -> Registry:
    """Parse and validate ``registry.toml`` (empty when the file is missing)."""
    source = Path(path)
    if not source.exists():
        return Registry()
    raw = _load_toml(source)
    entries = raw.get("exclusions")
    if entries is None:
        return Registry()
    if not isinstance(entries, list):
        message = f"{source}: 'exclusions' must be an array of tables"
        raise SpecError(message)
    exclusions: dict[str, str] = {}
    for index, entry in enumerate(entries):
        where = f"exclusions[{index}]"
        if not isinstance(entry, dict):
            message = f"{source}: {where} must be a table"
            raise SpecError(message)
        operation = _string(entry.get("operation"), f"{where}.operation", source)
        reason = _string(entry.get("reason"), f"{where}.reason", source)
        if operation in exclusions:
            message = f"{source}: {where} duplicates exclusion for {operation!r}"
            raise SpecError(message)
        exclusions[operation] = reason
    return Registry(exclusions=exclusions)


def operation_verb(operation_id: str) -> str | None:
    """Return the first verb token of ``operation_id`` (``adminCronRun`` -> ``run``)."""
    tokens: list[str] = _CAMEL_TOKEN.findall(operation_id)
    for token in tokens:
        lowered = token.lower()
        if lowered in ACTION_VERBS or lowered in _STANDARD_VERBS:
            return lowered
    return None


def assign_names(ir: IR, mapping: Overrides | None = None, registry: Registry | None = None) -> Naming:
    """Assign a namespace and method to every operation, failing on collisions.

    Args:
        ir: the built IR.
        mapping: parsed overrides; unknown operationIds or path prefixes fail.
        registry: parsed exclusions; unknown operationIds fail.

    Raises:
        SpecError: on unresolved collisions, unknown override keys, or
            collisions with Python identifiers.
    """
    mapping = mapping or Overrides()
    registry = registry or Registry()
    operations = {operation.operation_id: operation for operation in ir.operations}
    unknown = sorted(set(mapping.methods) - set(operations))
    if unknown:
        message = f"mapping.toml: method overrides for unknown operations: {unknown}"
        raise SpecError(message)
    unknown = sorted(set(registry.exclusions) - set(operations))
    if unknown:
        message = f"registry.toml: exclusions for unknown operations: {unknown}"
        raise SpecError(message)
    _validate_namespace_keys(ir.operations, mapping)

    paths = frozenset(operation.path for operation in ir.operations)
    path_counts: dict[str, int] = {}
    for operation in ir.operations:
        path_counts[operation.path] = path_counts.get(operation.path, 0) + 1
    endpoints: list[EndpointName] = []
    for operation in ir.operations:
        if operation.operation_id in registry.exclusions:
            continue
        endpoints.append(_name_operation(operation, paths, path_counts, mapping))
    _check_collisions(endpoints)
    _check_class_names(endpoints)
    exclusions = tuple(
        (operations[operation_id], reason) for operation_id, reason in sorted(registry.exclusions.items())
    )
    return Naming(endpoints=tuple(endpoints), exclusions=exclusions)


# ---------------------------------------------------------------------------
# Naming algorithm
# ---------------------------------------------------------------------------


def _name_operation(
    operation: Operation, paths: frozenset[str], path_counts: Mapping[str, int], mapping: Overrides
) -> EndpointName:
    namespace, method = _raw_name(operation, paths, path_counts, mapping.namespaces)
    override = mapping.methods.get(operation.operation_id)
    if override is not None and override.name is not None:
        method = override.name
    deprecated = operation.deprecated if override is None or override.deprecated is None else override.deprecated
    _validate_identifier(method, f"method name for {operation.operation_id!r}")
    for segment in namespace:
        _validate_identifier(segment, f"namespace segment for {operation.operation_id!r}")
    module = namespace[0]
    class_name = "".join(pascal_case(segment) for segment in namespace)
    return EndpointName(
        operation=operation,
        namespace=namespace,
        method=method,
        module=module,
        class_name=class_name,
        async_class_name=f"Async{class_name}",
        deprecated=deprecated,
    )


def _raw_name(
    operation: Operation,
    paths: frozenset[str],
    path_counts: Mapping[str, int],
    overrides: Mapping[str, NamespaceOverride],
) -> tuple[tuple[str, ...], str]:
    segments = operation.segments
    templates = [segment.template for segment in segments]
    static_names: list[str | None] = [
        _segment_name(segment.template, templates[: index + 1], overrides)
        for index, segment in enumerate(segments)
        if not segment.parameters
    ]
    names = [name for name in static_names if name is not None]
    raw_first = names[0] if names else None
    prefix: list[str] = [] if raw_first in TOP_LEVEL_NAMESPACES else [MISC]

    verb = operation_verb(operation.operation_id)
    if segments and segments[-1].parameters:
        # Item access: the trailing parameter identifies an existing resource.
        method = {"GET": "get", "PUT": "update", "PATCH": "update", "DELETE": "delete"}.get(
            operation.method, _action_verb(verb, fallback="create")
        )
        return tuple(prefix + names), method

    tail = snake_case(segments[-1].template) if segments else ""
    children = any(path != operation.path and path.startswith(f"{operation.path}/") for path in paths)
    siblings = path_counts.get(operation.path, 0) > 1
    if children or siblings:
        # A resource: the tail is a namespace, the method comes from the verb.
        if operation.method == "GET":
            method = "list"
        elif operation.method in {"PUT", "PATCH"}:
            method = "update"
        elif operation.method == "DELETE":
            method = "delete"
        else:
            method = _action_verb(verb, fallback="create", tail=tail)
        return tuple(prefix + names), method

    # An action leaf: the trailing segment names the method.
    return tuple(prefix + names[:-1]), tail


def _action_verb(verb: str | None, *, fallback: str, tail: str | None = None) -> str:
    """Pick a POST method name: the action verb unless it duplicates the resource name."""
    if verb is None or verb in _STANDARD_VERBS:
        return fallback
    if tail is not None and verb == tail:
        return fallback
    return verb


def _segment_name(template: str, prefix: list[str], overrides: Mapping[str, NamespaceOverride]) -> str | None:
    if not any(character.isalnum() for character in template):
        return None
    override = overrides.get("/" + "/".join(prefix))
    if override is not None:
        if override.skip:
            return None
        if override.name is not None:
            return override.name
    return snake_case(template)


def _validate_identifier(value: str, what: str) -> None:
    if not _IDENTIFIER.match(value) or keyword.iskeyword(value):
        message = f"{what}: {value!r} is not a valid identifier"
        raise SpecError(message)


def _validate_namespace_keys(operations: Iterable[Operation], mapping: Overrides) -> None:
    path_prefixes = set()
    for operation in operations:
        for index in range(1, len(operation.segments) + 1):
            path_prefixes.add("/" + "/".join(segment.template for segment in operation.segments[:index]))
    unknown = sorted(set(mapping.namespaces) - path_prefixes)
    if unknown:
        message = f"mapping.toml: namespace overrides for unknown path prefixes: {unknown}"
        raise SpecError(message)


# ---------------------------------------------------------------------------
# Collision checks
# ---------------------------------------------------------------------------


def _check_collisions(endpoints: Iterable[EndpointName]) -> None:
    methods: dict[tuple[str, ...], dict[str, str]] = {}
    children: dict[tuple[str, ...], dict[str, str]] = {}
    for endpoint in endpoints:
        namespace = endpoint.namespace
        existing = methods.setdefault(namespace, {})
        if endpoint.method in existing:
            message = (
                f"unresolved method collision in namespace {'.'.join(namespace)!r}: "
                f"{existing[endpoint.method]!r} and {endpoint.operation.operation_id!r} both name the method "
                f"{endpoint.method!r}; add a mapping.toml override"
            )
            raise SpecError(message)
        existing[endpoint.method] = endpoint.operation.operation_id
        for depth in range(1, len(namespace)):
            children.setdefault(namespace[:depth], {})[namespace[depth]] = endpoint.operation.operation_id
    for namespace, named_methods in methods.items():
        overlap = sorted(set(named_methods) & set(children.get(namespace, {})))
        if overlap:
            names = ", ".join(repr(name) for name in overlap)
            message = (
                f"unresolved attribute collision in namespace {'.'.join(namespace)!r}: "
                f"methods and child namespaces share the name(s) {names}; add a mapping.toml override"
            )
            raise SpecError(message)


def _check_class_names(endpoints: Iterable[EndpointName]) -> None:
    seen: dict[str, str] = {}
    for endpoint in endpoints:
        key = f"{endpoint.module}:{endpoint.class_name}"
        owner = seen.get(key)
        namespace = ".".join(endpoint.namespace)
        if owner is not None and owner != namespace:
            message = f"namespace classes collide: {owner!r} and {namespace!r} both map to {key!r}"
            raise SpecError(message)
        seen[key] = namespace


# ---------------------------------------------------------------------------
# TOML helpers
# ---------------------------------------------------------------------------


def _load_toml(source: Path) -> Mapping[str, object]:
    try:
        with source.open("rb") as file:
            return tomllib.load(file)
    except (OSError, tomllib.TOMLDecodeError) as exc:
        message = f"cannot read {source}: {exc}"
        raise SpecError(message) from exc


def _table(raw: Mapping[str, object], key: str, source: Path) -> Mapping[str, dict[str, object]]:
    value = raw.get(key, {})
    if not isinstance(value, dict):
        message = f"{source}: {key!r} must be a table"
        raise SpecError(message)
    table: dict[str, dict[str, object]] = {}
    for name, entry in value.items():
        if not isinstance(name, str) or not isinstance(entry, dict):
            message = f"{source}: {key}.{name} must be a table"
            raise SpecError(message)
        table[name] = {str(entry_key): entry_value for entry_key, entry_value in entry.items()}
    return table


def _string(value: object, where: str, source: Path) -> str:
    if not isinstance(value, str):
        message = f"{source}: {where} must be a string"
        raise SpecError(message)
    return value


def _optional_name(entry: Mapping[str, object], key: str, where: str, source: Path) -> str | None:
    value = entry.get(key)
    if value is None:
        return None
    return _string(value, f"{where}.{key}", source)


def _optional_bool(entry: Mapping[str, object], key: str, where: str, source: Path) -> bool:
    value = _optional_bool_value(entry, key, where, source)
    return value is True


def _optional_bool_value(entry: Mapping[str, object], key: str, where: str, source: Path) -> bool | None:
    value = entry.get(key)
    if value is None:
        return None
    if not isinstance(value, bool):
        message = f"{source}: {where}.{key} must be a boolean"
        raise SpecError(message)
    return value
