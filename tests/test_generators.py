import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.mark.usefixtures("usd_transactions")
def test_filter_by_currency_usd(usd_transactions: list) -> None:
    result = list(filter_by_currency(usd_transactions, "USD"))
    assert len(result) == 2
    assert result[0]["id"] == 41428829
    assert result[1]["id"] == 939719570


def test_filter_by_currency_rub(usd_transactions: list) -> None:
    result = list(filter_by_currency(usd_transactions, "RUB"))
    assert len(result) == 1
    assert result[0]["id"] == 594226727


def test_filter_by_currency_empty(usd_transactions: list) -> None:
    result = list(filter_by_currency(usd_transactions, " "))
    assert len(result) == 1
    assert result[0]["id"] == 615064591


def test_transaction_descriptions_valid(usd_transactions: list) -> None:
    result = transaction_descriptions(usd_transactions)
    assert next(result) == "Перевод организации"
    assert next(result) == "Перевод со счета на счет"
    assert next(result) == "Перевод организации"
    assert next(result) == "Перевод с карты на карту"


def test_transaction_descriptions_empty(usd_transactions: list) -> None:
    result = transaction_descriptions([])
    with pytest.raises(StopIteration):
        next(result)


def test_card_number_generator_valid() -> None:
    result = card_number_generator(1, 3)
    assert next(result) == "0000 0000 0000 0001"
    assert next(result) == "0000 0000 0000 0002"
    assert next(result) == "0000 0000 0000 0003"
    with pytest.raises(StopIteration):
        next(result)


def test_card_number_generator_correct_formatting() -> None:
    result = card_number_generator(5454620011039772, 5454620011039772)
    assert next(result) == "5454 6200 1103 9772"
    with pytest.raises(StopIteration):
        next(result)


def test_card_number_generator_start_less_than_min() -> None:
    with pytest.raises(ValueError, match="Начальное значение не может быть меньше 1"):
        list(card_number_generator(0, 100))


def test_card_number_generator_end_more_max() -> None:
    with pytest.raises(ValueError, match="Конечное значение не может быть больше 9999999999999999"):
        list(card_number_generator(1, 10000000000000000))


def test_card_number_generator_end_less_start() -> None:
    with pytest.raises(ValueError, match="Начальное значение не может быть больше конечного"):
        list(card_number_generator(2, 1))
