import pytest


def fizzBuzz(inputValue):
    return str(inputValue)


def checkFizzBuzz(inputValue, expectedValue):
    retVal = fizzBuzz(inputValue)
    assert retVal == expectedValue


def test_return1With1PassedIn():
    checkFizzBuzz(1, "1")


def test_return2With2PassedIn():
    checkFizzBuzz(2, "2")


pytest.main(["-v", "--tb=line", "-rN", __file__])
