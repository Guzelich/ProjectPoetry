import pytest


@pytest.fixture
def transactions():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2025-10-05T15:30:45.123456"},
        {"id": 2, "state": "CANCELED", "date": "2025-10-04T09:15:30.654321"},
        {"id": 3, "state": "PENDING", "date": "2025-10-06T06:00:00.000000"},
        {"id": 4, "state": "", "date": "2025-10-03T03:00:00.000000"},
    ]
