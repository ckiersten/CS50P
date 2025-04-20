import pytest
import fuel

def test_convert():
    assert fuel.convert("1/2") == 50
    with pytest.raises(ValueError):
        fuel.convert("cat/dog")
        fuel.convert("2/1")
    with pytest.raises(ZeroDivisionError):
        fuel.convert("1/0")


def test_gauge():
    assert fuel.gauge(100) == "F"
    assert fuel.gauge(99) == "F"
    assert fuel.gauge(50) == "50%"
    assert fuel.gauge(1) == "E"
    assert fuel.gauge(0) == "E"
