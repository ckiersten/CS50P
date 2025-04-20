import pytest
from plates import is_valid

def test_beginning():
    assert is_valid("aa")
    assert not is_valid("11")

def test_num_of_characters():
    assert not is_valid("a")
    assert not is_valid("aaaaaaa")

def test_num():
    assert is_valid("aaa222")
    assert not is_valid("aaa22a")
    assert not is_valid("aaa022")

def test_punc():
    assert not is_valid("aab .!")
