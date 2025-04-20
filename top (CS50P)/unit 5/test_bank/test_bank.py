import pytest
from bank import value

def test_str():
    assert value("hello world") == 0
    assert value("hey") == 20
    assert value("yo") == 100
    assert value("HELLO") == 0
