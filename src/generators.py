from typing import Iterator


def filter_by_currency(transactions: list, currency: str) -> Iterator:
    for transaction in transactions:
        if(
            isinstance(transaction, dict)
            and transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency
        ):
            yield transaction


def transaction_descriptions(transactions):
    descriptions = transaction_descriptions(transactions)
    for _ in range(4):
        print(next(descriptions))


def card_number_generator(start: int, end: int) -> Iterator:
    min_card = 1
    max_card = 9999999999999999
    if start < min_card:
        raise ValueError('Начальное значение не может быть меньше 1')
    if end > max_card:
        raise ValueError('Конечное значение не может быть больше 9999999999999999')
    if start > end:
        raise ValueError('Начальное значение не может быть больше конечного')

    for num in range(start, end + 1):
        num_card = str(num).zfill(16)
        yield f"{num[:4]} {num[4:8]} {num[8:12]} {num[12:]}"
