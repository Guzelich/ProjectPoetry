import pytest
from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "state, expected",
    [("EXECUTED", [1]), ("CANCELED", [2]), ("PENDING", [3]), ("", [4])],
    ids=["executed", "canceled", "pending", "empty"],
)
def test_filter_by_state_valid(transactions: list[dict], state: str, expected: list[int]) -> None:
    result = filter_by_state(transactions, state=state)
    result_ids = [item["id"] for item in result]
    assert result_ids == expected


def test_filter_by_state_custom(transactions: list[dict]) -> None:
    result = filter_by_state(transactions, "CANCELED")
    assert len(result) == 1
    assert result[0]["state"] == "CANCELED"
    assert result[0]["id"] == 2


def test_filter_by_state_empty_input() -> None:
    result = filter_by_state([])
    assert result == []


def test_sort_by_date_descending(transactions: list[dict]) -> None:
    result = sort_by_date(transactions)
    expected_order = [3, 1, 2, 4]
    assert [item["id"] for item in result] == expected_order


def test_sort_by_date_ascending(transactions: list[dict]) -> None:
    result = sort_by_date(transactions, descending=False)
    expected_order = [4, 2, 1, 3]
    assert [item["id"] for item in result] == expected_order


def test_sort_by_date_empty_list() -> None:
    result = sort_by_date([])
    assert result == []


def test_sort_by_date_invalid_date_format() -> None:
    invalid_data = [{"date": "invalid-date-format"}]
    with pytest.raises(ValueError):
        sort_by_date(invalid_data)


def test_sort_by_date_missing_date_key() -> None:
    invalid_data = [{"state": "EXECUTED"}]
    with pytest.raises(KeyError):
        sort_by_date(invalid_data)
