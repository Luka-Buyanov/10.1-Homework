from typing import Any
from unittest.mock import patch

from src.external_api import conversion


@patch("requests.get")
def test_converted_output(converter: Any) -> None:
    """Функция проверяющая работу при необходимости конвертации"""

    converter.return_value.json.return_value = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": 8221.37},
        "info": {"timestamp": 1726988343, "rate": 92.515546},
        "date": "2024-09-22",
        "result": 760604.534418,
    }
    assert (
        conversion(
            {
                "id": 41428829,
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
                "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод организации",
                "from": "MasterCard 7158300734726758",
                "to": "Счет 35383033474447895560",
            }
        )
        == 760604.534418
    )


def test_non_converted_output() -> None:
    """Функция проверяющая работу без необходимости конвертации"""

    assert (
        conversion(
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589",
            }
        )
        == 31957.58
    )


def test_wrong_input(capsys: Any) -> None:
    """Функция проверяющая работу при ошибке в переданных данных"""

    assert (
        conversion(
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUS"}},
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589",
            }
        )
        is None
    )
    captured = capsys.readouterr()
    assert captured.out == "Ошибка!\n"
