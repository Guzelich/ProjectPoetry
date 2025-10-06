from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """Функция маскирует номер банковской карты"""
    card_num = str(card_number).replace(" ", "")
    if len(card_num) == 16 and card_num.isdigit():
        return f"{card_num[:4]} {card_num[4:6]}** **** {card_num[-4:]}"
    return "Некорректный ввод"


def get_mask_account(account_number: Union[int, str]) -> str:
    """Функция маскирует аккаунт пользователя"""
    account_num = str(account_number).replace(" ", "")
    if account_num.isdigit() and len(account_num) >= 4:
        return f"**{account_num[-4:]}"
    return "Некорректный ввод"
