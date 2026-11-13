# information-retrieval

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -e ".[dev]"
```

## Modules

### 1. `indexes/`

| File | What goes there |
| --- | --- |
| `base.py` | `BaseIndex` — shared interface (`add_document`, `search`, `vocabulary`, `build`) |
| `corpus.py` | `load_corpus` — reads a folder of `.txt` files into `{doc_id: text}` |

To add an index (direct, inverted, incidence matrix, ...), subclass `BaseIndex` in a new
file, export it from `indexes/__init__.py` and add it to `INDEX_CLASSES` in
`tests/indexes/test_indexes.py`.

Sample documents live in `data/sample/`.

### `tokenization/`

| File | What goes there |
| --- | --- |
| `base.py` | `Tokenizer` — the contract: any `str -> list[str]` callable |
| `simple.py` | `simple_tokenize` — lowercase `\w+` tokenizer, the default for indexes |

Add new tokenizers as new files here and pass them to an index:
`InvertedIndex(tokenizer=my_tokenize)`.

## Tests

```bash
python -m pytest
```
