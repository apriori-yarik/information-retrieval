from tokenization import simple_tokenize


def test_lowercases_and_strips_punctuation():
    assert simple_tokenize("Hello, World! Hello again.") == ["hello", "world", "hello", "again"]


def test_empty():
    assert simple_tokenize("") == []
