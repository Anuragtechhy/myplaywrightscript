import pytest

@pytest.mark.order(2)
def test_a():
    print("this is a test")

@pytest.mark.order(1)
def test_b():
    print("this is b test")

@pytest.mark.order(3)
def test_c():
    print("this is c test")