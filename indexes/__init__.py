"""Module 1: indexes.

Different ways of indexing a document collection
(direct index, inverted index, incidence matrix, ...).
Every index subclasses `BaseIndex`.
"""

from indexes.base import BaseIndex
from indexes.corpus import load_corpus

__all__ = [
    "BaseIndex",
    "load_corpus",
]
