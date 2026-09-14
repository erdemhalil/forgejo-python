"""Decoding responses to models, None, bytes, and str."""

from __future__ import annotations

import httpx2
import pytest
from _helpers import Issue
from pydantic import ValidationError

from pyfj._runtime import DecodeError, decode

_REQUEST = httpx2.Request("GET", "https://forgejo.test/api/v1/repos/alice/demo")


def _response(
    *,
    status: int = 200,
    json: object | None = None,
    text: str | None = None,
    content: bytes | None = None,
    content_type: str | None = None,
) -> httpx2.Response:
    headers = {"Content-Type": content_type} if content_type is not None else None
    if content is not None:
        return httpx2.Response(status, content=content, headers=headers, request=_REQUEST)
    return httpx2.Response(status, json=json, text=text, headers=headers, request=_REQUEST)


def test_model_round_trip() -> None:
    response = _response(json={"id": 1, "title": "Bug"})
    issue = decode(response, Issue)
    assert issue == Issue(id=1, title="Bug")


def test_list_of_models() -> None:
    response = _response(json=[{"id": 1, "title": "one"}, {"id": 2, "title": "two"}])
    issues = decode(response, list[Issue])
    assert issues == [Issue(id=1, title="one"), Issue(id=2, title="two")]


def test_empty_list() -> None:
    assert decode(_response(json=[]), list[Issue]) == []


def test_204_and_205_decode_to_none() -> None:
    assert decode(_response(status=204), Issue) is None
    assert decode(_response(status=205), None) is None
    assert decode(_response(status=204), None) is None


def test_none_model_returns_none_for_a_json_body() -> None:
    assert decode(_response(json={"ignored": True}), None) is None


def test_text_decodes_to_str() -> None:
    response = _response(text="<h1>README</h1>", content_type="text/html")
    assert decode(response, str) == "<h1>README</h1>"


def test_bytes_decodes_to_bytes() -> None:
    response = _response(content=b"\x00\x01", content_type="application/octet-stream")
    assert decode(response, bytes) == b"\x00\x01"


def test_invalid_json_raises_decode_error_with_cause() -> None:
    response = httpx2.Response(200, content=b"not json", request=_REQUEST)
    with pytest.raises(DecodeError) as caught:
        decode(response, Issue)
    assert isinstance(caught.value.__cause__, ValueError)
    assert caught.value.response is response


def test_model_validation_failure_raises_decode_error_with_cause() -> None:
    response = _response(json={"id": "not-an-int", "title": "Bug"})
    with pytest.raises(DecodeError) as caught:
        decode(response, Issue)
    assert isinstance(caught.value.__cause__, ValidationError)


def test_list_validation_failure_names_the_item() -> None:
    response = _response(json=[{"id": 1, "title": "ok"}, {"id": 2}])
    with pytest.raises(DecodeError, match="item 1") as caught:
        decode(response, list[Issue])
    assert isinstance(caught.value.__cause__, ValidationError)


def test_list_model_rejects_non_array_payload() -> None:
    with pytest.raises(DecodeError, match="expected a JSON array"):
        decode(_response(json={"id": 1, "title": "Bug"}), list[Issue])


def test_unsupported_model_argument_raises_decode_error() -> None:
    response = _response(json={"id": 1, "title": "Bug"})
    with pytest.raises(DecodeError, match="unsupported model type"):
        decode(response, dict)


def test_scalar_bool_round_trip() -> None:
    assert decode(_response(json=True), bool) is True


def test_scalar_int_rejects_json_boolean() -> None:
    with pytest.raises(DecodeError, match="expected a JSON integer, got bool"):
        decode(_response(json=True), int)


def test_scalar_float_accepts_integer_and_returns_float() -> None:
    value = decode(_response(json=3), float)
    assert value == 3.0
    assert isinstance(value, float)


def test_scalar_shape_mismatch_names_both_sides() -> None:
    with pytest.raises(DecodeError, match="expected a JSON boolean, got list"):
        decode(_response(json=[]), bool)


def test_list_of_scalars() -> None:
    assert decode(_response(json=["a", "b"]), list[str]) == ["a", "b"]


def test_scalar_list_rejects_non_array_payload() -> None:
    with pytest.raises(DecodeError, match="expected a JSON array"):
        decode(_response(json={"a": 1}), list[str])


def test_scalar_list_rejects_bad_item() -> None:
    with pytest.raises(DecodeError, match="item 1: expected a JSON string, got int"):
        decode(_response(json=["a", 2]), list[str])


def test_scalar_dict_with_int_values() -> None:
    assert decode(_response(json={"python": 1}), dict[str, int]) == {"python": 1}


def test_scalar_dict_rejects_non_object_payload() -> None:
    with pytest.raises(DecodeError, match="expected a JSON object"):
        decode(_response(json=[]), dict[str, str])


def test_scalar_dict_rejects_bad_value() -> None:
    with pytest.raises(DecodeError, match="value for key 'a': expected a JSON string, got int"):
        decode(_response(json={"a": 1}), dict[str, str])


def test_scalar_dict_int_rejects_json_boolean_value() -> None:
    with pytest.raises(DecodeError, match="value for key 'a': expected a JSON integer, got bool"):
        decode(_response(json={"a": True}), dict[str, int])


def test_decode_error_message_names_request() -> None:
    response = httpx2.Response(200, content=b"nope", request=_REQUEST)
    with pytest.raises(DecodeError) as caught:
        decode(response, Issue)
    assert "GET" in str(caught.value)
    assert "https://forgejo.test/api/v1/repos/alice/demo" in str(caught.value)
