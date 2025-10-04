import pytest
from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize('account_number, expected', [(73654108430135874305, '**4305'), (73654108430135871705, '**1705')])
def test_get_mask_account_positive(account_number, expected):
    assert get_mask_account(account_number) == expected


@pytest.mark.parametrize('invalid_input', ['', '1', '12', '123'])
def test_get_mask_account_negative(invalid_input):
    assert get_mask_account(invalid_input)


@pytest.mark.parametrize('card_number, expected', [(1234567891011213, '1234 56 ** **** 1213')])
def test_get_mask_card_number_positive(card_number, expected):
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize('invalid_input', ['1234', ''])
def test_get_mask_card_number_negative(invalid_input):
    assert get_mask_card_number(invalid_input)
