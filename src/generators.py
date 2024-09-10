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


def card_number_generator(start: int, end: int) -> Generator:
    """Функция генерирующая номера кард в диапазоне между первым и вторым числом"""

    while start <= end:
        output_number = ""
        using_number = str(start)
        part_of_zero = ""
        for i in range(16 - len(using_number)):
            part_of_zero += "0"
        using_number_2 = part_of_zero + using_number
        for i in range(16):
            if i == 4 or i == 8 or i == 12:
                output_number += " "
            output_number += using_number_2[i]

        yield output_number
        start += 1
