from datetime import datetime


def filter_by_state(list_of_dict: list, state: str = "EXECUTED") -> list:
    """Функция фильтрует список словарей по заданному по умолчанию значению ключа"""
    filtered_list = []
    for dict_item in list_of_dict:
        if dict_item.get("state") == state:
            filtered_list.append(dict_item)
    return filtered_list


def sort_by_date(data_list: list, data_key="date", descending=True) -> list:
    """Функция сортирует список словарей по дате в заданном по умолчанию порядке сортировки - по убыванию"""
    data_key = datetime.strptime("2023-10-22", "%Y-%m-%d")
    return sorted(data_list, key=lambda x: datetime.strptime(x[data_key], "%Y-%m-%dT%H:%M:%S.%f"), reverse=descending)
