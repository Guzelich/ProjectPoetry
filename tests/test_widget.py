import pytest
from src.widget import mask_account_card, get_date


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("MasterCard 9876543210987654", "MasterCard 9876 54** **** 7654"),
        ("Счет 12345678901234567890", "Счет **7890"),
        ("Счет 9876543210", "Счет **3210"),
    ],
)
def test_mask_account_card_valid(input_str: str, expected: str) -> None:
    assert mask_account_card(input_str) == expected


@pytest.mark.parametrize("invalid_input_str", ["", "Visa 123", "Счет 123", "Счет abc", "Счет 12345 67890"])
def test_mask_account_card_invalid(invalid_input_str: str) -> None:
    mask_account_card(invalid_input_str)


@pytest.mark.parametrize(
    "iso_date, expected",
    [
        ("2023-12-31T15:30:00", "31.12.2023"),
        ("2024-02-29T00:00:00", "29.02.2024"),
        ("2023-05-07T10:00:00", "07.05.2023"),
        ("2000-01-01T00:00:00", "01.01.2000"),
    ],
)
def test_get_date_valid(iso_date: str, expected: str) -> None:
    assert get_date(iso_date) == expected


@pytest.mark.parametrize("invalid_date", ["2023-1-1", "2023/12/31", "short", "", "2023-12"])
def test_get_date_invalid(invalid_date: str) -> None:
    get_date(invalid_date)
