from seasons import amount_minutes
import pytest

def test_amount_minutes():
    assert amount_minutes("2024-02-17") == "Five hundred twenty-seven thousand forty minutes"
    assert amount_minutes("2023-02-17") == "One million, fifty-two thousand, six hundred forty minutes"
    with pytest.raises(SystemExit):
        amount_minutes("January 1, 1999")


