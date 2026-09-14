"""pyfj's code generator package.

Run it with ``uv run python -m codegen``; the generator reads
``spec/openapi.json`` only (never the network) and writes
``src/pyfj/_generated/`` deterministically. See docs/development/codegen.md for the
pipeline and docs/development/architecture.md for the surface it must produce.

The package is split into ``spec.py`` (loader/validation/``$ref``
resolution), ``ir.py`` (the semantic IR the emitters consume), the model
and naming/API emitters, and the runner in ``__main__.py``.
"""

from __future__ import annotations
