from src.widget import get_date


def filter_by_state(dictionary: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция сортирующая список по критерию 'state'"""

    sorted_dictionary = []
    for element in dictionary:
        if element["state"] == state:
            sorted_dictionary.append(element)

    return sorted_dictionary


def sort_by_date(date_dictionary: list[dict], date: bool = False) -> list[dict]:
    """Функция сортирующая список по дате"""

    def get_formated_date(dictionary: dict) -> str:
        """Подфункция выводящая дату в привычном формате"""

        formated_date = get_date(dictionary["date"])
        return formated_date

    sorted_date = sorted(date_dictionary, key=get_formated_date, reverse=date)
    return sorted_date
