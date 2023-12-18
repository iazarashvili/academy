from Bitcamp.tests.calculator import square


def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(4) == 16


def test_negative():
    assert square(-2) == 4
