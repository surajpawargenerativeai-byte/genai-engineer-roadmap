from src.utils import square, is_even, safe_divide


def test_square():
    assert square(4) == 16


def test_is_even():
    assert is_even(10) is True
    assert is_even(7) is False


def test_safe_divide():
    assert safe_divide(10, 2) == 5