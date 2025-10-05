import pytest
from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "account_number, expected", [(73654108430135874305, "**4305"), (73654108430135871705, "**1705")]
)
def test_get_mask_account_valid(account_number: int, expected: str) -> None:
    assert get_mask_account(account_number) == expected


@pytest.mark.parametrize("invalid_input", ["", "1", "12", "123"])
def test_get_mask_account_invalid(invalid_input: str) -> None:
    assert get_mask_account(invalid_input)


@pytest.mark.parametrize("card_number, expected", [(1234567891011213, "1234 56 ** **** 1213")])
def test_get_mask_card_number_valid(card_number: int, expected: str) -> None:
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize("invalid_input", ["1234", ""])
def test_get_mask_card_number_invalid(invalid_input: str) -> None:
    assert get_mask_card_number(invalid_input)
