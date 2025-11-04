from locale import currency

import pytest


@pytest.fixture
def transactions() -> list:
    return [
        {"id": 1, "state": "EXECUTED", "date": "2025-10-05T15:30:45.123456"},
        {"id": 2, "state": "CANCELED", "date": "2025-10-04T09:15:30.654321"},
        {"id": 3, "state": "PENDING", "date": "2025-10-06T06:00:00.000000"},
        {"id": 4, "state": "", "date": "2025-10-03T03:00:00.000000"},
    ]


@pytest.fixture
def usd_transactions() -> list:
    return [
    {
        "id": 41428829,
        "operationAmount": {
            "amount": "1000",
            "currency": {
                "code": "USD"
            }
        },
        "description": "Перевод организации"
    },
    {
        "id": 939719570,
        "operationAmount": {
            "amount": "150",
            "currency": {
                "code": "USD"
            }
        },
        "description": "Перевод со счета на счет"
    },
    {
        "id": 594226727,
        "operationAmount": {
            "amount": "1500",
            "currency": {
                "code": "RUB"
            }
        },
        "description": "Перевод организации"
    },
    {
        "id": 615064591,
        "operationAmount": {
            "amount": "500",
            "currency": {
                "code": " "
            }
        },
        "description": "Перевод с карты на карту"
    }
]
