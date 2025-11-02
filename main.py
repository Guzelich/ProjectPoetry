from src.masks import get_mask_card_number
from src.masks import get_mask_account


print(get_mask_card_number(7000792289606361))
print(get_mask_account(73654108430135874305))
print(get_mask_account("Счет 73654108430135874305"))
print([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}])
print([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}])


transactions = [
    {
        "id": 41428829,
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
            "amount": "1000",
            "currency": {
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 73654108430135874305",
        "to": "Счет 73654108430153874344"
    },
    {
        "id": 939719570,
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "150",
            "currency": {
                "code": "USD"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 74444301410430583587",
        "to": "Счет 73654108430153874344"
    },
    {
        "id": 594226727,
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {
            "amount": "1500",
            "currency": {
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 57776859947565777595",
        "to": "Счет 55976894775977565775"
    },
    {
        "id": 615064591,
        "date": "2018-10-14T08:21:33.419441",
        "operationAmount": {
            "amount": "500",
            "currency": {
                "code": " "
            }
        },
        "description": "Перевод с карты на карту",
        "from": "Счет 65658486867564868565",
        "to": "Счет 68487556864658568665"
    }
]
