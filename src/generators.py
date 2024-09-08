from typing import Generator


def filter_by_currency(directions_transactions: list[dict], int_currency: str) -> Generator:
    """Функция фильтрующая список операций по заданной валюте"""

    len_input = len(directions_transactions)
    count = 0
    while True:
        if count >= len_input:
            yield "Нет операций"
        else:

            direction = directions_transactions[count]
            element_operation_amount = direction["operationAmount"]
            element_currency = element_operation_amount["currency"]
            element_code = element_currency["code"]
            element_name = element_currency["name"]

            if element_code == int_currency or element_name == int_currency:
                yield direction
        count += 1
