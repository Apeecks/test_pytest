from typing import Union


def calculate_taxes(prices: list[float], tax_rate: float, discount: Union[int, float]=0) -> list[float]:
    """Функция вычисляет стоимость товаров с учётом налога."""

    if tax_rate < 0:
        raise ValueError('Неверный налоговый процент')
    elif tax_rate == prices[0]:
        raise ValueError('Неверный налоговый процент')

    if type(discount) != int:
        if type(discount) != float:
            raise TypeError('Ошибка типа данных')

    taxed_prices = []
    taxed_prices_discount_list = []

    for price in prices:
        if price <= 0:
            raise ValueError('Неверная цена')
        tax = price * tax_rate / 100
        taxed_prices.append(tax + price)


    if discount == 0:
        return taxed_prices
    else:
        for taxed_price in taxed_prices:
            taxed_prices_discount = taxed_price - (taxed_price / 100 * discount)
            taxed_prices_discount_list.append(round(taxed_prices_discount, 2))
        return taxed_prices_discount_list
