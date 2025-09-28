from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """Функция маскирует номер банковской карты"""
    card_number = str(card_number)
    if len(card_number) == 16:
        masked_number = f"{card_number[:4]} {card_number[4:6]} ** **** {card_number[-4:]}"
        return masked_number
    return "Некорректный ввод"


def get_mask_account(account_number: Union[int, str]) -> str:
    """Функция маскирует аккаунт пользователя"""
    account_number = str(account_number)
    if len(account_number) >= 4:
        masked_account = f"**{account_number[-4:]}"
        return masked_account
    return "Некорректный ввод"
