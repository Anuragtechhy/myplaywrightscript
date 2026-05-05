import pytest

@pytest.fixture
def test_a(scope='module'):
    print("this is fixture")


def test_b(test_a):
    print("hello a")

def test_b(test_a):
   print("hello b")





