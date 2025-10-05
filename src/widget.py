from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(info_card: str) -> str:
    """Функция обрабатывает информацию и о картах, и о счетах, возвращает замаскированный номер"""
    info_card = info_card.strip()
    parts = info_card.split()

    if len(parts) < 2:
        return "Некорректный ввод"

    number = parts[-1]
    name = " ".join(parts[:-1])

    if name == "Счет":
        result = get_mask_account(number)
    else:
        result = get_mask_card_number(number)
    return f"{name} {result}"


def get_date(date_incorrect: str) -> str:
    """Функция возвращает строку с датой в формате "ДД.ММ.ГГГГ"""
    date_correct = f"{date_incorrect[8:10]}.{date_incorrect[5:7]}.{date_incorrect[0:4]}"
    return date_correct
