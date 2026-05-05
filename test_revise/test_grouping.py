import pytest

@pytest.mark.sanity
def test_loginbyphone():
    print("test_sanity")

@pytest.mark.regression
def test_signupbypnone():
    print("test_regression")

@pytest.mark.regression
def test_loginbyname():
    print("test_regression")

@pytest.mark.regression
def test_signupbyname():
    print("test_regression")



