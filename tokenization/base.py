"""The tokenizer contract."""

from __future__ import annotations

from collections.abc import Callable

Tokenizer = Callable[[str], list[str]]
"""A tokenizer takes raw text and returns the list of terms in order."""
