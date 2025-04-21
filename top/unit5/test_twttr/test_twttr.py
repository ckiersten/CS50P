from twttr import shorten
import pytest

def test_str():
    assert shorten("twitter") == "twttr"
    assert shorten("bcd") == "bcd"
    assert shorten("twitter.") == "twttr."
    assert shorten("TWITTER") == "TWTTR"

def test_num():
    with pytest.raises(TypeError):
        assert shorten(1)
    assert shorten("twitter1") == "twttr1"

