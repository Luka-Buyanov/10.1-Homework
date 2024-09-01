from src.widget import get_date


def filter_by_state(dictionary_: list, state_: str = "EXECUTED") -> list:
    """Функция сортирующая список по критерию 'state'"""

    sorted_dictionary = []
    for element in dictionary_:
        if element["state"] == state_:
            sorted_dictionary.append(element)
        else:
            continue

    return sorted_dictionary


def sort_by_date(date_dictionary_: list, date_: bool = False) -> list:
    """Функция сортирующая список по дате"""

    def get_date_(dictionary: dict) -> str:
        """Подфункция выводящая дату в привычном формате"""

        good_date = get_date(dictionary["date"])
        return good_date

    sorted_date = sorted(date_dictionary_, key=get_date_, reverse=date_)
    return sorted_date
