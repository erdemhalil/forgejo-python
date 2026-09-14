"""Semantic IR: models and operations, resolved from the validated Spec.

The IR is the generator's stable intermediate representation; the model
and API emitters read it and nothing else. Design choices the
emitter relies on:

- **Nullability is not modelled by the Spec** (there is no ``x-nullable`` and
  no OpenAPI 3 ``nullable``). Every non-required property is therefore typed
  ``T | None`` with a ``None`` default; required properties are bare ``T``.
  Spec-level ``default`` values are recorded in :class:`codegen.spec.Schema`
  but intentionally not applied to model fields.
- **Scalar, array, and alias definitions** (``StateType``, ``Duration``,
  ``IssueTemplateLabels``, ``CreatePullReviewCommentOptions``) become type
  aliases, not models; object definitions become pydantic models.
- **Inline enums and inline object properties** become named types owned by
  the module of the surrounding definition (``CreateHookOptionType``,
  ``QuotaUsedAttachmentContainedIn``); their names are globally unique and a
  collision fails the build rather than silently renaming.
- **Inline response objects** (three search endpoints carry a titled inline
  object) become top-level models named after ``title``; a collision with a
  definition fails the build.
"""

from __future__ import annotations

import keyword
import re
from dataclasses import dataclass
from typing import TYPE_CHECKING, Final, Literal, TypeAlias, cast

from codegen.spec import (
    HTTP_METHODS,
    UNSET,
    Schema,
    Spec,
    SpecError,
)
from codegen.spec import (
    Operation as SpecOperation,
)
from codegen.spec import (
    Parameter as SpecParameter,
)
from codegen.spec import (
    Response as SpecResponse,
)

if TYPE_CHECKING:
    from collections.abc import Iterator, Mapping

__all__ = [
    "IR",
    "Body",
    "EnumValue",
    "Field",
    "ListType",
    "MapType",
    "NamedRef",
    "Operation",
    "Parameter",
    "PathSegment",
    "Response",
    "ScalarType",
    "TypeDef",
    "TypeExpr",
    "build_ir",
    "enum_member_name",
    "pascal_case",
    "snake_case",
]

TypeKind: TypeAlias = Literal["model", "enum", "alias"]
ScalarKind: TypeAlias = Literal["string", "integer", "number", "boolean", "datetime", "date", "bytes", "any", "file"]
EnumBase: TypeAlias = Literal["str", "int"]
ParamLocation: TypeAlias = Literal["path", "query", "header", "formData"]

_CAMEL_BOUNDARY_1: Final = re.compile(r"(.)([A-Z][a-z]+)")
_CAMEL_BOUNDARY_2: Final = re.compile(r"([a-z0-9])([A-Z])")
_NON_IDENTIFIER: Final = re.compile(r"[^0-9A-Za-z]+")
_PATH_PARAMETER: Final = re.compile(r"\{([^{}]+)\}")
_DEFINITION_PREFIX: Final = "#/definitions/"
_STRING_FORMATS: Final[dict[str | None, ScalarKind]] = {
    "date-time": "datetime",
    "date": "date",
    "binary": "bytes",
}
_SIMPLE_KINDS: Final[dict[str, ScalarKind]] = {
    "integer": "integer",
    "number": "number",
    "boolean": "boolean",
}


# ---------------------------------------------------------------------------
# Naming
# ---------------------------------------------------------------------------


def snake_case(name: str) -> str:
    """Convert a wire name to a snake_case Python identifier.

    Non-identifier characters become separators (``@context`` -> ``context``),
    leading non-alphanumerics are dropped (``_links`` -> ``links``), a leading
    digit is prefixed with an underscore, and keywords gain a trailing
    underscore.
    """
    value = _CAMEL_BOUNDARY_1.sub(r"\1_\2", name)
    value = _CAMEL_BOUNDARY_2.sub(r"\1_\2", value)
    value = _NON_IDENTIFIER.sub("_", value).strip("_").lower()
    if not value:
        value = "field"
    if value[0].isdigit():
        value = f"_{value}"
    if keyword.iskeyword(value):
        value = f"{value}_"
    return value


def pascal_case(name: str) -> str:
    """Convert a wire name to a PascalCase identifier fragment."""
    parts = [part for part in _NON_IDENTIFIER.split(name) if part]
    return "".join(part[:1].upper() + part[1:] for part in parts) or "Type"


def enum_member_name(value: str | int) -> str:
    """Convert an enum value to an UPPER_SNAKE member name (``rebase-merge`` -> ``REBASE_MERGE``)."""
    text = str(value)
    text = _CAMEL_BOUNDARY_1.sub(r"\1_\2", text)
    text = _CAMEL_BOUNDARY_2.sub(r"\1_\2", text)
    member = _NON_IDENTIFIER.sub("_", text).strip("_").upper()
    if not member:
        message = f"enum value {value!r} has no usable member name"
        raise SpecError(message)
    if member[0].isdigit():
        member = f"_{member}"
    return member


def _validate_class_name(name: str, what: str) -> None:
    if not name.isidentifier() or keyword.iskeyword(name):
        message = f"{what}: {name!r} is not a valid Python class name"
        raise SpecError(message)


# ---------------------------------------------------------------------------
# Type expressions
# ---------------------------------------------------------------------------


@dataclass(frozen=True, slots=True)
class ScalarType:
    """A primitive type; ``enum`` carries raw values for operation parameters."""

    kind: ScalarKind
    format: str | None = None
    enum: tuple[object, ...] | None = None


@dataclass(frozen=True, slots=True)
class NamedRef:
    """A reference to a generated type by class name and module."""

    name: str
    module: str
    kind: TypeKind


@dataclass(frozen=True, slots=True)
class ListType:
    """An array type."""

    item: TypeExpr


@dataclass(frozen=True, slots=True)
class MapType:
    """An object with string keys and uniform values (``additionalProperties``)."""

    value: TypeExpr


TypeExpr: TypeAlias = ScalarType | NamedRef | ListType | MapType


# ---------------------------------------------------------------------------
# Types and operations
# ---------------------------------------------------------------------------


@dataclass(frozen=True, slots=True)
class EnumValue:
    """One enum member."""

    name: str
    value: str | int


@dataclass(frozen=True, slots=True)
class Field:
    """A model field; ``wire_name`` is the Spec property name (the alias source)."""

    name: str
    wire_name: str
    type: TypeExpr
    required: bool
    description: str | None = None


@dataclass(frozen=True, slots=True)
class TypeDef:
    """A generated type: a pydantic model, an enum, or a type alias."""

    name: str
    module: str
    kind: TypeKind
    spec_name: str
    description: str | None = None
    fields: tuple[Field, ...] = ()
    enum_values: tuple[EnumValue, ...] = ()
    enum_base: EnumBase | None = None
    alias_target: TypeExpr | None = None
    nested: tuple[TypeDef, ...] = ()


@dataclass(frozen=True, slots=True)
class PathSegment:
    """One path segment; ``template`` may embed one or more ``{parameters}``."""

    template: str
    parameters: tuple[str, ...] = ()


@dataclass(frozen=True, slots=True)
class Parameter:
    """A non-body operation parameter."""

    wire_name: str
    python_name: str
    location: ParamLocation
    type: TypeExpr
    required: bool
    description: str | None = None
    has_default: bool = False
    default: object | None = None
    collection_format: str | None = None


@dataclass(frozen=True, slots=True)
class Body:
    """A body parameter (Swagger ``in: body``)."""

    wire_name: str
    type: TypeExpr
    required: bool
    description: str | None = None
    consumes: tuple[str, ...] = ()


@dataclass(frozen=True, slots=True)
class Response:
    """A documented response; ``status`` is ``None`` for ``default``."""

    status: int | None
    description: str | None
    type: TypeExpr | None


@dataclass(frozen=True, slots=True)
class Operation:
    """One HTTP method + path pair, with everything the API emitter needs to emit a method."""

    operation_id: str
    method: str
    path: str
    segments: tuple[PathSegment, ...]
    parameters: tuple[Parameter, ...]
    body: Body | None
    responses: tuple[Response, ...]
    produces: tuple[str, ...]
    consumes: tuple[str, ...]
    deprecated: bool = False
    summary: str | None = None
    description: str | None = None
    tags: tuple[str, ...] = ()


@dataclass(frozen=True, slots=True)
class IR:
    """Everything the emitters consume."""

    title: str
    version: str
    base_path: str
    definitions: tuple[TypeDef, ...]
    """The 246 definition-backed types, ordered by Spec definition name."""

    types: tuple[TypeDef, ...]
    """Every top-level generated type (definitions plus inline response models), sorted by module."""

    types_by_name: Mapping[str, TypeDef]
    """Every generated type, including nested inline types, keyed by class name."""

    operations: tuple[Operation, ...]


# ---------------------------------------------------------------------------
# Builder
# ---------------------------------------------------------------------------


@dataclass(frozen=True, slots=True)
class _DefInfo:
    spec_name: str
    name: str
    module: str
    kind: TypeKind


def build_ir(spec: Spec, *, model_names: Mapping[str, str] | None = None) -> IR:
    """Build the IR from a validated Spec.

    Args:
        spec: a Spec returned by :func:`codegen.spec.load_spec`.
        model_names: optional ``definition name -> class name`` overrides
            (the runner wires ``mapping.toml`` into this); every key must name a
            definition and every value must be a unique class name.
    """
    return _Builder(spec, model_names or {}).build()


class _Builder:
    def __init__(self, spec: Spec, model_names: Mapping[str, str]) -> None:
        self.spec = spec
        self.model_names = dict(model_names)
        self._info: dict[str, _DefInfo] = {}
        self._modules: dict[str, str] = {}
        self._type_names: set[str] = set()
        self._operation_types: list[TypeDef] = []

    # -- top level ---------------------------------------------------------

    def build(self) -> IR:
        self._prepare_definitions()
        definitions = tuple(self._build_definition(name) for name in sorted(self._info))
        operations = self._build_operations()
        top_level = (*definitions, *self._operation_types)
        types = tuple(sorted(top_level, key=lambda type_def: (type_def.module, type_def.name)))
        by_name: dict[str, TypeDef] = {}
        for type_def in types:
            for node in iter_types(type_def):
                by_name[node.name] = node
        return IR(
            title=self.spec.title,
            version=self.spec.version,
            base_path=self.spec.base_path,
            definitions=definitions,
            types=types,
            types_by_name=dict(sorted(by_name.items())),
            operations=operations,
        )

    def _prepare_definitions(self) -> None:
        unknown = set(self.model_names) - set(self.spec.definitions)
        if unknown:
            message = f"model name overrides for unknown definitions: {sorted(unknown)}"
            raise SpecError(message)
        for spec_name, schema in self.spec.definitions.items():
            name = self.model_names.get(spec_name, spec_name)
            _validate_class_name(name, f"model name override for {spec_name!r}")
            module = snake_case(spec_name)
            self._register_top_level(name, module, spec_name)
            kind = _definition_kind(schema, spec_name)
            self._info[spec_name] = _DefInfo(spec_name=spec_name, name=name, module=module, kind=kind)

    def _register_top_level(self, name: str, module: str, spec_name: str) -> None:
        self._register_type_name(name, spec_name)
        owner = self._modules.get(module)
        if owner is not None:
            message = f"{spec_name!r}: module {module!r} is already used by {owner!r}"
            raise SpecError(message)
        self._modules[module] = spec_name

    def _register_type_name(self, name: str, spec_name: str) -> None:
        if name in self._type_names:
            message = f"{spec_name!r}: generated type name {name!r} collides with another generated type"
            raise SpecError(message)
        self._type_names.add(name)

    # -- definitions -------------------------------------------------------

    def _build_definition(self, spec_name: str) -> TypeDef:
        info = self._info[spec_name]
        schema = self.spec.definitions[spec_name]
        description = schema.description or schema.title
        if info.kind == "model":
            return self._build_model(info.name, info.module, schema, spec_name, description)
        if info.kind == "enum":
            return self._build_enum(info.name, info.module, schema, spec_name, description)
        return self._build_alias(info.name, info.module, schema, spec_name, description)

    def _build_model(
        self,
        name: str,
        module: str,
        schema: Schema,
        spec_name: str,
        description: str | None,
    ) -> TypeDef:
        fields: list[Field] = []
        nested: list[TypeDef] = []
        seen: dict[str, str] = {}
        required = set(schema.required)
        for wire_name, property_schema in schema.properties.items():
            field_name = snake_case(wire_name)
            if field_name in seen:
                message = (
                    f"{spec_name}: properties {seen[field_name]!r} and {wire_name!r} "
                    f"both map to Python field {field_name!r}"
                )
                raise SpecError(message)
            seen[field_name] = wire_name
            field_type = self._field_type(
                property_schema,
                module=module,
                owner=name,
                spec_name=f"{spec_name}.{wire_name}",
                nested=nested,
            )
            fields.append(
                Field(
                    name=field_name,
                    wire_name=wire_name,
                    type=field_type,
                    required=wire_name in required,
                    description=property_schema.description or property_schema.title,
                )
            )
        return TypeDef(
            name=name,
            module=module,
            kind="model",
            spec_name=spec_name,
            description=description,
            fields=tuple(fields),
            nested=tuple(nested),
        )

    def _build_enum(
        self,
        name: str,
        module: str,
        schema: Schema,
        spec_name: str,
        description: str | None,
    ) -> TypeDef:
        values = schema.enum or ()
        base = _enum_base(schema.type, values, spec_name)
        return TypeDef(
            name=name,
            module=module,
            kind="enum",
            spec_name=spec_name,
            description=description,
            enum_values=_enum_values(values, spec_name),
            enum_base=base,
        )

    def _build_alias(
        self,
        name: str,
        module: str,
        schema: Schema,
        spec_name: str,
        description: str | None,
    ) -> TypeDef:
        return TypeDef(
            name=name,
            module=module,
            kind="alias",
            spec_name=spec_name,
            description=description,
            alias_target=self._alias_target(schema, module=module, spec_name=spec_name),
        )

    def _alias_target(self, schema: Schema, *, module: str, spec_name: str) -> TypeExpr:
        if schema.ref is not None:
            return self._ref_type(schema.ref)
        if schema.type == "array":
            if schema.items is None:
                message = f"{spec_name}: array alias requires items"
                raise SpecError(message)
            return ListType(self._simple_type(schema.items, module=module, spec_name=f"{spec_name}.items"))
        if schema.enum is not None:
            return self._parameter_scalar(schema, spec_name=spec_name)
        return self._simple_type(schema, module=module, spec_name=spec_name)

    # -- schemas -----------------------------------------------------------

    def _field_type(
        self,
        schema: Schema,
        *,
        module: str,
        owner: str,
        spec_name: str,
        nested: list[TypeDef],
    ) -> TypeExpr:
        if schema.ref is not None:
            return self._ref_type(schema.ref)
        if schema.type == "array":
            if schema.items is None:
                message = f"{spec_name}: array property requires items"
                raise SpecError(message)
            return ListType(
                self._field_type(
                    schema.items, module=module, owner=owner, spec_name=f"{spec_name}.items", nested=nested
                )
            )
        return self._inline_field_type(schema, module=module, owner=owner, spec_name=spec_name, nested=nested)

    def _inline_field_type(
        self,
        schema: Schema,
        *,
        module: str,
        owner: str,
        spec_name: str,
        nested: list[TypeDef],
    ) -> TypeExpr:
        if schema.properties:
            class_name = f"{owner}{pascal_case(spec_name.rsplit('.', 1)[-1])}"
            self._register_type_name(class_name, spec_name)
            child = self._build_model(class_name, module, schema, spec_name, schema.description or schema.title)
            nested.append(child)
            return NamedRef(name=class_name, module=module, kind="model")
        if schema.type == "object" or schema.additional_properties is not None:
            return MapType(self._map_value(schema, module=module, spec_name=spec_name))
        if schema.enum is not None:
            return self._inline_enum(schema, module=module, owner=owner, spec_name=spec_name, nested=nested)
        return self._simple_type(schema, module=module, spec_name=spec_name)

    def _map_value(self, schema: Schema, *, module: str, spec_name: str) -> TypeExpr:
        additional = schema.additional_properties
        if isinstance(additional, Schema):
            return self._simple_type(additional, module=module, spec_name=f"{spec_name}.additionalProperties")
        return ScalarType("any")

    def _simple_type(self, schema: Schema, *, module: str, spec_name: str) -> TypeExpr:
        if schema.ref is not None:
            return self._ref_type(schema.ref)
        if schema.type == "array":
            if schema.items is None:
                message = f"{spec_name}: array requires items"
                raise SpecError(message)
            return ListType(self._simple_type(schema.items, module=module, spec_name=f"{spec_name}.items"))
        if schema.type == "object" or schema.additional_properties is not None:
            return MapType(self._map_value(schema, module=module, spec_name=spec_name))
        if schema.enum is not None:
            return self._parameter_scalar(schema, spec_name=spec_name)
        return _scalar_type(schema.type, schema.format, spec_name, file_is_bytes=True)

    def _inline_enum(
        self,
        schema: Schema,
        *,
        module: str,
        owner: str,
        spec_name: str,
        nested: list[TypeDef],
    ) -> NamedRef:
        values = schema.enum or ()
        base = _enum_base(schema.type, values, spec_name)
        class_name = f"{owner}{pascal_case(spec_name.rsplit('.', 1)[-1])}"
        self._register_type_name(class_name, spec_name)
        nested.append(
            TypeDef(
                name=class_name,
                module=module,
                kind="enum",
                spec_name=spec_name,
                description=schema.description or schema.title,
                enum_values=_enum_values(values, spec_name),
                enum_base=base,
            )
        )
        return NamedRef(name=class_name, module=module, kind="enum")

    def _parameter_scalar(self, schema: Schema, *, spec_name: str) -> ScalarType:
        scalar = _scalar_type(schema.type, schema.format, spec_name, file_is_bytes=False)
        if schema.enum is None:
            return scalar
        return ScalarType(kind=scalar.kind, format=scalar.format, enum=schema.enum)

    def _ref_type(self, ref: str) -> NamedRef:
        spec_name = ref.removeprefix(_DEFINITION_PREFIX)
        info = self._info.get(spec_name)
        if info is None:
            message = f"dangling $ref {ref!r}: no definition named {spec_name!r}"
            raise SpecError(message)
        return NamedRef(name=info.name, module=info.module, kind=info.kind)

    # -- operations --------------------------------------------------------

    def _build_operations(self) -> tuple[Operation, ...]:
        operations = [
            self._build_operation(path_item.parameters, spec_operation)
            for path_item in self.spec.paths
            for spec_operation in path_item.operations
        ]
        operations.sort(key=lambda operation: (operation.path, HTTP_METHODS.index(operation.method.lower())))
        return tuple(operations)

    def _build_operation(self, path_parameters: tuple[SpecParameter, ...], spec_operation: SpecOperation) -> Operation:
        merged: dict[tuple[str, str], SpecParameter] = {}
        for parameter in (*path_parameters, *spec_operation.parameters):
            merged[(parameter.name, parameter.location)] = parameter

        consumes = _dedupe(spec_operation.consumes if spec_operation.consumes is not None else self.spec.consumes)
        produces = _dedupe(spec_operation.produces if spec_operation.produces is not None else self.spec.produces)
        parameters: list[Parameter] = []
        body: Body | None = None
        for parameter in merged.values():
            where = f"paths.{spec_operation.path}.{spec_operation.method}.parameters.{parameter.name}"
            if parameter.location == "body":
                if parameter.schema is None:
                    message = f"{where}: body parameter is missing a schema"
                    raise SpecError(message)
                body = Body(
                    wire_name=parameter.name,
                    type=self._operation_schema_type(
                        parameter.schema, where=where, operation_id=spec_operation.operation_id, status=None
                    ),
                    required=parameter.required,
                    description=parameter.description,
                    consumes=consumes,
                )
                continue
            if parameter.type is None:
                message = f"{where}: parameter is missing a type"
                raise SpecError(message)
            parameters.append(
                Parameter(
                    wire_name=parameter.name,
                    python_name=snake_case(parameter.name),
                    location=parameter.location,
                    type=self._parameter_type(parameter, where=where),
                    required=parameter.required,
                    description=parameter.description,
                    has_default=parameter.default is not UNSET,
                    default=None if parameter.default is UNSET else parameter.default,
                    collection_format=parameter.collection_format,
                )
            )
        responses = tuple(self._build_response(response, spec_operation) for response in spec_operation.responses)
        return Operation(
            operation_id=spec_operation.operation_id,
            method=spec_operation.method,
            path=spec_operation.path,
            segments=_segments(spec_operation.path),
            parameters=tuple(parameters),
            body=body,
            responses=responses,
            produces=produces,
            consumes=consumes,
            deprecated=spec_operation.deprecated,
            summary=spec_operation.summary,
            description=spec_operation.description,
            tags=spec_operation.tags,
        )

    def _parameter_type(self, parameter: SpecParameter, *, where: str) -> TypeExpr:
        if parameter.type == "array":
            if parameter.items is None:
                message = f"{where}: array parameter requires items"
                raise SpecError(message)
            return ListType(self._parameter_scalar(parameter.items, spec_name=f"{where}.items"))
        return self._parameter_scalar(
            Schema(type=parameter.type, format=parameter.format, enum=parameter.enum), spec_name=where
        )

    def _build_response(self, response: SpecResponse, operation: SpecOperation) -> Response:
        where = f"paths.{operation.path}.{operation.method}.responses.{response.status}"
        type_expr = (
            None
            if response.schema is None
            else self._operation_schema_type(
                response.schema, where=where, operation_id=operation.operation_id, status=response.status
            )
        )
        return Response(status=response.status, description=response.description, type=type_expr)

    def _operation_schema_type(
        self,
        schema: Schema,
        *,
        where: str,
        operation_id: str,
        status: int | None,
    ) -> TypeExpr:
        if schema.ref is not None:
            return self._ref_type(schema.ref)
        if schema.type == "array":
            if schema.items is None:
                message = f"{where}: array schema requires items"
                raise SpecError(message)
            return ListType(
                self._operation_schema_type(
                    schema.items, where=f"{where}.items", operation_id=operation_id, status=status
                )
            )
        if schema.properties:
            return self._inline_operation_model(schema, where=where, operation_id=operation_id, status=status)
        if schema.type == "object" or schema.additional_properties is not None:
            return MapType(self._map_value(schema, module="", spec_name=where))
        if schema.enum is not None:
            return self._parameter_scalar(schema, spec_name=where)
        return _scalar_type(schema.type, schema.format, where, file_is_bytes=True)

    def _inline_operation_model(
        self,
        schema: Schema,
        *,
        where: str,
        operation_id: str,
        status: int | None,
    ) -> NamedRef:
        name = schema.title or f"{pascal_case(operation_id)}{status if status is not None else 'Default'}Response"
        _validate_class_name(name, where)
        module = snake_case(name)
        self._register_top_level(name, module, where)
        type_def = self._build_model(name, module, schema, where, schema.description or schema.title)
        self._operation_types.append(type_def)
        return NamedRef(name=name, module=module, kind="model")


def iter_types(type_def: TypeDef) -> Iterator[TypeDef]:
    """Yield ``type_def`` and its nested types, children before parents."""
    for child in type_def.nested:
        yield from iter_types(child)
    yield type_def


def _definition_kind(schema: Schema, spec_name: str) -> TypeKind:
    if schema.ref is not None:
        return "alias"
    if schema.enum is not None:
        return "enum"
    if schema.type == "object" or schema.properties:
        return "model"
    if schema.type in {"array", "string", "integer", "number", "boolean", "file"} or schema.type is None:
        return "alias"
    message = f"{spec_name}: unsupported definition type {schema.type!r}"
    raise SpecError(message)


def _enum_base(type_: str | None, values: tuple[object, ...], spec_name: str) -> EnumBase:
    if type_ in {None, "string"} and all(isinstance(value, str) for value in values):
        return "str"
    if type_ in {None, "integer"} and all(isinstance(value, int) and not isinstance(value, bool) for value in values):
        return "int"
    message = f"{spec_name}: unsupported enum of type {type_!r} with values {list(values)!r}"
    raise SpecError(message)


def _enum_values(values: tuple[object, ...], spec_name: str) -> tuple[EnumValue, ...]:
    members = [enum_member_name(cast("str | int", value)) for value in values]
    counts: dict[str, int] = {}
    for member in members:
        counts[member] = counts.get(member, 0) + 1
    duplicates = sorted(member for member, count in counts.items() if count > 1)
    if duplicates:
        message = f"{spec_name}: enum values collapse to duplicate member names {duplicates}"
        raise SpecError(message)
    return tuple(
        EnumValue(name=member, value=cast("str | int", value)) for member, value in zip(members, values, strict=True)
    )


# The ``file`` scalar kind is parameter-specific: form-data uploads stay
# ``file`` for the API emitter (multipart), while schema fields map to bytes.
def _scalar_type(type_: str | None, format_: str | None, spec_name: str, *, file_is_bytes: bool) -> ScalarType:
    if type_ == "string":
        return ScalarType(_STRING_FORMATS.get(format_, "string"), format=format_)
    if type_ == "file":
        return ScalarType("bytes" if file_is_bytes else "file", format=format_)
    if type_ is None:
        return ScalarType("any", format=format_)
    kind = _SIMPLE_KINDS.get(type_)
    if kind is None:
        message = f"{spec_name}: unsupported scalar type {type_!r}"
        raise SpecError(message)
    return ScalarType(kind, format=format_)


def _segments(path: str) -> tuple[PathSegment, ...]:
    return tuple(
        PathSegment(template=segment, parameters=tuple(_PATH_PARAMETER.findall(segment)))
        for segment in path.strip("/").split("/")
        if segment
    )


def _dedupe(values: tuple[str, ...]) -> tuple[str, ...]:
    seen: dict[str, None] = {}
    for value in values:
        seen.setdefault(value, None)
    return tuple(seen)
