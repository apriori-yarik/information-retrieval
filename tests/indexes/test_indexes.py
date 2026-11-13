"""Shared contract every index must satisfy.

Add each index class you write to INDEX_CLASSES and these tests run against it.
"""

import pytest

from indexes import load_corpus

CORPUS = {
    0: "new home sales top forecasts",
    1: "home sales rise in july",
    2: "increase in home sales in july",
    3: "july new home sales rise",
}

# e.g. from indexes.inverted_index import InvertedIndex  ->  [InvertedIndex]
INDEX_CLASSES: list[type] = []


@pytest.fixture(params=INDEX_CLASSES, ids=lambda cls: cls.__name__)
def index(request):
    return request.param().build(CORPUS)


def test_counts_documents(index):
    assert len(index) == 4


def test_search_existing_term(index):
    assert index.search("july") == {1, 2, 3}
    assert index.search("forecasts") == {0}


def test_search_missing_term(index):
    assert index.search("nonexistent") == set()


def test_search_is_case_insensitive(index):
    assert index.search("JULY") == {1, 2, 3}


def test_vocabulary(index):
    assert index.vocabulary == {
        "new", "home", "sales", "top", "forecasts",
        "rise", "in", "july", "increase",
    }


def test_load_sample_corpus():
    corpus = load_corpus("data/sample")
    assert sorted(corpus) == [0, 1, 2]
    assert "Caesar" in corpus[0]
