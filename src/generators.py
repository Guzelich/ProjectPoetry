from typing import Iterator


def filter_by_currency(usd_transactions: list, currency: str) -> Iterator:
    """Функция принимает на вход список словарей, представляющих транзакции"""
    for usd_transaction in usd_transactions:
        if (
            isinstance(usd_transaction, dict)
            and usd_transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency
        ):
            yield usd_transaction


def transaction_descriptions(usd_transactions: list) -> Iterator:
    """Генератор принимает список словарей с транзакциями и
    возвращает описание каждой операции по очереди"""
    for usd_transaction in usd_transactions:
        yield usd_transaction.get("description")


def card_number_generator(start: int, end: int) -> Iterator:
    """Генератор выдает номера банковских карт
    в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты"""
    min_card = 1
    max_card = 9999999999999999
    if start < min_card:
        raise ValueError("Начальное значение не может быть меньше 1")
    if end > max_card:
        raise ValueError("Конечное значение не может быть больше 9999999999999999")
    if start > end:
        raise ValueError("Начальное значение не может быть больше конечного")
    for num in range(start, end + 1):
        num_card = str(num).zfill(16)
        yield f"{num_card[:4]} {num_card[4:8]} {num_card[8:12]} {num_card[12:]}"
