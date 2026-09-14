"""IR edge-case tests: naming, types, optionality, and operation data."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any

import pytest

from codegen.ir import (
    IR,
    ListType,
    MapType,
    NamedRef,
    ScalarType,
    build_ir,
    enum_member_name,
    pascal_case,
    snake_case,
)
from codegen.spec import HTTP_METHODS, SpecError, load_spec

if TYPE_CHECKING:
    from pathlib import Path


def _load(tmp_path: Path, data: object) -> IR:
    path = tmp_path / "spec.json"
    path.write_text(json.dumps(data), encoding="utf-8")
    return build_ir(load_spec(path))


@pytest.mark.parametrize(
    ("wire", "expected"),
    [
        ("already_snake", "already_snake"),
        ("camelCase", "camel_case"),
        ("PascalCase", "pascal_case"),
        ("@context", "context"),
        ("_links", "links"),
        ("Do", "do"),
        ("MergeCommitID", "merge_commit_id"),
        ("type", "type"),
        ("from", "from_"),
        ("9lives", "_9lives"),
        ("", "field"),
    ],
)
def test_snake_case(wire: str, expected: str) -> None:
    assert snake_case(wire) == expected


@pytest.mark.parametrize(
    ("wire", "expected"),
    [("contained_in", "ContainedIn"), ("@context", "Context"), ("Do", "Do"), ("", "Type")],
)
def test_pascal_case(wire: str, expected: str) -> None:
    assert pascal_case(wire) == expected


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("rebase-merge", "REBASE_MERGE"),
        ("fast-forward-only", "FAST_FORWARD_ONLY"),
        ("someValue", "SOME_VALUE"),
        (1, "_1"),
        (-2, "_2"),
    ],
)
def test_enum_member_name(value: str | int, expected: str) -> None:
    assert enum_member_name(value) == expected


def test_all_definitions_become_typedefs(mini_ir: IR) -> None:
    assert len(mini_ir.definitions) == 12
    assert len(mini_ir.types) == 13  # 12 definitions + the inline search result model
    kinds = {type_def.name: type_def.kind for type_def in mini_ir.definitions}
    assert kinds["Widget"] == "model"
    assert kinds["State"] == "alias"
    assert kinds["Priority"] == "enum"


def test_types_are_sorted_by_module(mini_ir: IR) -> None:
    modules = [type_def.module for type_def in mini_ir.types]
    assert modules == sorted(modules)
    assert len(set(modules)) == len(modules)


def test_required_and_optional_fields(mini_ir: IR) -> None:
    widget = mini_ir.types_by_name["Widget"]
    required = {field.name for field in widget.fields if field.required}
    assert required == {"id", "name"}
    optional = {field.name for field in widget.fields if not field.required}
    assert "state" in optional
    assert "parent" in optional


def test_field_aliases_track_the_wire_name(mini_ir: IR) -> None:
    widget = mini_ir.types_by_name["Widget"]
    fields = {field.name: field for field in widget.fields}
    assert fields["context"].wire_name == "@context"
    assert fields["links"].wire_name == "_links"
    assert fields["camel_case"].wire_name == "CamelCase"
    assert fields["id"].wire_name == "id"


def test_scalar_formats_map_to_datetime_and_date(mini_ir: IR) -> None:
    widget = mini_ir.types_by_name["Widget"]
    fields = {field.name: field for field in widget.fields}
    assert fields["created_at"].type == ScalarType("datetime", format="date-time")
    assert fields["birthday"].type == ScalarType("date", format="date")
    assert fields["id"].type == ScalarType("integer", format="int64")


def test_inline_string_and_integer_enums(mini_ir: IR) -> None:
    kind = mini_ir.types_by_name["WidgetKind"]
    assert kind.kind == "enum"
    assert kind.enum_base == "str"
    assert [(value.name, value.value) for value in kind.enum_values] == [
        ("STANDARD", "standard"),
        ("DELUXE", "deluxe"),
        ("LIMITED_EDITION", "limited-edition"),
    ]
    priority = mini_ir.types_by_name["WidgetPriority"]
    assert priority.enum_base == "int"
    assert [value.name for value in priority.enum_values] == ["_1", "_2", "_3"]


def test_definition_level_enum(mini_ir: IR) -> None:
    priority = mini_ir.types_by_name["Priority"]
    assert priority.kind == "enum"
    assert priority.enum_base == "int"
    assert priority.module == "priority"


def test_arrays_maps_and_any(mini_ir: IR) -> None:
    widget = mini_ir.types_by_name["Widget"]
    fields = {field.name: field for field in widget.fields}
    assert fields["labels"].type == ListType(ScalarType("string"))
    assert fields["parts"].type == ListType(NamedRef("Part", "part", "model"))
    assert fields["scores"].type == ListType(ScalarType("any"))
    assert fields["attributes"].type == MapType(ScalarType("string"))
    assert fields["anything"].type == MapType(ScalarType("any"))
    assert fields["metadata"].type == MapType(ScalarType("any"))


def test_nested_inline_model(mini_ir: IR) -> None:
    detail = mini_ir.types_by_name["WidgetDetail"]
    assert detail.module == "widget"
    assert detail.spec_name == "Widget.detail"
    widget = mini_ir.types_by_name["Widget"]
    assert [node.name for node in widget.nested] == ["WidgetKind", "WidgetPriority", "WidgetDetail"]
    widget_fields = {field.name: field for field in widget.fields}
    assert widget_fields["detail"].type == NamedRef("WidgetDetail", "widget", "model")


def test_self_reference(mini_ir: IR) -> None:
    widget_fields = {field.name: field for field in mini_ir.types_by_name["Widget"].fields}
    assert widget_fields["parent"].type == NamedRef("Widget", "widget", "model")


def test_alias_targets(mini_ir: IR) -> None:
    defs = mini_ir.types_by_name
    assert defs["State"].alias_target == ScalarType("string")
    assert defs["Duration"].alias_target == ScalarType("integer", format="int64")
    assert defs["Labels"].alias_target == ListType(ScalarType("string"))
    assert defs["WidgetAlias"].alias_target == NamedRef("Widget", "widget", "model")


def test_root_additional_properties_is_a_model(mini_ir: IR) -> None:
    config = mini_ir.types_by_name["Config"]
    assert config.kind == "model"
    assert config.fields == ()


def test_empty_object_definition_is_an_empty_model(mini_ir: IR) -> None:
    empty = mini_ir.types_by_name["EmptyModel"]
    assert empty.kind == "model"
    assert empty.fields == ()


def test_types_by_name_covers_nested_types(mini_ir: IR) -> None:
    assert "WidgetDetail" in mini_ir.types_by_name
    assert "WidgetKind" in mini_ir.types_by_name
    assert len(mini_ir.types_by_name) > len(mini_ir.types)


def test_operations_carry_path_segments(mini_ir: IR) -> None:
    operation = next(item for item in mini_ir.operations if item.operation_id == "widgetGet")
    assert [segment.template for segment in operation.segments] == ["widgets", "{id}"]
    assert operation.segments[1].parameters == ("id",)


def test_multi_parameter_segments(mini_ir: IR) -> None:
    operation = next(item for item in mini_ir.operations if item.operation_id == "widgetDownload")
    assert operation.segments[-1].template == "{id}.{format}"
    assert operation.segments[-1].parameters == ("id", "format")
    assert operation.produces == ("application/octet-stream",)
    assert operation.responses[0].type == ScalarType("bytes")


def test_path_level_parameters_merge_into_operations(mini_ir: IR) -> None:
    operation = next(item for item in mini_ir.operations if item.operation_id == "widgetGet")
    assert [(parameter.wire_name, parameter.location) for parameter in operation.parameters] == [("id", "path")]


def test_query_parameters_keep_enum_defaults_and_collection_format(mini_ir: IR) -> None:
    operation = next(item for item in mini_ir.operations if item.operation_id == "widgetList")
    parameters = {parameter.wire_name: parameter for parameter in operation.parameters}
    assert parameters["page"].has_default is True
    assert parameters["page"].default == 1
    assert parameters["sort"].type == ScalarType("string", enum=("alpha", "recent"))
    assert parameters["sort"].has_default is True
    assert parameters["labels"].type == ListType(ScalarType("integer", format="int64"))
    assert parameters["labels"].collection_format == "multi"
    assert parameters["labels"].required is False


def test_body_parameters_become_bodies(mini_ir: IR) -> None:
    operation = next(item for item in mini_ir.operations if item.operation_id == "widgetCreate")
    assert operation.body is not None
    assert operation.body.type == NamedRef("Widget", "widget", "model")
    assert operation.body.required is True
    assert operation.body.wire_name == "body"
    assert operation.body.consumes == ("application/json",)


def test_responses_keep_statuses_and_types(mini_ir: IR) -> None:
    create = next(item for item in mini_ir.operations if item.operation_id == "widgetCreate")
    responses = {response.status: response for response in create.responses}
    assert responses[422].type is None
    assert responses[201].type == NamedRef("Widget", "widget", "model")

    delete = next(item for item in mini_ir.operations if item.operation_id == "widgetDelete")
    assert delete.responses[0].status == 204
    assert delete.responses[0].type is None


def test_text_produces_and_string_responses(mini_ir: IR) -> None:
    report = next(item for item in mini_ir.operations if item.operation_id == "widgetReport")
    assert report.produces == ("text/plain",)
    assert report.responses[0].type == ScalarType("string")


def test_deprecated_operations_are_flagged(mini_ir: IR) -> None:
    operation = next(item for item in mini_ir.operations if item.operation_id == "widgetUpdateDeprecated")
    assert operation.deprecated is True


def test_inline_response_objects_become_titled_models(mini_ir: IR) -> None:
    search = next(item for item in mini_ir.operations if item.operation_id == "widgetSearch")
    assert search.responses[0].type == NamedRef("WidgetSearchResults", "widget_search_results", "model")
    model = mini_ir.types_by_name["WidgetSearchResults"]
    assert [(field.name, field.required) for field in model.fields] == [("items", False), ("total", False)]


def test_operations_are_sorted(mini_ir: IR) -> None:
    # Paths first, then Swagger's method order (get, put, post, delete, ...).
    keys = [(operation.path, HTTP_METHODS.index(operation.method.lower())) for operation in mini_ir.operations]
    assert keys == sorted(keys)


def test_field_name_collisions_fail_loudly(tmp_path: Path, minimal_spec_data: dict[str, Any]) -> None:
    data = minimal_spec_data
    data["definitions"] = {
        "Thing": {
            "type": "object",
            "properties": {"camelCase": {"type": "string"}, "camel_case": {"type": "string"}},
        }
    }
    with pytest.raises(SpecError, match="both map to Python field 'camel_case'"):
        _load(tmp_path, data)


def test_enum_member_collisions_fail_loudly(tmp_path: Path, minimal_spec_data: dict[str, Any]) -> None:
    data = minimal_spec_data
    data["definitions"] = {
        "Thing": {"type": "object", "properties": {"kind": {"type": "string", "enum": ["a-b", "a_b"]}}}
    }
    with pytest.raises(SpecError, match="collapse to duplicate member names"):
        _load(tmp_path, data)


def test_nested_type_name_collisions_fail_loudly(tmp_path: Path, minimal_spec_data: dict[str, Any]) -> None:
    data = minimal_spec_data
    data["definitions"] = {
        "Thing": {
            "type": "object",
            "properties": {"detail": {"type": "object", "properties": {"x": {"type": "string"}}}},
        },
        "ThingDetail": {"type": "object", "properties": {"y": {"type": "string"}}},
    }
    with pytest.raises(SpecError, match="generated type name 'ThingDetail' collides"):
        _load(tmp_path, data)


def test_module_collisions_fail_loudly(tmp_path: Path, minimal_spec_data: dict[str, Any]) -> None:
    data = minimal_spec_data
    data["definitions"] = {
        "MyThing": {"type": "object", "properties": {}},
        "My_Thing": {"type": "object", "properties": {}},
    }
    with pytest.raises(SpecError, match="module 'my_thing' is already used"):
        _load(tmp_path, data)


def test_model_name_overrides_apply_and_are_validated(tmp_path: Path, minimal_spec_data: dict[str, Any]) -> None:
    data = minimal_spec_data
    data["definitions"] = {"AwkwardName": {"type": "object", "properties": {}}}
    ir = _load(tmp_path, data)
    assert ir.types_by_name["AwkwardName"].module == "awkward_name"

    path = tmp_path / "spec.json"
    path.write_text(json.dumps(data), encoding="utf-8")
    renamed = build_ir(load_spec(path), model_names={"AwkwardName": "BetterName"})
    assert renamed.types_by_name["BetterName"].module == "awkward_name"
    assert "AwkwardName" not in renamed.types_by_name

    with pytest.raises(SpecError, match="unknown definitions"):
        build_ir(load_spec(path), model_names={"Missing": "X"})

    with pytest.raises(SpecError, match="not a valid Python class name"):
        build_ir(load_spec(path), model_names={"AwkwardName": "not-valid"})


def test_definition_types_are_ordered_by_spec_name(mini_ir: IR) -> None:
    names = [type_def.spec_name for type_def in mini_ir.definitions]
    assert names == sorted(names)


def test_ir_metadata(mini_ir: IR) -> None:
    assert mini_ir.title == "Mini API"
    assert mini_ir.version == "1.0.0"
    assert mini_ir.base_path == "/api/v1"
