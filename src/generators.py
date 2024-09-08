from typing import Generator


def filter_by_currency(dictionaries_transactions: list[dict], int_currency: str) -> Generator:
    """Функция фильтрующая список операций по заданной валюте"""

    len_input = len(dictionaries_transactions)
    count = 0
    while True:
        if count >= len_input:
            yield "Нет операций"
        else:

            dictionary = dictionaries_transactions[count]
            element_operation_amount = dictionary["operationAmount"]
            element_currency = element_operation_amount["currency"]
            element_code = element_currency["code"]
            element_name = element_currency["name"]

            if element_code == int_currency or element_name == int_currency:
                yield dictionary
        count += 1


def transaction_descriptions(int_transactions: list[dict]) -> Generator:
    """Функция выводящая описание каждой транзакции"""

    len_input = len(int_transactions)
    count = 0
    while True:
        if count >= len_input:
            yield "Нет операций"
        else:
            dictionary = int_transactions[count]
            description = dictionary["description"]
            yield description
        count += 1
