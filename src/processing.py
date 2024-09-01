def filter_by_state(dictionary_: list, state_: str = "EXECUTED") -> list:
    """Функция сортирующая список по критерию 'state'"""

    sorted_dictionary = []
    for element in dictionary_:
        if element["state"] == state_:
            sorted_dictionary.append(element)
        else:
            continue

    return sorted_dictionary
