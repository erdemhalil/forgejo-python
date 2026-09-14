"""Decode a successful HTTP response into the documented return type.

Frozen generated-code hook: generated code calls ``decode(response, Model)``,
``decode(response, list[Model])``, or ``decode(response, <scalar>)``;
``decode`` expects a 2xx response (the client request hooks raise for everything
else). The overloads below are the contract generated code binds to.

Supported ``model`` arguments:

- a pydantic model class → validates the JSON body to that model;
- ``list[Model]`` → validates a JSON array to a list of models;
- ``bool``, ``int``, ``float`` → validates a JSON scalar;
- ``list[str]`` and ``dict[str, str | int | float | bool]`` → validates a JSON
  array or object of scalars (integers must not be JSON booleans);
- ``str`` → the response text (``text/*``, ``text/html``);
- ``bytes`` → the raw response body (``application/zip``,
  ``application/octet-stream``, ``application/gzip``);
- ``None`` → ``None`` (204/205 operations).

Anything else, an undecodable JSON body, or a body that fails validation raises
:class:`~pyfj._runtime.errors.DecodeError`.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, get_args, get_origin, overload

from pydantic import BaseModel, ValidationError

from pyfj._runtime.errors import DecodeError

if TYPE_CHECKING:
    import httpx2

__all__ = ["decode"]

ModelT = TypeVar("ModelT", bound=BaseModel)
ScalarT = TypeVar("ScalarT", str, int, float, bool)

_SCALAR_EXPECTATIONS: dict[type, str] = {
    str: "a JSON string",
    bool: "a JSON boolean",
    int: "a JSON integer",
    float: "a JSON number",
}


@overload
def decode(response: httpx2.Response, model: type[ModelT]) -> ModelT: ...


@overload
def decode(response: httpx2.Response, model: type[list[ModelT]]) -> list[ModelT]: ...


@overload
def decode(response: httpx2.Response, model: type[ScalarT]) -> ScalarT: ...


@overload
def decode(response: httpx2.Response, model: type[list[ScalarT]]) -> list[ScalarT]: ...


@overload
def decode(response: httpx2.Response, model: type[dict[str, ScalarT]]) -> dict[str, ScalarT]: ...


@overload
def decode(response: httpx2.Response, model: type[bytes]) -> bytes: ...


@overload
def decode(response: httpx2.Response, model: None = None) -> None: ...


def decode(response: httpx2.Response, model: object | None = None) -> object:
    """Decode ``response`` to the declared type.

    Raises:
        DecodeError: the body cannot be decoded to ``model``.
    """
    if response.status_code in (204, 205):
        return None
    if model is None:
        return None
    if model is str:
        return response.text
    if model is bytes:
        return response.content
    if isinstance(model, type) and model in _SCALAR_EXPECTATIONS:
        return _coerce_scalar(_decode_json(response), model, response, where="")
    origin = get_origin(model)
    if origin is list:
        elements = get_args(model)
        if len(elements) == 1 and isinstance(elements[0], type):
            if issubclass(elements[0], BaseModel):
                return _decode_list(response, elements[0])
            if elements[0] in _SCALAR_EXPECTATIONS:
                return _decode_scalar_list(response, elements[0])
    elif origin is dict:
        arguments = get_args(model)
        if (
            len(arguments) == 2
            and arguments[0] is str
            and isinstance(arguments[1], type)
            and arguments[1] in _SCALAR_EXPECTATIONS
        ):
            return _decode_scalar_dict(response, arguments[1])
    if isinstance(model, type) and issubclass(model, BaseModel):
        payload = _decode_json(response)
        try:
            return model.model_validate(payload)
        except ValidationError as exc:
            raise DecodeError(response, str(exc)) from exc
    reason = f"unsupported model type: {model!r}"
    raise DecodeError(response, reason)


def _coerce_scalar(value: object, expected: type, response: httpx2.Response, *, where: str) -> object:
    """Validate one JSON scalar, rejecting booleans where an integer is declared."""
    if expected is bool:
        ok = isinstance(value, bool)
    elif expected is int:
        ok = isinstance(value, int) and not isinstance(value, bool)
    elif expected is float:
        ok = isinstance(value, (int, float)) and not isinstance(value, bool)
        if ok:
            value = float(value)
    else:
        ok = isinstance(value, str)
    if not ok:
        reason = f"{where}expected {_SCALAR_EXPECTATIONS[expected]}, got {type(value).__name__}"
        raise DecodeError(response, reason)
    return value


def _decode_json(response: httpx2.Response) -> object:
    """Parse the response body as JSON, wrapping failures in ``DecodeError``."""
    try:
        return response.json()
    except ValueError as exc:
        raise DecodeError(response, str(exc)) from exc


def _decode_list(response: httpx2.Response, model: type[ModelT]) -> list[ModelT]:
    """Validate a JSON array body to a list of ``model``."""
    payload = _decode_json(response)
    if not isinstance(payload, list):
        reason = f"expected a JSON array, got {type(payload).__name__}"
        raise DecodeError(response, reason)
    items: list[ModelT] = []
    for index, item in enumerate(payload):
        try:
            items.append(model.model_validate(item))
        except ValidationError as exc:
            reason = f"item {index}: {exc}"
            raise DecodeError(response, reason) from exc
    return items


def _decode_scalar_list(response: httpx2.Response, expected: type) -> list[object]:
    """Validate a JSON array body to a list of scalars."""
    payload = _decode_json(response)
    if not isinstance(payload, list):
        reason = f"expected a JSON array, got {type(payload).__name__}"
        raise DecodeError(response, reason)
    return [_coerce_scalar(item, expected, response, where=f"item {index}: ") for index, item in enumerate(payload)]


def _decode_scalar_dict(response: httpx2.Response, expected: type) -> dict[str, object]:
    """Validate a JSON object body to a dict with string keys and scalar values."""
    payload = _decode_json(response)
    if not isinstance(payload, dict):
        reason = f"expected a JSON object, got {type(payload).__name__}"
        raise DecodeError(response, reason)
    values: dict[str, object] = {}
    for key, value in payload.items():
        if not isinstance(key, str):
            reason = f"expected JSON object keys to be strings, got {type(key).__name__}"
            raise DecodeError(response, reason)
        values[key] = _coerce_scalar(value, expected, response, where=f"value for key {key!r}: ")
    return values
