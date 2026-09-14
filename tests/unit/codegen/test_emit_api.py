"""Golden, quirk, and hygiene tests for the API emitter.

The synthetic ``api_spec.json`` exercises the rows of the quirk table in
``docs/development/codegen.md``: pagination, flat bodies (required and optional),
``body_``-prefixed collisions, multipart uploads, 202/204/205, text/plain,
bytes, alias responses, and JSON fallbacks. Golden files are the committed
emitter output (run through ``ruff format`` exactly like the real tree).
"""

from __future__ import annotations

import ast
import re
from pathlib import Path
from typing import TYPE_CHECKING

import pytest

from codegen.__main__ import generate
from codegen.emit_api import _doc_returns, _strip_html, _wrap_docstring, emit_api, plan_endpoints, render_report
from codegen.ir import build_ir
from codegen.naming import Overrides, Registry, assign_names
from codegen.spec import load_spec

if TYPE_CHECKING:
    from collections.abc import Callable

    from codegen.emit_api import EndpointPlan
    from codegen.ir import IR
    from codegen.naming import Naming

API_SPEC_PATH = Path(__file__).parent / "data" / "api_spec.json"
API_GOLDEN_DIR = Path(__file__).parent / "golden" / "api"


@pytest.fixture(scope="session")
def api_ir() -> IR:
    return build_ir(load_spec(API_SPEC_PATH))


@pytest.fixture(scope="session")
def api_naming(api_ir: IR) -> Naming:
    return assign_names(api_ir, Overrides(), Registry())


@pytest.fixture(scope="session")
def api_plans(api_naming: Naming, api_ir: IR) -> tuple[EndpointPlan, ...]:
    return plan_endpoints(api_naming, api_ir)


def _plan(plans: tuple[EndpointPlan, ...], operation_id: str) -> EndpointPlan:
    return next(plan for plan in plans if plan.operation.operation_id == operation_id)


def _rendered(api_ir: IR, api_naming: Naming, operation_id: str, tmp_path: Path) -> str:
    emit_api(api_ir, tmp_path / "api", mapping=Overrides(), registry=Registry(), report_path=tmp_path / "report.md")
    plan = _plan(plan_endpoints(api_naming, api_ir), operation_id)
    return (tmp_path / "api" / f"{plan.module}.py").read_text(encoding="utf-8")


_METHOD_START = re.compile(r"^    (?:async )?def \w+\(", re.MULTILINE)


def _method_source(text: str, operation_id: str) -> str:
    """The source of the first method whose docstring carries ``operation_id``."""
    marker = f"Operation ID: {operation_id}"
    marker_position = text.index(marker)
    starts = [match.start() for match in _METHOD_START.finditer(text)]
    start = max(position for position in starts if position < marker_position)
    later = [position for position in starts if position > marker_position]
    return text[start : min(later) if later else len(text)]


# ---------------------------------------------------------------------------
# Quirk coverage
# ---------------------------------------------------------------------------


def test_strip_html_keeps_newlines_and_drops_format_characters() -> None:
    assert _strip_html("reclaimed<br>asynchronously") == "reclaimed\nasynchronously"
    assert _strip_html("normalized to LF to\nmatch the behaviour") == "normalized to LF to\nmatch the behaviour"
    assert _strip_html("zero\u200bwidth") == "zerowidth"


def test_wrapped_args_continuation_is_indented_below_the_entry() -> None:
    """Google-style parsers read a continuation at entry indent as a new, broken entry (regression)."""
    description = " ".join(f"word{index}" for index in range(40))
    lines = _wrap_docstring(["Args:", f"    sort: {description}", "", "Returns:", "    None."], indent=4)
    body = [line[4:] for line in lines[1:-1]]
    args_at = body.index("Args:")
    returns_at = body.index("Returns:")
    entries = [line for line in body[args_at + 1 : returns_at] if line]
    assert entries[0].startswith("    sort: word0 ")
    continuations = [line for line in entries if not line.startswith("    sort: ")]
    assert continuations
    assert all(line.startswith("        word") for line in continuations)
    assert " ".join(line.strip() for line in entries) == f"sort: {description}"


def test_paginated_list(api_plans: tuple[EndpointPlan, ...]) -> None:
    plan = _plan(api_plans, "widgetList")
    assert plan.paginated
    assert plan.response.annotation == "Paginated[Thing]"
    assert plan.response.element is not None
    assert {param.name for param in plan.query_params} == {"state"}
    assert plan.page_limit


def test_doc_returns_describes_the_response_without_the_type(api_plans: tuple[EndpointPlan, ...]) -> None:
    assert _doc_returns(_plan(api_plans, "widgetList")) == ["A page of things."]
    assert _doc_returns(_plan(api_plans, "widgetDelete")) == ["No content."]
    assert _doc_returns(_plan(api_plans, "widgetDownload")) == ["Rendered bytes."]


def test_return_types_stay_out_of_the_docstring(api_ir: IR, api_naming: Naming, tmp_path: Path) -> None:
    text = _rendered(api_ir, api_naming, "widgetList", tmp_path)
    sync_class, async_class = text.split("class AsyncMiscWidgets", 1)
    assert "A page of things." in sync_class
    assert "-> Paginated[Thing]:" in sync_class
    assert "-> AsyncPaginated[Thing]:" in async_class
    assert "Paginated[Thing]. A page of things." not in text
    assert "AsyncPaginated[Thing]. A page of things." not in text


def test_non_list_page_limit_stays_a_query_parameter(api_plans: tuple[EndpointPlan, ...]) -> None:
    plan = _plan(api_plans, "adminSearch")
    assert not plan.paginated
    assert {param.name for param in plan.query_params} >= {"q", "page", "limit"}
    assert plan.response.annotation == "SearchResults"


def test_required_body_exposes_required_fields(api_ir: IR, api_naming: Naming, tmp_path: Path) -> None:
    text = _method_source(_rendered(api_ir, api_naming, "widgetCreate", tmp_path), "widgetCreate")
    assert "params: CreateThingOptions | None = None" not in text
    assert "_MIXED_BODY_MESSAGE" not in text
    assert "name: str | None" not in text
    assert "name: str," in text
    assert "description: str | None = None" in text
    assert "owner: str | None = None" in text
    # A required body is always sent, with its required field passed straight through.
    assert "_payload = CreateThingOptions(" in text
    assert "name=name," in text
    assert "description=description," in text
    assert "owner=owner," in text
    assert ").model_dump(mode='json', by_alias=True, exclude_none=True)" in text
    assert "exclude_none=True" in text
    assert "cast(" not in text


def test_optional_body_keeps_the_provided_guard(api_ir: IR, api_naming: Naming, tmp_path: Path) -> None:
    text = _method_source(_rendered(api_ir, api_naming, "widgetEdit", tmp_path), "widgetEdit")
    assert "params: EditThingOptions | None = None" not in text
    assert "if name is not None or description is not None:" in text
    assert "_payload = None" in text
    assert "cast(" not in text


def test_optional_body_with_required_field_is_enforced(api_ir: IR, api_naming: Naming, tmp_path: Path) -> None:
    text = _method_source(_rendered(api_ir, api_naming, "thingEditInOrg", tmp_path), "thingEditInOrg")
    assert "name: str," in text
    assert "name: str | None" not in text
    assert "body_owner: str | None = None" in text
    # A model with required fields is always constructed: no guard, no casts.
    assert "if name is not None" not in text
    assert "_payload = CreateThingOptions(" in text
    assert "cast(" not in text
    assert "Wire field ``owner``." in text


def test_colliding_body_field_is_prefixed(api_plans: tuple[EndpointPlan, ...]) -> None:
    plan = _plan(api_plans, "thingCreateInOrg")
    assert plan.body is not None
    assert [(flat_field.parameter, flat_field.field.name) for flat_field in plan.body.flat] == [
        ("name", "name"),
        ("description", "description"),
        ("body_owner", "owner"),
    ]


def test_required_colliding_body_field_is_a_required_keyword(api_ir: IR, api_naming: Naming, tmp_path: Path) -> None:
    text = _method_source(_rendered(api_ir, api_naming, "userCreateOrg", tmp_path), "userCreateOrg")
    assert "body_username: str," in text
    assert "username: str | None" not in text
    assert "# ty: ignore" not in text
    assert "cast(" not in text
    assert "Wire field ``username``." in text


def test_fieldless_model_body_is_passed_whole(api_ir: IR, api_naming: Naming, tmp_path: Path) -> None:
    text = _method_source(_rendered(api_ir, api_naming, "widgetFreeForm", tmp_path), "widgetFreeForm")
    assert "body: FreeFormThing | None = None" in text
    assert "None if body is None else body.model_dump" in text


def test_multipart_upload(api_ir: IR, api_naming: Naming, tmp_path: Path) -> None:
    text = _rendered(api_ir, api_naming, "widgetUploadAttachment", tmp_path)
    assert "attachment: FilePart" in text
    assert "external_url: str | None = None" in text
    assert "updated_at.isoformat()" in text
    assert '_files["attachment"] = attachment' in text
    assert '_form["external_url"] = external_url' in text
    assert "files=_files" in text
    assert "data=_form" in text
    assert "from collections.abc import Mapping" in text
    assert "FilePart = FileContent" in text


def test_odd_success_statuses(api_plans: tuple[EndpointPlan, ...]) -> None:
    assert _plan(api_plans, "widgetDelete").response.annotation == "None"
    assert _plan(api_plans, "widgetStatus").response.annotation == "None"
    assert _plan(api_plans, "widgetIsMember").response.annotation == "None"
    assert _plan(api_plans, "widgetRefresh").response.annotation == "Thing | None"
    assert _plan(api_plans, "widgetFork").response.annotation == "Thing"


def test_redirect_responses_documented_as_api_error(api_ir: IR, api_naming: Naming, tmp_path: Path) -> None:
    text = _rendered(api_ir, api_naming, "widgetIsMember", tmp_path)
    assert "APIError: 303." in text
    assert "NotFoundError: 404." in text


def test_text_and_binary_produces(api_plans: tuple[EndpointPlan, ...]) -> None:
    assert _plan(api_plans, "widgetReport").response.annotation == "str"
    assert _plan(api_plans, "widgetLog").response.annotation == "str"
    assert _plan(api_plans, "widgetArchive").response.annotation == "bytes"


def test_alias_list_response(api_plans: tuple[EndpointPlan, ...]) -> None:
    plan = _plan(api_plans, "widgetInfo")
    assert plan.response.annotation == "builtins.list[Thing]"
    assert plan.response.decode == "list[Thing]"


def test_primitive_json_responses(api_ir: IR, api_naming: Naming, tmp_path: Path) -> None:
    plans = plan_endpoints(api_naming, api_ir)
    summary = _plan(plans, "adminReportSummary")
    assert (summary.response.annotation, summary.response.decode) == ("bool", "bool")
    flags = _plan(plans, "adminReportFlags")
    assert (flags.response.annotation, flags.response.decode) == ("builtins.list[str]", "list[str]")
    languages = _plan(plans, "adminReportLanguages")
    assert (languages.response.annotation, languages.response.decode) == ("dict[str, int]", "dict[str, int]")
    text = _rendered(api_ir, api_naming, "adminReportLanguages", tmp_path)
    assert "return decode(_response, dict[str, int])" in text
    assert 'cast("dict[str, int]"' not in text
    assert 'DecodeError(_response, "expected a JSON object")' not in text


def test_deprecated_operations_are_flagged(api_ir: IR, api_naming: Naming, tmp_path: Path) -> None:
    plan = _plan(plan_endpoints(api_naming, api_ir), "userOld")
    assert plan.name.deprecated
    text = _rendered(api_ir, api_naming, "userOld", tmp_path)
    assert "Deprecated:" in text
    assert "Operation ID: userOld" in text


def test_action_leaf_and_misc_routing(api_plans: tuple[EndpointPlan, ...]) -> None:
    assert _plan(api_plans, "widgetFork").name.namespace == ("misc", "widgets")
    assert _plan(api_plans, "widgetFork").method_name == "fork"
    assert _plan(api_plans, "getVersion").name.namespace == ("misc",)
    assert _plan(api_plans, "getVersion").method_name == "version"


def test_multi_parameter_path_segment(api_ir: IR, api_naming: Naming, tmp_path: Path) -> None:
    plan = _plan(plan_endpoints(api_naming, api_ir), "widgetDownload")
    assert [param.name for param in plan.path_params] == ["id", "format"]
    text = _rendered(api_ir, api_naming, "widgetDownload", tmp_path)
    assert 'f"/widgets/{id}.{format}"' in text
    assert 'format: Literal["raw", "diff"]' in text


# ---------------------------------------------------------------------------
# Golden files, determinism, hygiene
# ---------------------------------------------------------------------------


def _generate_api(tmp_path: Path, repo_root: Path, name: str) -> Path:
    api_dir = tmp_path / name
    generate(
        root=repo_root,
        spec_path=API_SPEC_PATH,
        models_dir=tmp_path / f"{name}_models",
        api_dir=api_dir,
        mapping_path=tmp_path / f"{name}_mapping.toml",
        registry_path=tmp_path / f"{name}_registry.toml",
        report_path=tmp_path / f"{name}_report.md",
    )
    return api_dir


def test_golden_files(tmp_path: Path, repo_root: Path, read_modules: Callable[[Path], dict[str, bytes]]) -> None:
    api_dir = _generate_api(tmp_path, repo_root, "api")
    generated = read_modules(api_dir)
    golden = {path.name: path.read_bytes() for path in API_GOLDEN_DIR.glob("*.py")}
    assert set(generated) == set(golden)
    assert [name for name in sorted(golden) if generated[name] != golden[name]] == []


def test_generation_is_deterministic(
    tmp_path: Path, repo_root: Path, read_modules: Callable[[Path], dict[str, bytes]]
) -> None:
    first = _generate_api(tmp_path, repo_root, "first")
    second = _generate_api(tmp_path, repo_root, "second")
    assert read_modules(first) == read_modules(second)


def test_stale_api_modules_are_removed(tmp_path: Path, repo_root: Path) -> None:
    api_dir = tmp_path / "api"
    api_dir.mkdir()
    stale = api_dir / "stale.py"
    stale.write_text("STALE = True\n", encoding="utf-8")
    _generate_api(tmp_path, repo_root, "api")
    assert not stale.exists()


def test_generated_modules_import_only_allowed_roots(tmp_path: Path, repo_root: Path) -> None:
    api_dir = _generate_api(tmp_path, repo_root, "api")
    allowed = {"__future__", "builtins", "typing", "datetime", "collections.abc", "functools"}
    for path in api_dir.glob("*.py"):
        tree = ast.parse(path.read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    assert alias.name.split(".")[0] in allowed or alias.name.startswith("pyfj")
            elif isinstance(node, ast.ImportFrom) and node.module is not None:
                assert (
                    node.module in allowed
                    or node.module.startswith("pyfj._runtime")
                    or node.module.startswith("pyfj._generated")
                )


def test_report_lists_every_operation(api_ir: IR, api_naming: Naming, api_plans: tuple[EndpointPlan, ...]) -> None:
    report = render_report(api_naming, api_plans, mapping=Overrides(), registry=Registry())
    assert report.startswith("# pyfj naming report")
    for plan in api_plans:
        assert f"`{plan.operation.operation_id}`" in report
    assert "Operations in the Spec: **" in report
