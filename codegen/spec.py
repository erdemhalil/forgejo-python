"""Swagger 2.0 Spec loading, validation, and ``$ref`` resolution.

``spec/openapi.json`` is vendored and never hand-edited; this module is the
only place that knows its raw shape. Everything downstream works with the
typed nodes defined here, and :func:`load_spec` fails loudly (raising
:class:`SpecError` with a JSON path) on shapes it does not understand.

Supported reference sections: ``#/definitions/...`` (schemas),
``#/parameters/...`` (reusable parameters) and ``#/responses/...``
(reusable responses). References are resolved eagerly for parameters and
responses; schemas keep their reference until :mod:`codegen.ir` decides
whether the target is a model, an enum, or a type alias.
"""

from __future__ import annotations

import json
import re
from collections.abc import Iterator, Mapping, Sequence
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Final, Literal, TypeAlias, cast

__all__ = [
    "HTTP_METHODS",
    "UNSET",
    "Info",
    "Operation",
    "Parameter",
    "PathItem",
    "Response",
    "Schema",
    "Spec",
    "SpecError",
    "load_spec",
]

HTTP_METHODS: Final[tuple[str, ...]] = ("get", "put", "post", "delete", "options", "head", "patch")
Location: TypeAlias = Literal["query", "header", "path", "formData", "body"]

UNSET: Final[object] = object()

_SCHEMA_TYPES: Final[frozenset[str]] = frozenset({"string", "integer", "number", "boolean", "array", "object", "file"})
_LOCATIONS: Final[frozenset[str]] = frozenset({"query", "header", "path", "formData", "body"})
_COLLECTION_FORMATS: Final[frozenset[str]] = frozenset({"csv", "ssv", "tsv", "pipes", "multi"})
_STATUS_PATTERN: Final = re.compile(r"^[1-5][0-9]{2}$")

_ROOT_KEYS: Final[frozenset[str]] = frozenset(
    {
        "swagger",
        "info",
        "host",
        "basePath",
        "schemes",
        "consumes",
        "produces",
        "paths",
        "definitions",
        "parameters",
        "responses",
        "security",
        "securityDefinitions",
        "tags",
        "externalDocs",
    }
)
_INFO_KEYS: Final[frozenset[str]] = frozenset(
    {"title", "description", "termsOfService", "contact", "license", "version"}
)
_PATH_ITEM_KEYS: Final[frozenset[str]] = frozenset({*HTTP_METHODS, "$ref", "parameters"})
_OPERATION_KEYS: Final[frozenset[str]] = frozenset(
    {
        "tags",
        "summary",
        "description",
        "externalDocs",
        "operationId",
        "consumes",
        "produces",
        "parameters",
        "responses",
        "schemes",
        "deprecated",
        "security",
    }
)
_PARAMETER_KEYS: Final[frozenset[str]] = frozenset(
    {
        "name",
        "in",
        "description",
        "required",
        "type",
        "format",
        "allowEmptyValue",
        "items",
        "collectionFormat",
        "default",
        "maximum",
        "exclusiveMaximum",
        "minimum",
        "exclusiveMinimum",
        "maxLength",
        "minLength",
        "pattern",
        "maxItems",
        "minItems",
        "uniqueItems",
        "enum",
        "multipleOf",
        "schema",
    }
)
_SCHEMA_KEYS: Final[frozenset[str]] = frozenset(
    {
        "$ref",
        "format",
        "title",
        "description",
        "default",
        "multipleOf",
        "maximum",
        "exclusiveMaximum",
        "minimum",
        "exclusiveMinimum",
        "maxLength",
        "minLength",
        "pattern",
        "maxItems",
        "minItems",
        "uniqueItems",
        "maxProperties",
        "minProperties",
        "required",
        "enum",
        "type",
        "items",
        "allOf",
        "properties",
        "additionalProperties",
        "discriminator",
        "readOnly",
        "xml",
        "externalDocs",
        "example",
        "not",
    }
)
_RESPONSE_KEYS: Final[frozenset[str]] = frozenset({"$ref", "description", "schema", "headers", "examples"})
_COMBINATORS: Final[tuple[str, ...]] = ("allOf", "anyOf", "oneOf", "not")


class SpecError(Exception):
    """Raised when the Spec has a shape the generator does not understand."""


@dataclass(frozen=True, slots=True)
class Info:
    """The Spec's ``info`` object."""

    title: str
    version: str
    description: str | None = None


@dataclass(frozen=True, slots=True)
class Schema:
    """A (possibly referencing) Swagger schema node."""

    ref: str | None = None
    type: str | None = None
    format: str | None = None
    description: str | None = None
    title: str | None = None
    enum: tuple[object, ...] | None = None
    items: Schema | None = None
    properties: Mapping[str, Schema] = field(default_factory=dict)
    required: tuple[str, ...] = ()
    additional_properties: bool | Schema | None = None
    default: object = UNSET
    unique_items: bool = False


@dataclass(frozen=True, slots=True)
class Parameter:
    """A parameter; body parameters carry ``schema`` instead of ``type``."""

    name: str
    location: Location
    description: str | None = None
    required: bool = False
    type: str | None = None
    format: str | None = None
    items: Schema | None = None
    enum: tuple[object, ...] | None = None
    collection_format: str | None = None
    default: object = UNSET
    schema: Schema | None = None


@dataclass(frozen=True, slots=True)
class Response:
    """A response; ``status`` is ``None`` for ``default`` and top-level entries."""

    description: str | None = None
    schema: Schema | None = None
    status: int | None = None


@dataclass(frozen=True, slots=True)
class Operation:
    """One HTTP method + path pair (before naming)."""

    path: str
    method: str
    operation_id: str
    summary: str | None
    description: str | None
    tags: tuple[str, ...]
    consumes: tuple[str, ...] | None
    produces: tuple[str, ...] | None
    parameters: tuple[Parameter, ...]
    responses: tuple[Response, ...]
    deprecated: bool = False


@dataclass(frozen=True, slots=True)
class PathItem:
    """A path and the operations it carries; path-level parameters are shared."""

    path: str
    operations: tuple[Operation, ...]
    parameters: tuple[Parameter, ...] = ()


@dataclass(frozen=True, slots=True)
class Spec:
    """The parsed Spec, with ``$ref`` lookups for the three reference sections."""

    title: str
    version: str
    base_path: str
    consumes: tuple[str, ...]
    produces: tuple[str, ...]
    definitions: Mapping[str, Schema]
    parameters: Mapping[str, Parameter]
    responses: Mapping[str, Response]
    paths: tuple[PathItem, ...]

    def resolve_schema(self, ref: str) -> Schema:
        """Return the definition ``ref`` points at."""
        name = _ref_name(ref, "definitions")
        try:
            return self.definitions[name]
        except KeyError:
            message = f"dangling $ref {ref!r}: no definition named {name!r}"
            raise SpecError(message) from None

    def resolve_parameter(self, ref: str) -> Parameter:
        """Return the reusable parameter ``ref`` points at."""
        name = _ref_name(ref, "parameters")
        try:
            return self.parameters[name]
        except KeyError:
            message = f"dangling $ref {ref!r}: no reusable parameter named {name!r}"
            raise SpecError(message) from None

    def resolve_response(self, ref: str) -> Response:
        """Return the reusable response ``ref`` points at."""
        name = _ref_name(ref, "responses")
        try:
            return self.responses[name]
        except KeyError:
            message = f"dangling $ref {ref!r}: no reusable response named {name!r}"
            raise SpecError(message) from None


def load_spec(path: str | Path) -> Spec:
    """Read, validate, and index a Swagger 2.0 Spec.

    Raises:
        SpecError: the file cannot be read or parsed, is not Swagger 2.0, has
            an unexpected shape, contains an unsupported feature
            (``allOf``/``anyOf``/``oneOf``, ``x-nullable``, path-item
            ``$ref``, per-operation ``security``), or has a dangling ``$ref``.
    """
    source = Path(path)
    try:
        text = source.read_text(encoding="utf-8")
    except OSError as exc:
        message = f"cannot read Spec at {source}: {exc}"
        raise SpecError(message) from exc
    try:
        raw = json.loads(text)
    except json.JSONDecodeError as exc:
        message = f"{source}: invalid JSON: {exc}"
        raise SpecError(message) from exc
    spec = _parse_spec(raw, origin=str(source))
    _validate_refs(spec)
    return spec


# ---------------------------------------------------------------------------
# Parsing helpers
# ---------------------------------------------------------------------------


def _at(path: str, key: str) -> str:
    return f"{path}.{key}" if path else key


def _kind(value: object) -> str:
    if value is None:
        return "null"
    return type(value).__name__


def _mapping(value: object, path: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        message = f"{path}: expected an object, got {_kind(value)}"
        raise SpecError(message)
    return value


def _sequence(value: object, path: str) -> Sequence[Any]:
    if isinstance(value, str) or not isinstance(value, Sequence):
        message = f"{path}: expected an array, got {_kind(value)}"
        raise SpecError(message)
    return value


def _require(node: Mapping[str, Any], key: str, path: str) -> object:
    if key not in node:
        message = f"{_at(path, key)}: required key is missing"
        raise SpecError(message)
    return node[key]


def _string(value: object, path: str) -> str:
    if not isinstance(value, str):
        message = f"{path}: expected a string, got {_kind(value)}"
        raise SpecError(message)
    return value


def _required_string(node: Mapping[str, Any], key: str, path: str) -> str:
    return _string(_require(node, key, path), _at(path, key))


def _optional_string(node: Mapping[str, Any], key: str, path: str) -> str | None:
    if key not in node or node[key] is None:
        return None
    return _string(node[key], _at(path, key))


def _optional_bool(node: Mapping[str, Any], key: str, path: str) -> bool:
    if key not in node:
        return False
    value = node[key]
    if not isinstance(value, bool):
        message = f"{_at(path, key)}: expected a boolean, got {_kind(value)}"
        raise SpecError(message)
    return value


def _string_list(value: object, path: str) -> tuple[str, ...]:
    items = _sequence(value, path)
    return tuple(_string(item, f"{path}[{index}]") for index, item in enumerate(items))


def _check_keys(node: Mapping[str, Any], allowed: frozenset[str], path: str) -> None:
    for key in node:
        if key in {"x-nullable", "nullable"}:
            message = (
                f"{_at(path, key)}: nullability markers are not modelled; the Spec is expected to be nullable-free"
            )
            raise SpecError(message)
        if key.startswith("x-"):
            continue
        if key not in allowed:
            message = f"{_at(path, key)}: unexpected key {key!r}"
            raise SpecError(message)


def _ref_name(ref: str, section: str) -> str:
    prefix = f"#/{section}/"
    if not ref.startswith(prefix):
        message = f"unsupported $ref {ref!r}: expected a JSON pointer under {prefix!r}"
        raise SpecError(message)
    name = ref[len(prefix) :].replace("~1", "/").replace("~0", "~")
    if not name or "/" in name:
        message = f"unsupported $ref {ref!r}: expected a single {section} name"
        raise SpecError(message)
    return name


# ---------------------------------------------------------------------------
# Spec parsing
# ---------------------------------------------------------------------------


def _parse_spec(raw: object, origin: str) -> Spec:
    root = _mapping(raw, origin)
    _check_keys(root, _ROOT_KEYS, "")
    swagger = _required_string(root, "swagger", "")
    if swagger != "2.0":
        message = f"swagger: expected '2.0', got {swagger!r}; only Swagger 2.0 Specs are supported"
        raise SpecError(message)

    info = _mapping(root.get("info"), "info")
    _check_keys(info, _INFO_KEYS, "info")

    base_path = _optional_string(root, "basePath", "") or "/"
    if "schemes" in root:
        _string_list(root["schemes"], "schemes")

    definitions_node = _mapping(root.get("definitions", {}), "definitions")
    definitions = {name: _parse_schema(node, f"definitions.{name}") for name, node in definitions_node.items()}

    parameters_node = _mapping(root.get("parameters", {}), "parameters")
    parameters = {name: _parse_parameter(node, f"parameters.{name}") for name, node in parameters_node.items()}

    responses = _parse_reusable_responses(root.get("responses", {}))

    consumes = _string_list(root["consumes"], "consumes") if "consumes" in root else ()
    produces = _string_list(root["produces"], "produces") if "produces" in root else ()

    _validate_security(root.get("security"), "security")
    paths = _parse_paths(
        root.get("paths"),
        _Context(responses=responses, parameters=parameters, operation_ids=set()),
    )

    return Spec(
        title=_required_string(info, "title", "info"),
        version=_required_string(info, "version", "info"),
        base_path=base_path,
        consumes=consumes,
        produces=produces,
        definitions=definitions,
        parameters=parameters,
        responses=responses,
        paths=paths,
    )


def _validate_security(value: object, path: str) -> None:
    if value is None:
        return
    for index, requirement in enumerate(_sequence(value, path)):
        mapping = _mapping(requirement, f"{path}[{index}]")
        for scheme, scopes in mapping.items():
            if scopes is None:
                continue
            _string_list(scopes, f"{path}[{index}].{scheme}")


@dataclass(slots=True)
class _Context:
    """Mutable state shared while parsing paths and operations."""

    responses: Mapping[str, Response]
    parameters: Mapping[str, Parameter]
    operation_ids: set[str]


def _parse_paths(value: object, context: _Context) -> tuple[PathItem, ...]:
    if value is None:
        message = "paths: required key is missing"
        raise SpecError(message)
    paths_node = _mapping(value, "paths")
    items: list[PathItem] = []
    for path, node in paths_node.items():
        where = f"paths.{path}"
        if not path.startswith("/"):
            message = f"{where}: path must start with '/'"
            raise SpecError(message)
        item = _mapping(node, where)
        _check_keys(item, _PATH_ITEM_KEYS, where)
        if "$ref" in item:
            message = f"{where}: path-item $ref is not supported; inline the path item instead"
            raise SpecError(message)
        path_parameters = _parse_parameter_list(item.get("parameters"), f"{where}.parameters", context.parameters)
        operations: list[Operation] = []
        for method in HTTP_METHODS:
            if method not in item:
                continue
            operation = _parse_operation(item[method], path, method, context)
            operations.append(operation)
        if not operations:
            message = f"{where}: path item has no supported operations"
            raise SpecError(message)
        items.append(PathItem(path=path, operations=tuple(operations), parameters=path_parameters))
    return tuple(items)


def _parse_operation(value: object, path: str, method: str, context: _Context) -> Operation:
    where = f"paths.{path}.{method}"
    node = _mapping(value, where)
    _check_keys(node, _OPERATION_KEYS, where)
    if "security" in node:
        message = f"{where}: per-operation security is not supported; pyfj honours only the global security"
        raise SpecError(message)
    operation_id = _required_string(node, "operationId", where)
    if operation_id in context.operation_ids:
        message = f"{where}: duplicate operationId {operation_id!r}"
        raise SpecError(message)
    context.operation_ids.add(operation_id)
    parameters = _parse_parameter_list(node.get("parameters"), f"{where}.parameters", context.parameters)
    responses_node = _mapping(_require(node, "responses", where), f"{where}.responses")
    responses: list[Response] = []
    for code, entry in responses_node.items():
        if code.startswith("x-"):
            continue
        if code == "default":
            status = None
        elif _STATUS_PATTERN.match(code):
            status = int(code)
        else:
            message = f"{where}.responses.{code}: expected a 3-digit status code or 'default'"
            raise SpecError(message)
        parsed = _parse_response(entry, f"{where}.responses.{code}", context.responses)
        responses.append(Response(description=parsed.description, schema=parsed.schema, status=status))
    return Operation(
        path=path,
        method=method.upper(),
        operation_id=operation_id,
        summary=_optional_string(node, "summary", where),
        description=_optional_string(node, "description", where),
        tags=_string_list(node["tags"], f"{where}.tags") if "tags" in node else (),
        consumes=_string_list(node["consumes"], f"{where}.consumes") if "consumes" in node else None,
        produces=_string_list(node["produces"], f"{where}.produces") if "produces" in node else None,
        parameters=parameters,
        responses=tuple(responses),
        deprecated=_optional_bool(node, "deprecated", where),
    )


def _parse_parameter_list(
    value: object, path: str, reusable_parameters: Mapping[str, Parameter]
) -> tuple[Parameter, ...]:
    if value is None:
        return ()
    parameters: list[Parameter] = []
    seen: set[tuple[str, str]] = set()
    for index, entry in enumerate(_sequence(value, path)):
        where = f"{path}[{index}]"
        mapping = _mapping(entry, where)
        if "$ref" in mapping:
            ref = _required_string(mapping, "$ref", where)
            name = _ref_name(ref, "parameters")
            try:
                parameter = reusable_parameters[name]
            except KeyError:
                message = f"{where}: dangling $ref {ref!r}: no reusable parameter named {name!r}"
                raise SpecError(message) from None
        else:
            parameter = _parse_parameter(entry, where)
        key = (parameter.name, parameter.location)
        if key in seen:
            message = f"{where}: duplicate parameter {parameter.name!r} in {parameter.location!r}"
            raise SpecError(message)
        seen.add(key)
        parameters.append(parameter)
    return tuple(parameters)


def _parse_parameter(value: object, path: str) -> Parameter:
    node = _mapping(value, path)
    _check_keys(node, _PARAMETER_KEYS, path)
    name = _required_string(node, "name", path)
    location = _required_string(node, "in", path)
    if location not in _LOCATIONS:
        message = f"{path}.in: expected one of {sorted(_LOCATIONS)}, got {location!r}"
        raise SpecError(message)
    description = _optional_string(node, "description", path)
    required = _optional_bool(node, "required", path)
    if location == "body":
        if "schema" not in node:
            message = f"{path}: body parameter requires a schema"
            raise SpecError(message)
        schema = _parse_schema(node["schema"], f"{path}.schema")
        return Parameter(name=name, location="body", description=description, required=required, schema=schema)

    if "schema" in node:
        message = f"{path}: schema is only valid on body parameters"
        raise SpecError(message)
    type_ = _required_string(node, "type", path)
    if type_ not in _SCHEMA_TYPES:
        message = f"{path}.type: unsupported type {type_!r}"
        raise SpecError(message)
    items = _parse_schema(node["items"], f"{path}.items") if "items" in node else None
    if type_ == "array" and items is None:
        message = f"{path}: array parameter requires items"
        raise SpecError(message)
    enum = _parse_enum(node["enum"], f"{path}.enum") if "enum" in node else None
    collection_format = _optional_string(node, "collectionFormat", path)
    if collection_format is not None and collection_format not in _COLLECTION_FORMATS:
        message = f"{path}.collectionFormat: unsupported format {collection_format!r}"
        raise SpecError(message)
    return Parameter(
        name=name,
        location=cast("Location", location),
        description=description,
        required=required,
        type=type_,
        format=_optional_string(node, "format", path),
        items=items,
        enum=enum,
        collection_format=collection_format,
        default=node.get("default", UNSET),
    )


def _parse_response_body(node: Mapping[str, Any], path: str) -> Response:
    """Parse a response without a ``$ref`` (both inline and reusable share this shape)."""
    if "headers" in node:
        _mapping(node["headers"], f"{path}.headers")
    schema = _parse_schema(node["schema"], f"{path}.schema") if "schema" in node else None
    return Response(description=_optional_string(node, "description", path), schema=schema)


def _parse_response(value: object, path: str, reusable_responses: Mapping[str, Response]) -> Response:
    node = _mapping(value, path)
    _check_keys(node, _RESPONSE_KEYS, path)
    if "$ref" in node:
        ref = _required_string(node, "$ref", path)
        name = _ref_name(ref, "responses")
        try:
            return reusable_responses[name]
        except KeyError:
            message = f"{path}: dangling $ref {ref!r}: no reusable response named {name!r}"
            raise SpecError(message) from None
    return _parse_response_body(node, path)


def _parse_reusable_responses(value: object) -> Mapping[str, Response]:
    node = _mapping(value, "responses")
    raw: dict[str, Mapping[str, Any]] = {}
    for name, entry in node.items():
        raw[name] = _mapping(entry, f"responses.{name}")
    parsed: dict[str, Response] = {}
    resolving: set[str] = set()

    def resolve(name: str) -> Response:
        if name in parsed:
            return parsed[name]
        if name in resolving:
            message = f"responses.{name}: circular reusable response reference"
            raise SpecError(message)
        entry = raw[name]
        where = f"responses.{name}"
        resolving.add(name)
        try:
            _check_keys(entry, _RESPONSE_KEYS, where)
            if "$ref" in entry:
                ref = _required_string(entry, "$ref", where)
                target = _ref_name(ref, "responses")
                if target not in raw:
                    message = f"{where}: dangling $ref {ref!r}: no reusable response named {target!r}"
                    raise SpecError(message)
                response = resolve(target)
            else:
                response = _parse_response_body(entry, where)
        finally:
            resolving.discard(name)
        parsed[name] = response
        return response

    for name in raw:
        resolve(name)
    return parsed


def _parse_properties(node: Mapping[str, Any], path: str) -> dict[str, Schema]:
    if "properties" not in node:
        return {}
    properties_node = _mapping(node["properties"], f"{path}.properties")
    return {name: _parse_schema(entry, f"{path}.properties.{name}") for name, entry in properties_node.items()}


def _parse_additional_properties(node: Mapping[str, Any], path: str) -> bool | Schema | None:
    if "additionalProperties" not in node:
        return None
    raw_additional = node["additionalProperties"]
    if isinstance(raw_additional, bool):
        return raw_additional
    return _parse_schema(raw_additional, f"{path}.additionalProperties")


def _parse_schema(value: object, path: str) -> Schema:
    node = _mapping(value, path)
    _check_keys(node, _SCHEMA_KEYS, path)
    for combinator in _COMBINATORS:
        if combinator in node:
            message = f"{path}: schema combinator {combinator!r} is not supported; the Spec is expected to be flat"
            raise SpecError(message)
    if "$ref" in node:
        ref = _required_string(node, "$ref", path)
        _ref_name(ref, "definitions")
        siblings = {key for key in node if key not in {"$ref", "description", "title"} and not key.startswith("x-")}
        if siblings:
            message = f"{path}: $ref cannot be combined with {sorted(siblings)}"
            raise SpecError(message)
        return Schema(
            ref=ref,
            description=_optional_string(node, "description", path),
            title=_optional_string(node, "title", path),
        )

    type_ = _optional_string(node, "type", path)
    if type_ is not None and type_ not in _SCHEMA_TYPES:
        message = f"{path}.type: unsupported type {type_!r}"
        raise SpecError(message)
    properties = _parse_properties(node, path)
    required = _string_list(node["required"], f"{path}.required") if "required" in node else ()
    for name in required:
        if name not in properties:
            message = f"{path}.required: {name!r} is not one of the declared properties"
            raise SpecError(message)
    items = _parse_schema(node["items"], f"{path}.items") if "items" in node else None
    if type_ == "array" and items is None:
        message = f"{path}: array schema requires items"
        raise SpecError(message)
    return Schema(
        type=type_,
        format=_optional_string(node, "format", path),
        description=_optional_string(node, "description", path),
        title=_optional_string(node, "title", path),
        enum=_parse_enum(node["enum"], f"{path}.enum") if "enum" in node else None,
        items=items,
        properties=properties,
        required=required,
        additional_properties=_parse_additional_properties(node, path),
        default=node.get("default", UNSET),
        unique_items=_optional_bool(node, "uniqueItems", path),
    )


def _parse_enum(value: object, path: str) -> tuple[object, ...]:
    entries = _sequence(value, path)
    if not entries:
        message = f"{path}: enum must not be empty"
        raise SpecError(message)
    for index, entry in enumerate(entries):
        if not isinstance(entry, (str, int, float, bool)):
            message = f"{path}[{index}]: enum values must be strings or numbers, got {_kind(entry)}"
            raise SpecError(message)
    return tuple(entries)


# ---------------------------------------------------------------------------
# Reference validation
# ---------------------------------------------------------------------------


def _parameter_schemas(parameter: Parameter, path: str) -> Iterator[tuple[Schema, str]]:
    if parameter.schema is not None:
        yield parameter.schema, f"{path}.schema"
    if parameter.items is not None:
        yield parameter.items, f"{path}.items"


def _root_schemas(spec: Spec) -> Iterator[tuple[Schema, str]]:
    for name, schema in spec.definitions.items():
        yield schema, f"definitions.{name}"
    for name, parameter in spec.parameters.items():
        yield from _parameter_schemas(parameter, f"parameters.{name}")
    for name, response in spec.responses.items():
        if response.schema is not None:
            yield response.schema, f"responses.{name}.schema"
    for item in spec.paths:
        for parameter in item.parameters:
            yield from _parameter_schemas(parameter, f"paths.{item.path}.parameters")
        for operation in item.operations:
            for parameter in operation.parameters:
                yield from _parameter_schemas(parameter, f"paths.{item.path}.{operation.method}.parameters")
            for response in operation.responses:
                if response.schema is not None:
                    yield response.schema, f"paths.{item.path}.{operation.method}.responses.{response.status}"


def _validate_refs(spec: Spec) -> None:
    for schema, path in _root_schemas(spec):
        _validate_schema_refs(spec, schema, path)


def _validate_schema_refs(spec: Spec, schema: Schema, path: str) -> None:
    if schema.ref is not None:
        spec.resolve_schema(schema.ref)
        return
    if schema.items is not None:
        _validate_schema_refs(spec, schema.items, f"{path}.items")
    for name, property_schema in schema.properties.items():
        _validate_schema_refs(spec, property_schema, f"{path}.properties.{name}")
    if isinstance(schema.additional_properties, Schema):
        _validate_schema_refs(spec, schema.additional_properties, f"{path}.additionalProperties")
