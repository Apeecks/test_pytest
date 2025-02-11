from src.calculate_taxes import calculate_taxes

import pytest


def test_calculate_taxes_zero(value_zero_prices):
    with pytest.raises(ValueError) as file:
        calculate_taxes(value_zero_prices[0], value_zero_prices[1])
    assert str(file.value) == 'Неверная цена'

def test_calculate_taxes_zero_rate(value_zero_rate):
    with pytest.raises(ValueError) as file:
        calculate_taxes(value_zero_rate[0], value_zero_rate[1])
    assert str(file.value) == 'Неверный налоговый процент'

@pytest.mark.parametrize ("prices, tax_rate, result", [
    ([100], 1.0, [101]),
    ([200], 1.0, [202]),
    ([300], 1.0, [303])
])
def test_calculate_taxes_parametrise(prices, tax_rate, result):
    assert calculate_taxes(prices, tax_rate) == result
