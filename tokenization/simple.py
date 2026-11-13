"""Simple regex tokenizer: lowercase word characters."""

from __future__ import annotations

import re

_TOKEN_RE = re.compile(r"\w+", re.UNICODE)


def simple_tokenize(text: str) -> list[str]:
    """Split text into lowercase word tokens.

    >>> simple_tokenize("Hello, World! Hello again.")
    ['hello', 'world', 'hello', 'again']
    """
    return [token.lower() for token in _TOKEN_RE.findall(text)]
