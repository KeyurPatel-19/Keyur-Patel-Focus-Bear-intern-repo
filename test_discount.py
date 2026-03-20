import pytest
from discount import calculate_discount

def test_regular_discount():
    assert calculate_discount(100, 20) == 80

def test_zero_discount():
    assert calculate_discount(100, 0) == 100

def test_full_discount():
    assert calculate_discount(100, 100) == 0

def test_negative_price():
    with pytest.raises(ValueError):
        calculate_discount(-100, 20)

def test_invalid_discount_above_100():
    with pytest.raises(ValueError):
        calculate_discount(100, 120)

def test_invalid_discount_negative():
    with pytest.raises(ValueError):
        calculate_discount(100, -5)