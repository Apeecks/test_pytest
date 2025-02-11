import pytest


@pytest.fixture
def value_zero_prices():
    return [[-1], 2.0]

@pytest.fixture
def value_zero_rate():
    return [[100], -1.0]
