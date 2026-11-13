"""Common interface for all index implementations."""

from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Iterable, Mapping

from tokenization import Tokenizer, simple_tokenize


class BaseIndex(ABC):
    """Base class every index implements.

    Subclasses must implement `add_document`, `search` and `vocabulary`.
    """

    def __init__(self, tokenizer: Tokenizer = simple_tokenize) -> None:
        self.tokenizer = tokenizer
        self.doc_ids: set[int] = set()

    def build(self, documents: Mapping[int, str] | Iterable[tuple[int, str]]) -> BaseIndex:
        """Index a whole collection. Accepts a dict or (doc_id, text) pairs."""
        items = documents.items() if isinstance(documents, Mapping) else documents
        for doc_id, text in items:
            self.add_document(doc_id, text)
        return self

    @abstractmethod
    def add_document(self, doc_id: int, text: str) -> None:
        """Add a single document to the index.

        Implementations should tokenize with `self.tokenizer(text)`
        and register `doc_id` in `self.doc_ids`.
        """

    @abstractmethod
    def search(self, term: str) -> set[int]:
        """Return ids of documents containing `term` (empty set if none)."""

    @property
    @abstractmethod
    def vocabulary(self) -> set[str]:
        """All distinct terms in the index."""

    def __len__(self) -> int:
        return len(self.doc_ids)
