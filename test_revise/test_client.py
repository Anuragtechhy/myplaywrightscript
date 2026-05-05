import pytest


@pytest.fixture(scope='function')
def test_1():
    print("setup")
    assert True == True

@pytest.mark.skip(reason='not needed')
def test_2(test_1):
    print("test 2")


def test_3(test_1):
    print("test 3")
