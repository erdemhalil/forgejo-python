"""Model emission: one module per generated type, deterministic bytes.

``emit_models`` writes ``src/pyfj/_generated/models/**`` from the IR. The
rendered source is already close to the committed form; the runner finishes
with ``ruff format`` so the tree is formatted with the repository's config.
Two runs over the same Spec produce byte-identical output because every
collection iterated here has an explicit order.

Generated models are pydantic v2 (``extra="allow"``, ``populate_by_name``),
use snake_case fields with wire-name aliases, ``StrEnum``/``IntEnum`` for
enums, and ``datetime``/``date`` for the ``date-time``/``date`` formats.
Spec descriptions become class docstrings and pydantic ``Field`` descriptions.
Models never import from ``pyfj._generated.api``.
"""

from __future__ import annotations

import json
import re
import textwrap
from dataclasses import dataclass
from dataclasses import field as dataclass_field
from pathlib import Path
from typing import TYPE_CHECKING, Final

from codegen.ir import (
    Field as ModelField,
)
from codegen.ir import (
    ListType,
    MapType,
    NamedRef,
    ScalarType,
    TypeDef,
    TypeExpr,
    iter_types,
)

if TYPE_CHECKING:
    from codegen.ir import IR

__all__ = ["emit_models", "render_init", "render_module"]

_LINE_LENGTH: Final = 120
_DOCSTRING_PAD: Final = 4

_SCALAR_NAMES: Final[dict[str, str]] = {
    "string": "str",
    "integer": "int",
    "number": "float",
    "boolean": "bool",
    "datetime": "datetime",
    "date": "date",
    "bytes": "bytes",
    "file": "bytes",
    "any": "Any",
}


@dataclass(slots=True)
class _Imports:
    datetime: bool = False
    date: bool = False
    any_: bool = False
    str_enum: bool = False
    int_enum: bool = False
    field: bool = False
    models: dict[str, set[str]] = dataclass_field(default_factory=dict)


def emit_models(ir: IR, out_dir: str | Path) -> list[Path]:
    """Write every model module plus the generated ``__init__`` re-exports.

    Stale ``*.py`` files that are not part of this generation are removed so
    the directory exactly mirrors the Spec. Returns the written paths.
    """
    directory = Path(out_dir)
    directory.mkdir(parents=True, exist_ok=True)
    files: dict[str, str] = {f"{type_def.module}.py": render_module(type_def) for type_def in ir.types}
    files["__init__.py"] = render_init(ir)
    written: list[Path] = []
    for name in sorted(files):
        path = directory / name
        path.write_text(files[name], encoding="utf-8", newline="\n")
        written.append(path)
    for stale in sorted(directory.glob("*.py")):
        if stale.name not in files:
            stale.unlink()
    return written


def render_module(type_def: TypeDef) -> str:
    """Render the module that owns ``type_def`` (its nested types included)."""
    imports = _Imports()
    nodes = list(iter_types(type_def))
    for node in nodes:
        _collect_imports(node, imports)
    has_model = any(node.kind == "model" for node in nodes)
    blocks: list[str] = [
        f'"""{_module_header(type_def)}"""',
        "",
        "from __future__ import annotations",
        "",
    ]
    import_lines: list[str] = []
    stdlib = _stdlib_import_lines(imports)
    if stdlib:
        import_lines.extend(stdlib)
        import_lines.append("")
    if has_model:
        names = ["BaseModel", "ConfigDict", *(["Field"] if imports.field else [])]
        import_lines.append(f"from pydantic import {', '.join(names)}")
    if imports.models:
        if has_model:
            import_lines.append("")
        for module in sorted(imports.models):
            names = ", ".join(sorted(imports.models[module]))
            import_lines.append(f"from pyfj._generated.models.{module} import {names}")
    if import_lines:
        blocks.extend(import_lines)
        blocks.append("")
    for node in nodes:
        blocks.extend(_render_type_def(node))
        blocks.append("")
    return "\n".join(blocks).rstrip("\n") + "\n"


def render_init(ir: IR) -> str:
    """Render the package ``__init__`` re-exporting every generated type."""
    exports: list[str] = []
    lines: list[str] = [
        '"""Generated re-exports of every model in ``pyfj._generated.models``. Do not edit by hand."""',
        "",
        "from __future__ import annotations",
        "",
    ]
    for type_def in ir.types:
        names = sorted(node.name for node in iter_types(type_def))
        exports.extend(names)
        lines.append(f"from pyfj._generated.models.{type_def.module} import {', '.join(names)}")
    lines.append("")
    lines.append("__all__ = [")
    lines.extend(f'    "{name}",' for name in sorted(exports, key=_all_sort_key))
    lines.append("]")
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# Rendering helpers
# ---------------------------------------------------------------------------


def _module_header(type_def: TypeDef) -> str:
    return f"Generated from spec/openapi.json ({type_def.name}). Do not edit by hand."


def _all_sort_key(name: str) -> tuple[bool, str]:
    """Match ruff's isort-style ``__all__`` ordering: constants, classes, functions."""
    return (not name.isupper(), name)


def _render_type_def(type_def: TypeDef) -> list[str]:
    if type_def.kind == "model":
        return _render_model(type_def)
    if type_def.kind == "enum":
        return _render_enum(type_def)
    return _render_alias(type_def)


def _render_model(type_def: TypeDef) -> list[str]:
    lines = [f"class {type_def.name}(BaseModel):"]
    description = _describe(type_def.description) if type_def.description else None
    docstring = _render_docstring(description, _DOCSTRING_PAD)
    if docstring:
        lines.extend(docstring)
        lines.append("")
    lines.append('    model_config = ConfigDict(extra="allow", populate_by_name=True)')
    if type_def.fields:
        lines.append("")
        for field in type_def.fields:
            lines.extend(_render_field(field))
    return lines


def _render_enum(type_def: TypeDef) -> list[str]:
    base = "StrEnum" if type_def.enum_base == "str" else "IntEnum"
    lines = [f"class {type_def.name}({base}):"]
    description = _describe(type_def.description) if type_def.description else None
    docstring = _render_docstring(description, _DOCSTRING_PAD)
    if docstring:
        lines.extend(docstring)
        lines.append("")
    for value in type_def.enum_values:
        literal = _py_string(value.value) if isinstance(value.value, str) else str(value.value)
        lines.append(f"    {value.name} = {literal}")
    return lines


def _render_alias(type_def: TypeDef) -> list[str]:
    lines: list[str] = []
    if type_def.description:
        lines.extend(_render_comment(_describe(type_def.description), indent=0))
    target = "Any" if type_def.alias_target is None else _render_type(type_def.alias_target)
    lines.append(f"{type_def.name} = {target}")
    return lines


def _render_field(field: ModelField) -> list[str]:
    annotation = _render_type(field.type)
    if not field.required:
        annotation = f"{annotation} | None"
    has_metadata = field.wire_name != field.name or bool(field.description)
    if not has_metadata:
        suffix = "" if field.required else " = None"
        return [f"    {field.name}: {annotation}{suffix}"]
    arguments: list[str] = []
    if not field.required:
        arguments.append("default=None")
    if field.wire_name != field.name:
        arguments.append(f"alias={_py_string(field.wire_name)}")
    if field.description:
        start = 8 + len("description=")
        arguments.append(f"description={_string_expr(_describe(field.description), indent=8, start=start)}")
    return [f"    {field.name}: {annotation} = Field({', '.join(arguments)})"]


def _render_type(expr: TypeExpr) -> str:
    if isinstance(expr, ScalarType):
        return _SCALAR_NAMES[expr.kind]
    if isinstance(expr, NamedRef):
        return expr.name
    if isinstance(expr, ListType):
        return f"list[{_render_type(expr.item)}]"
    if isinstance(expr, MapType):
        return f"dict[str, {_render_type(expr.value)}]"
    message = f"unsupported IR type expression: {expr!r}"
    raise TypeError(message)


_NEWLINE_RUN: Final[re.Pattern[str]] = re.compile(r"\s*[\r\n]+\s*")


def _describe(text: str) -> str:
    """Collapse Spec line breaks into spaces so descriptions read as single-line prose."""
    return _NEWLINE_RUN.sub(" ", text).strip()


def _render_docstring(text: str | None, indent: int) -> list[str]:
    if text is None or not text.strip():
        return []
    escaped = _escape_docstring(text.strip())
    pad = " " * indent
    source_lines = escaped.split("\n")
    if len(source_lines) == 1 and indent + len(escaped) + 6 <= _LINE_LENGTH:
        return [f'{pad}"""{escaped}"""']
    first = _wrap(source_lines[0], _LINE_LENGTH - indent - 10)
    lines = [f'{pad}"""{first[0]}']
    lines.extend(f"{pad}{line}" for line in first[1:])
    for source_line in source_lines[1:]:
        wrapped = _wrap(source_line, _LINE_LENGTH - indent)
        lines.extend(f"{pad}{line}" for line in wrapped)
    lines.append(f'{pad}"""')
    return lines


def _render_comment(text: str, indent: int) -> list[str]:
    pad = " " * indent
    lines: list[str] = []
    for source_line in text.strip().split("\n"):
        wrapped = _wrap(source_line, _LINE_LENGTH - indent - 2)
        lines.extend(f"{pad}# {line}" for line in wrapped)
    return lines


def _wrap(line: str, width: int) -> list[str]:
    if not line:
        return [""]
    return textwrap.wrap(
        line,
        width=max(width, 20),
        break_long_words=True,
        break_on_hyphens=False,
    ) or [""]


def _escape_docstring(text: str) -> str:
    return text.replace("\\", "\\\\").replace('"""', '\\"\\"\\"')


def _py_string(text: str) -> str:
    """Render ``text`` as a double-quoted Python string literal (JSON escaping)."""
    return json.dumps(text, ensure_ascii=False)


def _string_expr(text: str, *, indent: int, start: int | None = None) -> str:
    """Render a (possibly long) string as one implicit-concatenation expression."""
    literal = _py_string(text)
    effective_start = indent if start is None else start
    if effective_start + len(literal) <= _LINE_LENGTH:
        return literal
    chunks = textwrap.wrap(
        text,
        width=max(40, _LINE_LENGTH - indent - 12),
        replace_whitespace=False,
        drop_whitespace=False,
        expand_tabs=False,
        break_long_words=True,
        break_on_hyphens=False,
    )
    if not chunks:
        return literal
    inner_pad = " " * (indent + 4)
    closing_pad = " " * indent
    joined = f"\n{inner_pad}".join(_py_string(chunk) for chunk in chunks)
    return f"(\n{inner_pad}{joined}\n{closing_pad})"


# ---------------------------------------------------------------------------
# Import collection
# ---------------------------------------------------------------------------


def _collect_imports(type_def: TypeDef, imports: _Imports) -> None:
    if type_def.kind == "enum":
        if type_def.enum_base == "str":
            imports.str_enum = True
        else:
            imports.int_enum = True
    for field in type_def.fields:
        _collect_expr(field.type, imports, type_def.module)
        if field.wire_name != field.name or bool(field.description):
            imports.field = True
    if type_def.kind != "alias":
        return
    if type_def.alias_target is None:
        imports.any_ = True
    else:
        _collect_expr(type_def.alias_target, imports, type_def.module)


def _collect_expr(expr: TypeExpr, imports: _Imports, module: str) -> None:
    if isinstance(expr, ScalarType):
        if expr.kind == "datetime":
            imports.datetime = True
        elif expr.kind == "date":
            imports.date = True
        elif expr.kind == "any":
            imports.any_ = True
        return
    if isinstance(expr, NamedRef):
        if expr.module != module:
            imports.models.setdefault(expr.module, set()).add(expr.name)
        return
    if isinstance(expr, ListType):
        _collect_expr(expr.item, imports, module)
        return
    _collect_expr(expr.value, imports, module)


def _stdlib_import_lines(imports: _Imports) -> list[str]:
    lines: list[str] = []
    datetime_names: list[str] = []
    if imports.date:
        datetime_names.append("date")
    if imports.datetime:
        datetime_names.append("datetime")
    if datetime_names:
        joined = ", ".join(datetime_names)
        lines.append(f"from datetime import {joined}")
    enum_names: list[str] = []
    if imports.int_enum:
        enum_names.append("IntEnum")
    if imports.str_enum:
        enum_names.append("StrEnum")
    if enum_names:
        lines.append(f"from enum import {', '.join(enum_names)}")
    if imports.any_:
        lines.append("from typing import Any")
    return lines
