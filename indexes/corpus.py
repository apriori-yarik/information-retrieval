"""Loading document collections from disk."""

from __future__ import annotations

from pathlib import Path


def load_corpus(directory: str | Path, pattern: str = "*.txt") -> dict[int, str]:
    """Read every file matching `pattern` in `directory`.

    Files are sorted by name and given ids 0, 1, 2, ...
    Returns a mapping doc_id -> document text.
    """
    paths = sorted(Path(directory).glob(pattern))
    return {doc_id: path.read_text(encoding="utf-8") for doc_id, path in enumerate(paths)}
