"""Tokenizers: functions that turn raw text into a list of terms.

Any callable matching `Tokenizer` (str -> list[str]) can be passed to an index.
"""

from tokenization.base import Tokenizer
from tokenization.simple import simple_tokenize

__all__ = ["Tokenizer", "simple_tokenize"]
