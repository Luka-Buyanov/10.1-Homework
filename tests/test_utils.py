from typing import Any
from unittest.mock import patch

from src.utils import transaction_data


@patch("json.load")
def test_not_list_output(data: Any) -> None:
    """Функция проверяющая вывод при получении данных не в списке"""

    data.return_value = "asskfwhjbfhj"
    assert transaction_data("C:/Users/ciple/PycharmProjects/Homework/data/operations.json") == []


@patch("json.load")
def test_list_output(data: Any) -> None:
    """Функция проверяющая вывод при данных в виде списка"""

    data.return_value = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        },
    ]
    assert transaction_data("C:/Users/ciple/PycharmProjects/Homework/data/operations.json") == [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        },
    ]


def test_file_not_found_output() -> None:
    """Функция проверяющая случай когда файл не найден"""

    assert transaction_data("aaa") == []


@patch("json.load")
def test_null_file_output(data: Any) -> None:
    """Функция проверяющая вывод при пустом файле"""

    data.return_value = ""
    assert transaction_data("C:/Users/ciple/PycharmProjects/Homework/data/operations.json") == []
