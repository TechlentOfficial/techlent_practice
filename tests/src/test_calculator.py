from app.src.calculator import Calculator


cal = Calculator()

def test_add():
    assert cal.add(1, 1) == 2
    assert cal.add(1, 2) == 3


def test_subtract():
    assert cal.add(2, 1) == 1
