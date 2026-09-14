"""API emission: one module per top-level namespace, sync and async classes.

``emit_api`` writes ``src/pyfj/_generated/api/**`` from the IR and the naming
assignment, plus the reviewed ``codegen/naming-report.md``. Rendering is
deterministic; the runner finishes with ``ruff format`` so the tree is
formatted with the repository's configuration.

Generated modules import only from ``pyfj._runtime``,
``pyfj._generated.models``, and the standard library. Namespace methods call
the frozen ``_request`` / ``_paginate`` hooks and ``decode``; they never touch
httpx2 directly. Response shapes outside ``decode``'s overloads (booleans,
string lists, maps) are parsed with an inline JSON step that raises
:class:`~pyfj._runtime.DecodeError` on failure.
"""

from __future__ import annotations

import html
import json
import re
import textwrap
import unicodedata
from dataclasses import dataclass, field, replace
from pathlib import Path
from typing import TYPE_CHECKING, Final

from codegen.ir import (
    ListType,
    MapType,
    NamedRef,
    ScalarType,
    pascal_case,
    snake_case,
)
from codegen.naming import (
    EndpointName,
    Naming,
    Overrides,
    Registry,
    assign_names,
    load_mapping,
    load_registry,
)

if TYPE_CHECKING:
    from collections.abc import Iterable, Sequence

    from codegen.ir import IR, Field, Operation, Parameter, Response, TypeExpr

__all__ = [
    "BodyPlan",
    "EndpointPlan",
    "ParamPlan",
    "ResponsePlan",
    "emit_api",
    "plan_endpoints",
    "render_report",
]

_LINE_LENGTH: Final = 120
_MAX_ARGS: Final = 5
# Google-style entry sections: each entry is ``name: description`` and wrapped continuations must be
# indented deeper than the entry, or parsers such as griffe read them as new entries and fail.
_DOCSTRING_ENTRY_SECTIONS: Final[frozenset[str]] = frozenset({"Args:", "Raises:"})
_DOCSTRING_CONTINUATION_INDENT: Final = 4
_HTTP_OK_MIN: Final = 200
_HTTP_OK_MAX: Final = 300
_HTTP_SERVER_ERROR_MIN: Final = 500
_HTTP_SERVER_ERROR_MAX: Final = 600
_BINARY_PRODUCES: Final[tuple[str, ...]] = ("zip", "octet-stream", "gzip")
_ERROR_CLASSES: Final[dict[int, str]] = {
    400: "BadRequestError",
    401: "UnauthorizedError",
    403: "ForbiddenError",
    404: "NotFoundError",
    405: "MethodNotAllowedError",
    409: "ConflictError",
    412: "PreconditionFailedError",
    413: "PayloadTooLargeError",
    422: "UnprocessableEntityError",
    423: "LockedError",
}
_SCALAR_NAMES: Final[dict[str, str]] = {
    "string": "str",
    "integer": "int",
    "number": "float",
    "boolean": "bool",
    "datetime": "datetime",
    "date": "date",
    "bytes": "bytes",
    "file": "FilePart",
    "any": "object",
}
# Scalar kinds `decode` accepts as a top-level response or inside list/dict responses.
_DECODABLE_SCALARS: Final[frozenset[str]] = frozenset({"string", "integer", "number", "boolean"})
_METHOD_ORDER: Final[dict[str, int]] = {"GET": 0, "POST": 1, "PUT": 2, "PATCH": 3, "DELETE": 4}
_FILE_PART: Final = (
    "FilePart = FileContent | tuple[str | None, FileContent]"
    " | tuple[str | None, FileContent, str | None]"
    " | tuple[str | None, FileContent, str | None, Mapping[str, str]]"
)

_TAG: Final = re.compile(r"<[^>]+>")
_BREAK: Final = re.compile(r"<br\s*/?>|</p>", re.IGNORECASE)
_UNKNOWN_NAMESPACE: Final = "unknown namespace class"
_MISSING_ELEMENT: Final = "paginated response is missing its element type"
_NO_MODEL_BODY: Final = "endpoint has no model body"


# ---------------------------------------------------------------------------
# Plans
# ---------------------------------------------------------------------------


@dataclass(frozen=True, slots=True)
class ParamPlan:
    """One generated method parameter (path, query, or form field)."""

    wire_name: str
    name: str
    location: str
    annotation: str
    required: bool
    description: str | None
    is_datetime: bool = False
    is_file: bool = False


@dataclass(frozen=True, slots=True)
class FlatField:
    """One flat body field: the model field and the keyword it is exposed as."""

    field: Field
    parameter: str


@dataclass(frozen=True, slots=True)
class BodyPlan:
    """How a request body is exposed on the method."""

    model: NamedRef | None = None
    flat: tuple[FlatField, ...] = ()
    required: bool = False
    enforced: bool = False
    passthrough: bool = False
    raw_annotation: str | None = None
    raw_name: str | None = None


@dataclass(frozen=True, slots=True)
class ResponsePlan:
    """How the success response is decoded and annotated."""

    annotation: str
    decode: str
    description: str | None
    models: tuple[NamedRef, ...] = ()
    element: NamedRef | None = None


@dataclass(frozen=True, slots=True)
class EndpointPlan:
    """Everything needed to render one sync and one async method."""

    name: EndpointName
    operation: Operation
    module: str
    class_name: str
    async_class_name: str
    method_name: str
    path_params: tuple[ParamPlan, ...]
    query_params: tuple[ParamPlan, ...]
    form_params: tuple[ParamPlan, ...]
    body: BodyPlan | None
    response: ResponsePlan
    paginated: bool
    page_limit: bool

    @property
    def call_params(self) -> tuple[ParamPlan, ...]:
        return (*self.path_params, *self.query_params, *self.form_params)


class _Aliases:
    """Model-name aliases for one module (avoids clashing with namespace classes)."""

    def __init__(self, class_names: set[str]) -> None:
        self.class_names = class_names

    def model(self, name: str) -> str:
        return f"{name}Model" if name in self.class_names else name


# ---------------------------------------------------------------------------
# Emission
# ---------------------------------------------------------------------------


def emit_api(
    ir: IR,
    out_dir: str | Path,
    *,
    mapping: Overrides | None = None,
    registry: Registry | None = None,
    report_path: str | Path | None = None,
) -> list[Path]:
    """Write the API modules and the naming report; return the module paths.

    ``mapping``/``registry`` default to the checked-in ``codegen`` files;
    ``report_path`` defaults to ``codegen/naming-report.md``.
    """
    codegen_dir = Path(__file__).resolve().parent
    mapping = mapping if mapping is not None else load_mapping(codegen_dir / "mapping.toml")
    registry = registry if registry is not None else load_registry(codegen_dir / "registry.toml")
    naming = assign_names(ir, mapping, registry)
    plans = plan_endpoints(naming, ir)

    directory = Path(out_dir)
    directory.mkdir(parents=True, exist_ok=True)
    files = _render_modules(plans)
    written: list[Path] = []
    for name in sorted(files):
        path = directory / name
        path.write_text(files[name], encoding="utf-8", newline="\n")
        written.append(path)
    for stale in sorted(directory.glob("*.py")):
        if stale.name not in files:
            stale.unlink()

    report = Path(report_path) if report_path is not None else codegen_dir / "naming-report.md"
    report.write_text(render_report(naming, plans, mapping=mapping, registry=registry), encoding="utf-8", newline="\n")
    return written


def plan_endpoints(naming: Naming, ir: IR) -> tuple[EndpointPlan, ...]:
    """Turn the naming assignment into render-ready endpoint plans."""
    class_names: dict[str, set[str]] = {}
    referenced: dict[str, set[str]] = {}
    for name in naming.endpoints:
        class_names.setdefault(name.module, set()).update({name.class_name, name.async_class_name})
        referenced.setdefault(name.module, set()).add(name.class_name)
    aliases = {module: _Aliases(names) for module, names in class_names.items()}
    return tuple(_plan_endpoint(name, ir, aliases[name.module]) for name in naming.endpoints)


def _plan_endpoint(name: EndpointName, ir: IR, aliases: _Aliases) -> EndpointPlan:
    operation = name.operation
    path_params = _path_params(operation)
    other_params = [parameter for parameter in operation.parameters if parameter.location != "path"]
    query_params = [_param_plan(parameter) for parameter in other_params if parameter.location == "query"]
    form_params = [_param_plan(parameter) for parameter in other_params if parameter.location == "formData"]
    param_names = {param.name for param in (*path_params, *query_params, *form_params)}
    duplicates = _duplicates([param.name for param in (*path_params, *query_params, *form_params)])
    if duplicates:
        message = f"{operation.operation_id}: parameters collapse to duplicate names {duplicates}"
        raise ValueError(message)

    response = _response_plan(operation, ir, aliases)
    page_limit = {parameter.wire_name for parameter in operation.parameters if parameter.location == "query"} >= {
        "page",
        "limit",
    }
    paginated = False
    if page_limit and response.element is not None:
        paginated = True
        response = ResponsePlan(
            annotation=f"Paginated[{aliases.model(response.element.name)}]",
            decode=response.decode,
            description=response.description,
            models=response.models,
            element=response.element,
        )
    reserved = {"page", "limit"} if page_limit else set()
    body = _body_plan(operation, param_names | reserved, ir)
    if paginated:
        query_params = [param for param in query_params if param.name not in {"page", "limit"}]
    return EndpointPlan(
        name=name,
        operation=operation,
        module=name.module,
        class_name=name.class_name,
        async_class_name=name.async_class_name,
        method_name=name.method,
        path_params=tuple(path_params),
        query_params=tuple(query_params),
        form_params=tuple(form_params),
        body=body,
        response=response,
        paginated=paginated,
        page_limit=page_limit,
    )


def _duplicates(values: Iterable[str]) -> list[str]:
    seen: dict[str, int] = {}
    for value in values:
        seen[value] = seen.get(value, 0) + 1
    return sorted(value for value, count in seen.items() if count > 1)


def _path_params(operation: Operation) -> list[ParamPlan]:
    by_wire = {parameter.wire_name: parameter for parameter in operation.parameters if parameter.location == "path"}
    plans: list[ParamPlan] = []
    seen: set[str] = set()
    for segment in operation.segments:
        for wire_name in segment.parameters:
            parameter = by_wire.get(wire_name)
            if parameter is None:
                message = f"{operation.operation_id}: path parameter {wire_name!r} is not declared"
                raise ValueError(message)
            if wire_name in seen:
                continue
            seen.add(wire_name)
            plans.append(_param_plan(parameter))
    extra = sorted(set(by_wire) - seen)
    if extra:
        message = f"{operation.operation_id}: declared path parameters missing from the path: {extra}"
        raise ValueError(message)
    return plans


def _param_plan(parameter: Parameter) -> ParamPlan:
    type_expr = parameter.type
    is_datetime = isinstance(type_expr, ScalarType) and type_expr.kind in {"datetime", "date"}
    is_file = isinstance(type_expr, ScalarType) and type_expr.kind == "file"
    return ParamPlan(
        wire_name=parameter.wire_name,
        name=parameter.python_name,
        location=parameter.location,
        annotation=_annotation(type_expr),
        required=parameter.required,
        description=parameter.description,
        is_datetime=is_datetime,
        is_file=is_file,
    )


def _body_plan(operation: Operation, reserved: set[str], ir: IR) -> BodyPlan | None:
    body = operation.body
    if body is None:
        return None
    name = snake_case(body.wire_name) if body.wire_name else "body"
    if name in reserved:
        name = "body"
    resolved = _resolve_alias(body.type, ir)
    if isinstance(resolved, NamedRef) and resolved.kind == "model":
        model = ir.types_by_name[resolved.name]
        fields = tuple(replace(model_field, type=_resolve_alias(model_field.type, ir)) for model_field in model.fields)
        if not fields and not body.required:
            # A fieldless model body has no flat field to expose; keep the whole model passable.
            return BodyPlan(model=resolved, raw_name=name, passthrough=True)
        flat = tuple(
            FlatField(field=model_field, parameter=_body_field_name(model_field.name, reserved))
            for model_field in fields
        )
        duplicates = _duplicates(flat_field.parameter for flat_field in flat)
        if duplicates:
            message = f"{operation.operation_id}: body fields collapse to duplicate names {duplicates}"
            raise ValueError(message)
        # A model with required fields cannot be built without them, so the body
        # is effectively required even when the Spec marks it optional.
        enforced = body.required or any(model_field.required for model_field in fields)
        return BodyPlan(
            model=resolved,
            flat=flat,
            required=body.required,
            enforced=enforced,
        )
    return BodyPlan(
        model=None,
        required=body.required,
        raw_name=name,
        raw_annotation=_annotation(resolved),
    )


def _body_field_name(name: str, reserved: set[str]) -> str:
    """Expose a body field as a keyword; fields colliding with another parameter get a ``body_`` prefix."""
    return f"body_{name}" if name in reserved else name


def _response_plan(operation: Operation, ir: IR, aliases: _Aliases) -> ResponsePlan:
    success = sorted(
        (
            response
            for response in operation.responses
            if response.status is not None and _HTTP_OK_MIN <= response.status < _HTTP_OK_MAX
        ),
        key=lambda response: response.status if response.status is not None else 0,
    )
    if not success:
        message = f"{operation.operation_id}: no documented 2xx response"
        raise ValueError(message)
    none_only = all(response.status in {204, 205} for response in success)
    typed = next((response for response in success if response.type is not None), None)
    if none_only:
        return ResponsePlan(annotation="None", decode="None", description=success[0].description)
    if typed is None or typed.type is None:
        return _no_content_plan(success[0], operation)
    resolved = _resolve_alias(typed.type, ir)
    returns_none = any(response.status in {204, 205} for response in success)
    plan = _typed_response_plan(resolved, typed, operation, ir, aliases)
    if returns_none and plan.annotation != "None":
        plan = ResponsePlan(
            annotation=f"{plan.annotation} | None",
            decode=plan.decode,
            description=plan.description,
            models=plan.models,
            element=plan.element,
        )
    return plan


def _no_content_plan(response: Response, operation: Operation) -> ResponsePlan:
    media_types = operation.produces
    if any(marker in media_type for media_type in media_types for marker in _BINARY_PRODUCES):
        return ResponsePlan(annotation="bytes", decode="bytes", description=response.description)
    has_json = any(media_type == "application/json" or media_type.endswith("+json") for media_type in media_types)
    if not has_json and any(media_type.startswith("text/") for media_type in media_types):
        return ResponsePlan(annotation="str", decode="str", description=response.description)
    return ResponsePlan(annotation="None", decode="None", description=response.description)


def _typed_response_plan(
    type_expr: TypeExpr, response: Response, operation: Operation, ir: IR, aliases: _Aliases
) -> ResponsePlan:
    if isinstance(type_expr, NamedRef):
        if type_expr.kind != "model":
            message = f"{operation.operation_id}: response references non-model type {type_expr.name!r}"
            raise ValueError(message)
        return ResponsePlan(
            annotation=aliases.model(type_expr.name),
            decode=aliases.model(type_expr.name),
            description=response.description,
            models=(type_expr,),
        )
    if isinstance(type_expr, ListType):
        item = _resolve_alias(type_expr.item, ir)
        if isinstance(item, NamedRef) and item.kind == "model":
            name = aliases.model(item.name)
            return ResponsePlan(
                annotation=f"builtins.list[{name}]",
                decode=f"list[{name}]",
                description=response.description,
                models=(item,),
                element=item,
            )
        if isinstance(item, ScalarType) and item.kind in _DECODABLE_SCALARS:
            name = _annotation(item)
            return ResponsePlan(
                annotation=f"builtins.list[{name}]",
                decode=f"list[{name}]",
                description=response.description,
            )
    if (
        isinstance(type_expr, MapType)
        and isinstance(type_expr.value, ScalarType)
        and type_expr.value.kind in _DECODABLE_SCALARS
    ):
        name = _annotation(type_expr.value)
        return ResponsePlan(
            annotation=f"dict[str, {name}]",
            decode=f"dict[str, {name}]",
            description=response.description,
        )
    if isinstance(type_expr, ScalarType) and (type_expr.kind == "bytes" or type_expr.kind in _DECODABLE_SCALARS):
        name = _annotation(type_expr)
        return ResponsePlan(annotation=name, decode=name, description=response.description)
    message = f"{operation.operation_id}: unsupported response type {type_expr!r}"
    raise ValueError(message)


def _resolve_alias(expr: TypeExpr, ir: IR) -> TypeExpr:
    seen: set[str] = set()
    while isinstance(expr, NamedRef) and expr.kind == "alias":
        if expr.name in seen:
            message = f"circular alias {expr.name!r}"
            raise ValueError(message)
        seen.add(expr.name)
        target = ir.types_by_name[expr.name].alias_target
        if target is None:
            message = f"alias {expr.name!r} has no target"
            raise ValueError(message)
        expr = target
    return expr


def _annotation(expr: TypeExpr) -> str:
    if isinstance(expr, ScalarType):
        if expr.enum:
            return f"Literal[{', '.join(_literal(value) for value in expr.enum)}]"
        return _SCALAR_NAMES[expr.kind]
    if isinstance(expr, NamedRef):
        return expr.name
    if isinstance(expr, ListType):
        # Qualified because namespace classes define a `list` method, which type checkers resolve in class scope.
        return f"builtins.list[{_annotation(expr.item)}]"
    if isinstance(expr, MapType):
        return f"dict[str, {_annotation(expr.value)}]"
    message = f"unsupported type expression: {expr!r}"
    raise TypeError(message)


def _display_annotation(annotation: str) -> str:
    """Render an annotation for docstrings/reports (``builtins.list`` -> ``list``)."""
    return annotation.replace("builtins.list[", "list[")


def _literal(value: object) -> str:
    if isinstance(value, str):
        return json.dumps(value, ensure_ascii=False)
    return repr(value)


# ---------------------------------------------------------------------------
# Module rendering
# ---------------------------------------------------------------------------


def _render_modules(plans: Sequence[EndpointPlan]) -> dict[str, str]:
    modules: dict[str, list[EndpointPlan]] = {}
    for plan in plans:
        modules.setdefault(plan.module, []).append(plan)
    files = {f"{module}.py": _render_namespace_module(module, module_plans) for module, module_plans in modules.items()}
    files["__init__.py"] = _render_api_init(tuple(sorted(modules)))
    return files


def _render_namespace_module(module: str, plans: Sequence[EndpointPlan]) -> str:
    classes = _namespace_classes(plans)
    class_names = set(classes) | {f"Async{class_name}" for class_name in classes}
    aliases = _Aliases(class_names)
    imports = _collect_imports(module, plans, aliases)
    blocks: list[str] = [
        f'"""Generated resource namespaces for the ``{module}`` group. Do not edit by hand.',
        "",
        "Regenerate with ``python -m codegen``; see docs/development/codegen.md.",
        '"""',
        "",
        "from __future__ import annotations",
        "",
    ]
    blocks.extend(_import_lines(imports))
    blocks.append("")
    for class_name in classes:
        blocks.extend(_render_class(class_name, plans, aliases, async_=False))
        blocks.append("")
        blocks.extend(_render_class(class_name, plans, aliases, async_=True))
        blocks.append("")
    return "\n".join(blocks).rstrip("\n") + "\n"


@dataclass(slots=True)
class _ModuleImports:
    runtime_models: dict[str, dict[str, str]] = field(default_factory=dict)
    typing_models: dict[str, dict[str, str]] = field(default_factory=dict)
    decode: bool = False
    paginated: bool = False
    literal: bool = False
    datetime: bool = False
    date: bool = False
    file_part: bool = False
    builtins: bool = False

    def add_runtime(self, ref: NamedRef, aliases: _Aliases) -> None:
        self.runtime_models.setdefault(ref.module, {})[aliases.model(ref.name)] = ref.name

    def add_typing(self, ref: NamedRef, aliases: _Aliases) -> None:
        alias = aliases.model(ref.name)
        if alias in self.runtime_models.get(ref.module, {}):
            return
        self.typing_models.setdefault(ref.module, {})[alias] = ref.name


def _collect_imports(module: str, plans: Sequence[EndpointPlan], aliases: _Aliases) -> _ModuleImports:
    imports = _ModuleImports()
    for plan in plans:
        _collect_response_imports(plan, imports, aliases)
        _collect_param_imports(plan, imports)
        _collect_body_imports(plan, imports, aliases)
    for model_module, names in list(imports.typing_models.items()):
        runtime = imports.runtime_models.get(model_module, {})
        for alias in [alias for alias in names if alias in runtime]:
            del names[alias]
        if not names:
            del imports.typing_models[model_module]
    return imports


def _collect_response_imports(plan: EndpointPlan, imports: _ModuleImports, aliases: _Aliases) -> None:
    if "builtins.list[" in plan.response.annotation:
        imports.builtins = True
    for ref in plan.response.models:
        imports.add_runtime(ref, aliases)
    if plan.paginated:
        imports.paginated = True
    else:
        imports.decode = True


def _collect_param_imports(plan: EndpointPlan, imports: _ModuleImports) -> None:
    for param in plan.call_params:
        if "Literal[" in param.annotation:
            imports.literal = True
        if "builtins.list[" in param.annotation:
            imports.builtins = True
        if param.is_datetime:
            if param.annotation == "date":
                imports.date = True
            else:
                imports.datetime = True
        if param.is_file:
            imports.file_part = True


def _collect_body_imports(plan: EndpointPlan, imports: _ModuleImports, aliases: _Aliases) -> None:
    body = plan.body
    if body is None:
        return
    if body.model is not None:
        if body.passthrough:
            imports.add_typing(body.model, aliases)
        else:
            imports.add_runtime(body.model, aliases)
    for flat_field in body.flat:
        if "builtins.list[" in _annotation(flat_field.field.type):
            imports.builtins = True
        for ref in _iter_refs(flat_field.field.type):
            imports.add_typing(ref, aliases)
        if _contains_kind(flat_field.field.type, "datetime"):
            imports.datetime = True
        elif _contains_kind(flat_field.field.type, "date"):
            imports.date = True


def _iter_refs(expr: TypeExpr) -> Iterable[NamedRef]:
    if isinstance(expr, NamedRef):
        if expr.kind == "alias":
            return
        yield expr
        return
    if isinstance(expr, ListType):
        yield from _iter_refs(expr.item)
        return
    if isinstance(expr, MapType):
        yield from _iter_refs(expr.value)


def _contains_kind(expr: TypeExpr, kind: str) -> bool:
    if isinstance(expr, ScalarType):
        return expr.kind == kind
    if isinstance(expr, ListType):
        return _contains_kind(expr.item, kind)
    if isinstance(expr, MapType):
        return _contains_kind(expr.value, kind)
    return False


def _import_lines(imports: _ModuleImports) -> list[str]:
    lines: list[str] = []
    typing_names = ["TYPE_CHECKING"]
    lines.append(f"from typing import {', '.join(typing_names)}")
    lines.append("")
    model_lines = _model_import_lines(imports.runtime_models)
    runtime_names: list[str] = []
    if imports.decode:
        runtime_names.append("decode")
    if model_lines or runtime_names:
        if model_lines:
            lines.extend(model_lines)
        if runtime_names:
            lines.append(f"from pyfj._runtime import {', '.join(sorted(runtime_names))}")
    lines.append("")
    lines.append("if TYPE_CHECKING:")
    stdlib: list[str] = []
    if imports.builtins:
        stdlib.append("import builtins")
    if imports.file_part:
        stdlib.append("from collections.abc import Mapping")
    names: list[str] = []
    if imports.date:
        names.append("date")
    if imports.datetime:
        names.append("datetime")
    if names:
        stdlib.append(f"from datetime import {', '.join(names)}")
    if imports.literal:
        stdlib.append("from typing import Literal")
    first_party: list[str] = []
    first_party.extend(_model_import_lines(imports.typing_models))
    first_party.append("from pyfj._runtime import AsyncForgejo as _RuntimeAsyncForgejo")
    if imports.paginated:
        first_party.append("from pyfj._runtime import AsyncPaginated, Paginated")
    first_party.append("from pyfj._runtime import Forgejo as _RuntimeForgejo")
    typing_lines: list[str] = list(stdlib)
    if stdlib:
        typing_lines.append("")
    typing_lines.extend(first_party)
    if imports.file_part:
        typing_lines.append("")
        typing_lines.append("FileContent = bytes | str")
        typing_lines.append(_FILE_PART)
    lines.extend(f"    {line}" if line else "" for line in typing_lines)
    return lines


def _model_import_lines(models: dict[str, dict[str, str]]) -> list[str]:
    lines: list[str] = []
    for module in sorted(models):
        names = []
        for alias, source in sorted(models[module].items()):
            names.append(source if alias == source else f"{source} as {alias}")
        lines.append(f"from pyfj._generated.models.{module} import {', '.join(names)}")
    return lines


def _namespace_classes(plans: Sequence[EndpointPlan]) -> list[str]:
    """Every sync namespace class name in a module, sorted."""
    names: dict[str, None] = {}
    for plan in plans:
        parts = plan.name.namespace
        for depth in range(len(parts), 0, -1):
            names.setdefault("".join(pascal_case(part) for part in parts[:depth]), None)
    return sorted(names)


def _render_class(class_name: str, plans: Sequence[EndpointPlan], aliases: _Aliases, *, async_: bool) -> list[str]:
    render_name = f"Async{class_name}" if async_ else class_name
    base = "_RuntimeAsyncForgejo" if async_ else "_RuntimeForgejo"
    children = _child_namespaces(class_name, plans)
    lines = [f"class {render_name}:", f'    """The ``{".".join(_namespace_of(class_name, plans))}`` namespace."""', ""]
    lines.append(f"    def __init__(self, client: {base}) -> None:")
    lines.append("        self._client = client")
    for attribute, child_class in children:
        child_name = f"Async{child_class}" if async_ else child_class
        lines.append(f"        self.{attribute}: {child_name} = {child_name}(client)")
    lines.append("")
    methods = sorted(
        (plan for plan in plans if (plan.async_class_name if async_ else plan.class_name) == render_name),
        key=_method_order,
    )
    for plan in methods:
        lines.extend(_render_method(plan, async_=async_, aliases=aliases))
        lines.append("")
    return lines


def _namespace_of(class_name: str, plans: Sequence[EndpointPlan]) -> tuple[str, ...]:
    for plan in plans:
        parts = plan.name.namespace
        for depth in range(1, len(parts) + 1):
            if "".join(pascal_case(part) for part in parts[:depth]) == class_name:
                return parts[:depth]
    raise ValueError(_UNKNOWN_NAMESPACE)


def _child_namespaces(class_name: str, plans: Sequence[EndpointPlan]) -> list[tuple[str, str]]:
    seen: dict[str, str] = {}
    for plan in plans:
        parts = plan.name.namespace
        for depth in range(1, len(parts)):
            if "".join(pascal_case(part) for part in parts[:depth]) != class_name:
                continue
            seen[parts[depth]] = "".join(pascal_case(part) for part in parts[: depth + 1])
    return sorted(seen.items())


def _method_order(plan: EndpointPlan) -> tuple[str, int, str]:
    return (plan.operation.path, _METHOD_ORDER.get(plan.operation.method, 99), plan.operation.operation_id)


def _render_method(plan: EndpointPlan, *, async_: bool, aliases: _Aliases) -> list[str]:
    keyword = "async def" if async_ else "def"
    annotation = plan.response.annotation
    if async_ and annotation.startswith("Paginated["):
        annotation = f"Async{annotation}"
    parameters = _method_parameters(plan, aliases)
    lines = _render_signature(keyword, plan.method_name, parameters, annotation)
    lines.extend(_render_docstring(plan, indent=8))
    lines.extend(_render_body(plan, async_=async_, aliases=aliases))
    return lines


def _render_signature(keyword: str, method_name: str, parameters: Sequence[str], annotation: str) -> list[str]:
    single = f"    {keyword} {method_name}({', '.join(parameters)}) -> {annotation}:"
    argument_count = sum(1 for parameter in parameters[1:] if parameter != "*")
    if len(single) <= _LINE_LENGTH and argument_count <= _MAX_ARGS:
        return [single]
    lines = [f"    {keyword} {method_name}("]
    lines.extend(f"        {parameter}," for parameter in parameters)
    lines.append(f"    ) -> {annotation}:")
    return lines


def _method_parameters(plan: EndpointPlan, aliases: _Aliases) -> list[str]:
    parameters = ["self"]
    parameters.extend(f"{param.name}: {param.annotation}" for param in plan.path_params)
    keyword_only: list[str] = []
    for param in (*plan.query_params, *plan.form_params):
        if param.required:
            keyword_only.append(f"{param.name}: {param.annotation}")
        else:
            keyword_only.append(f"{param.name}: {param.annotation} | None = None")
    body = plan.body
    if body is not None and body.passthrough:
        annotation = aliases.model(body.model.name) if body.model is not None else "object"
        keyword_only.append(f"{body.raw_name or 'body'}: {annotation} | None = None")
    elif body is not None and body.model is not None:
        for flat_field in body.flat:
            annotation = _annotation(flat_field.field.type)
            if body.enforced and flat_field.field.required:
                keyword_only.append(f"{flat_field.parameter}: {annotation}")
            else:
                keyword_only.append(f"{flat_field.parameter}: {annotation} | None = None")
    if body is not None and body.model is None:
        annotation = body.raw_annotation or "object"
        if body.required:
            keyword_only.append(f"{body.raw_name}: {annotation}")
        else:
            keyword_only.append(f"{body.raw_name}: {annotation} | None = None")
    if plan.paginated:
        keyword_only.append("page: int | None = None")
        keyword_only.append("limit: int | None = None")
    if keyword_only:
        parameters.append("*")
        parameters.extend(keyword_only)
    return parameters


def _render_docstring(plan: EndpointPlan, *, indent: int) -> list[str]:
    operation = plan.operation
    body_lines: list[str] = []
    summary = _strip_html(operation.summary or _first_line(operation.description) or plan.method_name.replace("_", " "))
    body_lines.append(summary.strip().rstrip(".") + ".")
    description = _strip_html(operation.description or "").strip()
    if description and description.rstrip(".") != summary.strip().rstrip("."):
        body_lines.append("")
        body_lines.extend(description.split("\n"))
    args = _doc_args(plan)
    if args:
        body_lines.append("")
        body_lines.append("Args:")
        body_lines.extend(f"    {line}" for line in args)
    returns = _doc_returns(plan)
    if returns:
        body_lines.append("")
        body_lines.append("Returns:")
        body_lines.extend(f"    {line}" for line in returns)
    raises = _doc_raises(operation)
    if raises:
        body_lines.append("")
        body_lines.append("Raises:")
        body_lines.extend(f"    {line}" for line in raises)
    if plan.name.deprecated:
        body_lines.append("")
        body_lines.append("Deprecated:")
        body_lines.append("    Deprecated in the vendored Spec; generated for compatibility.")
    body_lines.append("")
    body_lines.append(f"Operation ID: {operation.operation_id}")
    return _wrap_docstring(body_lines, indent=indent)


def _doc_args(plan: EndpointPlan) -> list[str]:
    entries: list[str] = []
    for param in plan.call_params:
        description = _strip_html(param.description or "").strip()
        entries.append(_tuple_entry(param.name, description))
    body = plan.body
    if body is not None and body.passthrough:
        entries.append(
            _tuple_entry(
                body.raw_name or "body",
                "Full request body; the Spec declares no fields, so extra fields are allowed.",
            )
        )
    elif body is not None and body.model is not None:
        for flat_field in body.flat:
            description = _strip_html(flat_field.field.description or "").strip()
            if flat_field.parameter != flat_field.field.name:
                wire = f"Wire field ``{flat_field.field.name}``."
                description = f"{description} {wire}".strip()
            entries.append(_tuple_entry(flat_field.parameter, description))
    if plan.paginated:
        entries.append(_tuple_entry("page", "1-based page to start iteration at."))
        entries.append(_tuple_entry("limit", "Page size; the instance caps it server-side."))
    return entries


def _tuple_entry(name: str, description: str) -> str:
    if description:
        return f"{name}: {description}"
    return f"{name}:"


def _doc_returns(plan: EndpointPlan) -> list[str]:
    """The Spec's description of the response; the return type lives in the method annotation.

    ``None`` responses get a generic sentence instead of the Spec's schema boilerplate
    ("APIEmpty is an empty response").
    """
    if plan.response.annotation == "None":
        return ["No content."]
    description = _strip_html(plan.response.description or "").strip().rstrip(".")
    if not description:
        return []
    return [f"{description}."]


def _doc_raises(operation: Operation) -> list[str]:
    entries: list[str] = []
    seen: set[str] = set()
    for response in operation.responses:
        if response.status is not None and _HTTP_OK_MIN <= response.status < _HTTP_OK_MAX:
            continue
        name = _error_name(response.status)
        if name in seen:
            continue
        seen.add(name)
        description = _strip_html(response.description or "").strip().rstrip(".")
        status = "default" if response.status is None else str(response.status)
        entries.append(f"{name}: {status}. {description}." if description else f"{name}: {status}.")
    return entries


def _error_name(status: int | None) -> str:
    if status is None:
        return "APIError"
    if _HTTP_SERVER_ERROR_MIN <= status < _HTTP_SERVER_ERROR_MAX:
        return "ServerError"
    return _ERROR_CLASSES.get(status, "APIError")


def _render_body(plan: EndpointPlan, *, async_: bool, aliases: _Aliases) -> list[str]:
    operation = plan.operation
    lines: list[str] = []
    path = _path_expression(plan)
    queryable = bool(plan.query_params)
    if queryable:
        entries = ", ".join(f'"{param.wire_name}": {_query_value(param)}' for param in plan.query_params)
        lines.append(f"        _query: dict[str, object] = {{{entries}}}")
        lines.append("")
    await_prefix = "await " if async_ else ""
    if plan.paginated:
        element = plan.response.element
        if element is None:
            raise ValueError(_MISSING_ELEMENT)
        paginate_arguments = [f'"{operation.method}"', path, f"model={aliases.model(element.name)}"]
        if queryable:
            paginate_arguments.append("params=_query")
        paginate_arguments.extend(["page=page", "limit=limit"])
        lines.append(f"        return {await_prefix}self._client._paginate({', '.join(paginate_arguments)})")
        return lines
    call_arguments = [f'"{operation.method}"', path]
    if queryable:
        call_arguments.append("params=_query")
    body = plan.body
    if body is not None and body.model is not None:
        lines.extend(_render_model_body(plan, aliases))
        call_arguments.append("json=_payload")
    elif body is not None:
        lines.append(f"        _payload = {body.raw_name}")
        call_arguments.append("json=_payload")
    if plan.form_params:
        form_lines, form_arguments = _render_form_body(plan)
        lines.extend(form_lines)
        call_arguments.extend(form_arguments)
    lines.append(f"        _response = {await_prefix}self._client._request({', '.join(call_arguments)})")
    lines.append(f"        return decode(_response, {plan.response.decode})")
    return lines


def _query_value(param: ParamPlan) -> str:
    """Render one query value; ``None`` entries are dropped by the runtime hook."""
    if param.is_datetime:
        return f"None if {param.name} is None else {param.name}.isoformat()"
    return param.name


def _render_model_body(plan: EndpointPlan, aliases: _Aliases) -> list[str]:
    body = plan.body
    if body is None or body.model is None:
        raise ValueError(_NO_MODEL_BODY)
    if body.passthrough:
        name = body.raw_name or "body"
        return [
            (
                f"        _payload = None if {name} is None "
                f"else {name}.model_dump(mode='json', by_alias=True, exclude_none=True)"
            ),
            "",
        ]
    model = aliases.model(body.model.name)
    flat = body.flat
    arguments = [f"{flat_field.field.name}={flat_field.parameter}" for flat_field in flat]
    lines: list[str] = []
    if body.enforced:
        if arguments:
            lines.append(f"        _payload = {model}(")
            lines.extend(f"            {argument}," for argument in arguments)
            lines.append("        ).model_dump(mode='json', by_alias=True, exclude_none=True)")
        else:
            lines.append(f"        _payload = {model}().model_dump(mode='json', by_alias=True, exclude_none=True)")
    elif flat:
        checks = " or ".join(f"{flat_field.parameter} is not None" for flat_field in flat)
        dump = f"{model}({', '.join(arguments)}).model_dump(mode='json', by_alias=True, exclude_none=True)"
        lines.append(f"        if {checks}:")
        lines.append(f"            _payload = {dump}")
        lines.append("        else:")
        lines.append("            _payload = None")
    else:
        lines.append("        _payload = None")
    lines.append("")
    return lines


def _render_form_body(plan: EndpointPlan) -> tuple[list[str], list[str]]:
    lines: list[str] = []
    arguments: list[str] = []
    files = [param for param in plan.form_params if param.is_file]
    fields = [param for param in plan.form_params if not param.is_file]
    if files:
        lines.append("        _files: dict[str, object] = {}")
        for param in files:
            if param.required:
                lines.append(f'        _files["{param.wire_name}"] = {param.name}')
            else:
                lines.append(f"        if {param.name} is not None:")
                lines.append(f'            _files["{param.wire_name}"] = {param.name}')
        arguments.append("files=_files")
    if fields:
        lines.append("        _form: dict[str, object] = {}")
        for param in fields:
            if param.required:
                lines.append(f'        _form["{param.wire_name}"] = {param.name}')
            else:
                lines.append(f"        if {param.name} is not None:")
                lines.append(f'            _form["{param.wire_name}"] = {param.name}')
        arguments.append("data=_form")
    lines.append("")
    return lines, arguments


def _path_expression(plan: EndpointPlan) -> str:
    operation = plan.operation
    by_wire = {parameter.wire_name: parameter.python_name for parameter in operation.parameters}
    segments: list[str] = []
    dynamic = False
    for segment in operation.segments:
        text = segment.template
        for wire_name in segment.parameters:
            dynamic = True
            text = text.replace("{" + wire_name + "}", "{" + by_wire[wire_name] + "}")
        segments.append(text)
    if not dynamic:
        return '"/' + "/".join(segments) + '"'
    return 'f"/' + "/".join(segments) + '"'


# ---------------------------------------------------------------------------
# The assembled clients
# ---------------------------------------------------------------------------


def _render_api_init(modules: Sequence[str]) -> str:
    lines: list[str] = [
        '"""Generated Forgejo clients with typed namespace attributes. Do not edit by hand.',
        "",
        "Regenerate with ``python -m codegen``; see docs/development/codegen.md.",
        '"""',
        "",
        "from __future__ import annotations",
        "",
        "from functools import cached_property",
        "",
    ]
    for module in modules:
        class_name = pascal_case(module)
        names = ", ".join(sorted((class_name, f"Async{class_name}")))
        lines.append(f"from pyfj._generated.api.{module} import {names}")
    lines.append("from pyfj._runtime import AsyncForgejo as _RuntimeAsyncForgejo")
    lines.append("from pyfj._runtime import Forgejo as _RuntimeForgejo")
    lines.append("")
    lines.append('__all__ = ["AsyncForgejo", "Forgejo"]')
    lines.append("")
    lines.append("")
    lines.extend(_render_client("Forgejo", "_RuntimeForgejo", "", modules))
    lines.append("")
    lines.append("")
    lines.extend(_render_client("AsyncForgejo", "_RuntimeAsyncForgejo", "Async", modules))
    return "\n".join(lines).rstrip("\n") + "\n"


def _render_client(client_name: str, base: str, prefix: str, modules: Sequence[str]) -> list[str]:
    doc = "asynchronous" if prefix else "synchronous"
    lines = [f"class {client_name}({base}):", f'    """The {doc} pyfj client."""', ""]
    for index, module in enumerate(modules):
        class_name = f"{prefix}{pascal_case(module)}"
        lines.append("    @cached_property")
        lines.append(f"    def {module}(self) -> {class_name}:")
        lines.append(f'        """The ``{module}`` namespace."""')
        lines.append(f"        return {class_name}(self)")
        if index != len(modules) - 1:
            lines.append("")
    return lines


# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------


def render_report(naming: Naming, plans: Sequence[EndpointPlan], *, mapping: Overrides, registry: Registry) -> str:
    """Render ``codegen/naming-report.md`` for review."""
    counts: dict[str, int] = {}
    for plan in plans:
        counts[plan.module] = counts.get(plan.module, 0) + 1
    lines: list[str] = [
        "# pyfj naming report",
        "",
        "Generated by `python -m codegen` from `spec/openapi.json`; do not edit by hand.",
        "Overrides live in `codegen/mapping.toml`, exclusions in `codegen/registry.toml`.",
        "",
        f"- Operations in the Spec: **{len(naming.endpoints) + len(naming.exclusions)}**",
        f"- Generated: **{len(naming.endpoints)}**",
        f"- Excluded: **{len(naming.exclusions)}**",
        "",
        "Top-level namespaces (operations): "
        + ", ".join(f"`{name}` ({count})" for name, count in sorted(counts.items()))
        + ".",
        "",
    ]
    lines.extend(_render_overrides(mapping))
    lines.extend(_render_exclusions(naming))
    lines.extend(
        [
            "## Operations",
            "",
            "`Call` is the synchronous call site; the async client exposes the same",
            "shape with `await`. `Body` records the body mode: `json` bodies expose",
            "flat keyword fields; a field whose name collides with another parameter is",
            "prefixed `body_` (its wire field is shown in parentheses), `raw` bodies are",
            "a single keyword, and `multipart` bodies expose file and form fields.",
            "",
            "| # | operationId | HTTP | Path | Call | Body | Returns | Deprecated |",
            "|---|-------------|------|------|------|------|---------|------------|",
        ]
    )
    for index, plan in enumerate(plans, start=1):
        lines.append(_report_row(index, plan))
    lines.append("")
    return "\n".join(lines)


def _render_overrides(mapping: Overrides) -> list[str]:
    lines = ["## Overrides", ""]
    if mapping.namespaces:
        lines.append("Namespace overrides:")
        lines.append("")
        lines.append("| Path prefix | Rename | Skip |")
        lines.append("|-------------|--------|------|")
        for prefix, override in sorted(mapping.namespaces.items()):
            lines.append(f"| `{prefix}` | {override.name or '—'} | {'yes' if override.skip else 'no'} |")
        lines.append("")
    if mapping.methods:
        lines.append("Method overrides:")
        lines.append("")
        lines.append("| operationId | Name | Deprecated |")
        lines.append("|-------------|------|------------|")
        for operation_id, override in sorted(mapping.methods.items()):
            name = override.name or "—"
            deprecated = "—" if override.deprecated is None else ("yes" if override.deprecated else "no")
            lines.append(f"| `{operation_id}` | `{name}` | {deprecated} |")
        lines.append("")
    if mapping.models:
        lines.append("Model overrides:")
        lines.append("")
        lines.append("| Definition | Class name |")
        lines.append("|------------|------------|")
        for definition, class_name in sorted(mapping.models.items()):
            lines.append(f"| `{definition}` | `{class_name}` |")
        lines.append("")
    if not mapping.namespaces and not mapping.methods and not mapping.models:
        lines.append("None.")
        lines.append("")
    return lines


def _render_exclusions(naming: Naming) -> list[str]:
    lines = ["## Exclusions", ""]
    if not naming.exclusions:
        lines.append("None: every operation in the Spec is generated.")
        lines.append("")
        return lines
    lines.append("| operationId | Reason |")
    lines.append("|-------------|--------|")
    for operation, reason in naming.exclusions:
        lines.append(f"| `{operation.operation_id}` | {reason} |")
    lines.append("")
    return lines


def _report_row(index: int, plan: EndpointPlan) -> str:
    operation = plan.operation
    call = _report_call(plan)
    body = _report_body(plan)
    deprecated = "yes" if plan.name.deprecated else "no"
    return (
        f"| {index} | `{operation.operation_id}` | {operation.method} | `{operation.path}` | "
        f"`{call}` | {body} | `{_display_annotation(plan.response.annotation)}` | {deprecated} |"
    )


def _report_call(plan: EndpointPlan) -> str:
    arguments: list[str] = [param.name for param in plan.path_params]
    keyword: list[str] = [
        param.name if param.required else f"{param.name}=None" for param in (*plan.query_params, *plan.form_params)
    ]
    body = plan.body
    if body is not None and body.passthrough:
        keyword.append(f"{body.raw_name or 'body'}=None")
    elif body is not None and body.model is not None:
        for flat_field in body.flat:
            if body.enforced and flat_field.field.required:
                keyword.append(flat_field.parameter)
            else:
                keyword.append(f"{flat_field.parameter}=None")
    elif body is not None:
        keyword.append(f"{body.raw_name}=...")
    if plan.paginated:
        keyword.extend(["page=None", "limit=None"])
    if keyword:
        arguments.append("*")
        arguments.extend(keyword)
    return f"client.{'.'.join(plan.name.namespace)}.{plan.method_name}({', '.join(arguments)})"


def _report_body(plan: EndpointPlan) -> str:
    body = plan.body
    if body is None:
        if plan.form_params:
            files = ", ".join(param.name for param in plan.form_params if param.is_file)
            fields = ", ".join(param.name for param in plan.form_params if not param.is_file)
            parts: list[str] = []
            if files:
                parts.append(f"files: {files}")
            if fields:
                parts.append(f"form: {fields}")
            return "multipart (" + "; ".join(parts) + ")"
        return "—"
    if body.model is None:
        return f"raw `{body.raw_annotation}`"
    if body.passthrough:
        return f"json `{body.model.name}` whole: {body.raw_name or 'body'}"
    flat = ", ".join(
        flat_field.parameter
        if flat_field.parameter == flat_field.field.name
        else f"{flat_field.parameter} (wire {flat_field.field.name})"
        for flat_field in body.flat
    )
    return f"json `{body.model.name}` flat: {flat or '-'}"


def _wrap_docstring(body_lines: Sequence[str], *, indent: int) -> list[str]:
    pad = " " * indent
    lines: list[str] = [f'{pad}"""']
    section = ""
    for body_line in body_lines:
        if not body_line:
            lines.append("")
            continue
        leading = len(body_line) - len(body_line.lstrip(" "))
        if not leading and body_line.endswith(":"):
            section = body_line
        continuation = " " * _DOCSTRING_CONTINUATION_INDENT if section in _DOCSTRING_ENTRY_SECTIONS else ""
        width = max(_LINE_LENGTH - indent - leading, 40)
        wrapped = textwrap.wrap(
            body_line.strip(),
            width=width,
            break_long_words=True,
            break_on_hyphens=False,
            subsequent_indent=continuation,
        ) or [""]
        lines.extend(f"{pad}{' ' * leading}{piece}" for piece in wrapped)
    lines.append(f'{pad}"""')
    return lines


_UNICODE_REPLACEMENTS: Final[dict[int, str]] = {
    0x2018: "'",  # left single quotation mark
    0x2019: "'",  # right single quotation mark
    0x201C: '"',  # left double quotation mark
    0x201D: '"',  # right double quotation mark
    0x2013: "-",  # en dash
    0x2014: "-",  # em dash
    0x2026: "...",  # horizontal ellipsis
    0x00A0: " ",  # no-break space
    0x200B: "",  # zero-width space
}


def _strip_html(text: str) -> str:
    if not text:
        return ""
    value = _BREAK.sub("\n", text)
    value = _TAG.sub("", value)
    value = html.unescape(value).translate(_UNICODE_REPLACEMENTS)
    # Keep the newlines inserted above (and any authored ones); drop other
    # control/format characters so docstrings stay plain text.
    value = "".join(
        character for character in value if character == "\n" or not unicodedata.category(character).startswith("C")
    )
    output: list[str] = []
    for line in value.splitlines():
        collapsed = " ".join(line.split())
        if collapsed:
            output.append(collapsed)
    return "\n".join(output)


def _first_line(text: str | None) -> str:
    if not text:
        return ""
    return _strip_html(text).split("\n", 1)[0]
