"""Spec loading, validation, and ``$ref`` resolution tests."""

from __future__ import annotations

import copy
import json
from typing import TYPE_CHECKING, Any

import pytest

from codegen.spec import Spec, SpecError, load_spec

if TYPE_CHECKING:
    from pathlib import Path


def _write_spec(tmp_path: Path, data: object) -> Path:
    path = tmp_path / "spec.json"
    path.write_text(json.dumps(data), encoding="utf-8")
    return path


def test_loads_the_vendored_spec(real_spec: Spec) -> None:
    assert real_spec.title == "Forgejo API"
    assert real_spec.version == "16.0.4+gitea-1.22.0"
    assert real_spec.base_path == "/api/v1"
    assert len(real_spec.definitions) == 246
    assert len(real_spec.responses) == 174
    assert len(real_spec.parameters) == 0
    assert sum(len(path.operations) for path in real_spec.paths) == 506


def test_operation_ids_are_unique(real_spec: Spec) -> None:
    ids = [operation.operation_id for path in real_spec.paths for operation in path.operations]
    assert len(ids) == len(set(ids)) == 506


def test_resolves_all_three_reference_sections(mini_spec: Spec) -> None:
    assert mini_spec.resolve_schema("#/definitions/Widget").type == "object"
    assert mini_spec.resolve_parameter("#/parameters/Page").name == "page"
    assert mini_spec.resolve_response("#/responses/WidgetList").schema is not None


def test_path_level_parameters_are_kept_on_the_path_item(mini_spec: Spec) -> None:
    item = next(path for path in mini_spec.paths if path.path == "/widgets/{id}")
    assert [parameter.name for parameter in item.parameters] == ["id"]
    assert item.parameters[0].required is True


def test_operation_metadata_round_trips(mini_spec: Spec) -> None:
    operations = {operation.operation_id: operation for path in mini_spec.paths for operation in path.operations}
    deprecated = operations["widgetUpdateDeprecated"]
    assert deprecated.deprecated is True
    assert deprecated.method == "PUT"
    assert deprecated.tags == ("widget",)
    report = operations["widgetReport"]
    assert report.produces == ("text/plain",)
    empty = next(response for response in operations["widgetDelete"].responses if response.status == 204)
    assert empty.schema is None
    payload = operations["widgetSearch"].responses[0]
    assert payload.schema is not None
    assert payload.schema.title == "WidgetSearchResults"


def test_reusable_response_without_schema_is_resolved(mini_spec: Spec) -> None:
    response = mini_spec.resolve_response("#/responses/Empty")
    assert response.description == "No content"
    assert response.schema is None


def test_missing_file_is_a_loud_error(tmp_path: Path) -> None:
    with pytest.raises(SpecError, match="cannot read Spec"):
        load_spec(tmp_path / "missing.json")


def test_invalid_json_is_a_loud_error(tmp_path: Path) -> None:
    path = tmp_path / "spec.json"
    path.write_text("{not json", encoding="utf-8")
    with pytest.raises(SpecError, match="invalid JSON"):
        load_spec(path)


def test_wrong_swagger_version_is_rejected(tmp_path: Path, minimal_spec_data: dict[str, Any]) -> None:
    minimal_spec_data["swagger"] = "3.0.0"
    with pytest.raises(SpecError, match=r"Swagger 2\.0"):
        load_spec(_write_spec(tmp_path, minimal_spec_data))


def test_unknown_key_is_rejected(tmp_path: Path, minimal_spec_data: dict[str, Any]) -> None:
    minimal_spec_data["paths"]["/things"]["get"]["unexpected"] = True  # type: ignore[index]
    with pytest.raises(SpecError, match="unexpected key 'unexpected'"):
        load_spec(_write_spec(tmp_path, minimal_spec_data))


def test_nullability_marker_is_rejected(tmp_path: Path, minimal_spec_data: dict[str, Any]) -> None:
    minimal_spec_data["definitions"] = {
        "Thing": {"type": "object", "properties": {"id": {"type": "integer", "x-nullable": True}}}
    }
    with pytest.raises(SpecError, match="nullability markers are not modelled"):
        load_spec(_write_spec(tmp_path, minimal_spec_data))


def test_schema_combinator_is_rejected(tmp_path: Path, minimal_spec_data: dict[str, Any]) -> None:
    minimal_spec_data["definitions"] = {"Thing": {"allOf": [{"type": "object"}]}}
    with pytest.raises(SpecError, match="combinator 'allOf' is not supported"):
        load_spec(_write_spec(tmp_path, minimal_spec_data))


def test_dangling_definition_ref_is_rejected(tmp_path: Path, minimal_spec_data: dict[str, Any]) -> None:
    minimal_spec_data["definitions"] = {
        "Thing": {"type": "object", "properties": {"other": {"$ref": "#/definitions/Missing"}}}
    }
    with pytest.raises(SpecError, match="dangling \\$ref '#/definitions/Missing'"):
        load_spec(_write_spec(tmp_path, minimal_spec_data))


def test_dangling_parameter_ref_is_rejected(tmp_path: Path, minimal_spec_data: dict[str, Any]) -> None:
    minimal_spec_data["paths"]["/things"]["get"]["parameters"] = [{"$ref": "#/parameters/Missing"}]  # type: ignore[index]
    with pytest.raises(SpecError, match="no reusable parameter named 'Missing'"):
        load_spec(_write_spec(tmp_path, minimal_spec_data))


def test_dangling_response_ref_is_rejected(tmp_path: Path, minimal_spec_data: dict[str, Any]) -> None:
    minimal_spec_data["paths"]["/things"]["get"]["responses"] = {"200": {"$ref": "#/responses/Missing"}}  # type: ignore[index]
    with pytest.raises(SpecError, match="no reusable response named 'Missing'"):
        load_spec(_write_spec(tmp_path, minimal_spec_data))


def test_duplicate_operation_id_is_rejected(tmp_path: Path, minimal_spec_data: dict[str, Any]) -> None:
    minimal_spec_data["paths"] = {
        "/things": {"get": {"operationId": "same", "responses": {"200": {"description": "ok"}}}},
        "/others": {"get": {"operationId": "same", "responses": {"200": {"description": "ok"}}}},
    }
    with pytest.raises(SpecError, match="duplicate operationId 'same'"):
        load_spec(_write_spec(tmp_path, minimal_spec_data))


def test_path_item_ref_is_rejected(tmp_path: Path, minimal_spec_data: dict[str, Any]) -> None:
    minimal_spec_data["paths"]["/things"] = {"$ref": "#/paths/other"}  # type: ignore[index]
    with pytest.raises(SpecError, match="path-item \\$ref is not supported"):
        load_spec(_write_spec(tmp_path, minimal_spec_data))


def test_per_operation_security_is_rejected(tmp_path: Path, minimal_spec_data: dict[str, Any]) -> None:
    minimal_spec_data["paths"]["/things"]["get"]["security"] = [{"BasicAuth": []}]  # type: ignore[index]
    with pytest.raises(SpecError, match="per-operation security is not supported"):
        load_spec(_write_spec(tmp_path, minimal_spec_data))


def test_unsupported_schema_type_is_rejected(tmp_path: Path, minimal_spec_data: dict[str, Any]) -> None:
    minimal_spec_data["definitions"] = {"Thing": {"type": "object", "properties": {"weird": {"type": "null"}}}}
    with pytest.raises(SpecError, match="unsupported type 'null'"):
        load_spec(_write_spec(tmp_path, minimal_spec_data))


def test_array_without_items_is_rejected(tmp_path: Path, minimal_spec_data: dict[str, Any]) -> None:
    minimal_spec_data["definitions"] = {"Thing": {"type": "object", "properties": {"items": {"type": "array"}}}}
    with pytest.raises(SpecError, match="array schema requires items"):
        load_spec(_write_spec(tmp_path, minimal_spec_data))


def test_duplicate_parameter_is_rejected(tmp_path: Path, minimal_spec_data: dict[str, Any]) -> None:
    parameter = {"name": "q", "in": "query", "type": "string"}
    minimal_spec_data["paths"]["/things"]["get"]["parameters"] = [parameter, copy.deepcopy(parameter)]  # type: ignore[index]
    with pytest.raises(SpecError, match="duplicate parameter 'q' in 'query'"):
        load_spec(_write_spec(tmp_path, minimal_spec_data))


def test_empty_enum_is_rejected(tmp_path: Path, minimal_spec_data: dict[str, Any]) -> None:
    minimal_spec_data["definitions"] = {
        "Thing": {"type": "object", "properties": {"kind": {"type": "string", "enum": []}}}
    }
    with pytest.raises(SpecError, match="enum must not be empty"):
        load_spec(_write_spec(tmp_path, minimal_spec_data))


def test_required_property_must_exist(tmp_path: Path, minimal_spec_data: dict[str, Any]) -> None:
    minimal_spec_data["definitions"] = {
        "Thing": {"type": "object", "required": ["missing"], "properties": {"id": {"type": "integer"}}}
    }
    with pytest.raises(SpecError, match="'missing' is not one of the declared properties"):
        load_spec(_write_spec(tmp_path, minimal_spec_data))


def test_reusable_parameters_are_resolved_into_operations(tmp_path: Path, minimal_spec_data: dict[str, Any]) -> None:
    minimal_spec_data["parameters"] = {"Limit": {"name": "limit", "in": "query", "type": "integer"}}
    minimal_spec_data["paths"]["/things"]["get"]["parameters"] = [{"$ref": "#/parameters/Limit"}]  # type: ignore[index]
    spec = load_spec(_write_spec(tmp_path, minimal_spec_data))
    operation = spec.paths[0].operations[0]
    assert [(parameter.name, parameter.location) for parameter in operation.parameters] == [("limit", "query")]
