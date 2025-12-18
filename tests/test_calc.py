from decimal import Decimal
from src.calc import multiply, divide


def test_multiply_integers():
    assert multiply(2, 3) == Decimal('6')


def test_multiply_floats():
    assert multiply('1.5', '2') == Decimal('3.0')


def test_divide_normal():
    assert divide('3', '2') == Decimal('1.5')


def test_divide_by_zero():
    assert divide('1', '0') == 'Infinity'


def test_invalid_input():
    import pytest
    with pytest.raises(ValueError):
        multiply('abc', 1)
