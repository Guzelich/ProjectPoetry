from typing import Iterator


def filter_by_currency(transactions: list, currency: str) -> Iterator:
    for transaction in transactions:
        if(
            isinstance(transaction, dict)
            and transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency
        ):
            yield transaction
