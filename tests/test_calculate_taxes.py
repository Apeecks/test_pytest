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


def test_calculate_taxes_prices_tax_error():
    with pytest.raises(ValueError) as file:
        calculate_taxes([100], 100)
    assert str(file.value) == 'Неверный налоговый процент'


@pytest.mark.parametrize ("prices, tax_rate, discount, result", [
    ([100], 2.0, 10, [91.80]),
    ([950], 3.0, 7.0, [910.00]),
    ([111], 7.0, 13, [103.33])
])
def test_calculate_taxes_discount(prices, tax_rate, discount, result):
    assert calculate_taxes(prices, tax_rate, discount) == result


def test_calculate_taxes_error_type():
    with pytest.raises(TypeError) as file:
        calculate_taxes([100], 1.0, "Привет")
    assert str(file.value) == 'Ошибка типа данных'