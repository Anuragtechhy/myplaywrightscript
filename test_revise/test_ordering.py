import pytest


@pytest.mark.order(2)
def test_order():
    print("test_order 2")


@pytest.mark.order(1)
def test_order1():
    print("test_order1 1")


@pytest.mark.order(3)
def test_order3():
    print("test_order3 3")
