
def filter_by_state(list_of_dict: list, state: str = 'EXECUTED') -> list:
    """Функция фильтрует список словарей по значению ключа"""
    filtered_list = []
    for dict_item in list_of_dict:
        if dict_item.get('state') == state:
            filtered_list.append(dict_item)
    return filtered_list
