from typing import Any
from unittest.mock import patch

import pandas as pd

from src.reading import reader_csv, reader_excel


@patch("csv.DictReader")
def test_correct_input_csv(data: Any) -> None:
    """Функция проверяющая работу при корректном вводе."""

    data.return_value = [
        {
            "id": "134341",
            "state": "CANCELED",
            "date": "2022-03-03T08:41:08Z",
            "amount": "13642",
            "currency_name": "Peso",
            "currency_code": "COP",
            "from": "Visa 9770850749183268",
            "to": "American Express 0522499169905654",
            "description": "Перевод с карты на карту",
        },
        {
            "id": "2177828",
            "state": "EXECUTED",
            "date": "2022-04-14T15:14:21Z",
            "amount": "24853",
            "currency_name": "Yuan Renminbi",
            "currency_code": "CNY",
            "from": "Счет 38577962752140632721",
            "to": "Счет 47657753885349826314",
            "description": "Перевод со счета на счет",
        },
        {
            "id": "4137938",
            "state": "EXECUTED",
            "date": "2023-01-04T13:13:34Z",
            "amount": "15560",
            "currency_name": "Real",
            "currency_code": "BRL",
            "from": "",
            "to": "Счет 38164279390569873521",
            "description": "Открытие вклада",
        },
        {
            "id": "4699552",
            "state": "EXECUTED",
            "date": "2022-03-23T08:29:37Z",
            "amount": "23423",
            "currency_name": "Peso",
            "currency_code": "PHP",
            "from": "Discover 7269000803370165",
            "to": "American Express 1963030970727681",
            "description": "Перевод с карты на карту",
        },
    ]
    assert reader_csv("../data/transactions.csv") == [
        {
            "id": "134341",
            "state": "CANCELED",
            "date": "2022-03-03T08:41:08Z",
            "amount": "13642",
            "currency_name": "Peso",
            "currency_code": "COP",
            "from": "Visa 9770850749183268",
            "to": "American Express 0522499169905654",
            "description": "Перевод с карты на карту",
        },
        {
            "id": "2177828",
            "state": "EXECUTED",
            "date": "2022-04-14T15:14:21Z",
            "amount": "24853",
            "currency_name": "Yuan Renminbi",
            "currency_code": "CNY",
            "from": "Счет 38577962752140632721",
            "to": "Счет 47657753885349826314",
            "description": "Перевод со счета на счет",
        },
        {
            "id": "4137938",
            "state": "EXECUTED",
            "date": "2023-01-04T13:13:34Z",
            "amount": "15560",
            "currency_name": "Real",
            "currency_code": "BRL",
            "from": "",
            "to": "Счет 38164279390569873521",
            "description": "Открытие вклада",
        },
        {
            "id": "4699552",
            "state": "EXECUTED",
            "date": "2022-03-23T08:29:37Z",
            "amount": "23423",
            "currency_name": "Peso",
            "currency_code": "PHP",
            "from": "Discover 7269000803370165",
            "to": "American Express 1963030970727681",
            "description": "Перевод с карты на карту",
        },
    ]


def test_incorrect_input_csv(capsys: Any) -> None:
    """Функция проверяющая работу при подаче неверного пути к файлу."""

    assert reader_csv("../data/aoaoao") == []
    captured = capsys.readouterr()
    assert captured.out == "Ошибка, файл не найден!\n"


@patch("csv.DictReader")
def test_null_input_csv(data: Any) -> None:
    """Функция проверяющая работу при пустом файле."""

    data.return_value = []
    assert reader_csv("../data/transactions.csv") == []


@patch("pandas.read_excel")
def test_correct_input_xlsx(data: Any) -> None:
    """Функция проверяющая работу при корректном вводе."""

    data.return_value = pd.DataFrame(
        [
            {
                "id": 650703.0,
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                "amount": 16210.0,
                "currency_name": "Sol",
                "currency_code": "PEN",
                "from": "Счет 58803664561298323391",
                "to": "Счет 39745660563456619397",
                "description": "Перевод организации",
            },
            {
                "id": 3598919.0,
                "state": "EXECUTED",
                "date": "2020-12-06T23:00:58Z",
                "amount": 29740.0,
                "currency_name": "Peso",
                "currency_code": "COP",
                "from": "Discover 3172601889670065",
                "to": "Discover 0720428384694643",
                "description": "Перевод с карты на карту",
            },
            {
                "id": 593027.0,
                "state": "CANCELED",
                "date": "2023-07-22T05:02:01Z",
                "amount": 30368.0,
                "currency_name": "Shilling",
                "currency_code": "TZS",
                "from": "Visa 1959232722494097",
                "to": "Visa 6804119550473710",
                "description": "Перевод с карты на карту",
            },
        ]
    )

    assert reader_excel("../data/transactions_excel.xlsx") == [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        },
        {
            "id": 3598919.0,
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "amount": 29740.0,
            "currency_name": "Peso",
            "currency_code": "COP",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
            "description": "Перевод с карты на карту",
        },
        {
            "id": 593027.0,
            "state": "CANCELED",
            "date": "2023-07-22T05:02:01Z",
            "amount": 30368.0,
            "currency_name": "Shilling",
            "currency_code": "TZS",
            "from": "Visa 1959232722494097",
            "to": "Visa 6804119550473710",
            "description": "Перевод с карты на карту",
        },
    ]


def test_incorrect_input_xlsx(capsys: Any) -> None:
    """Функция проверяющая работу при подаче неверного пути к файлу."""

    assert reader_excel("../data/aoaoao") == []
    captured = capsys.readouterr()
    assert captured.out == "Ошибка, файл не найден!\n"


@patch("pandas.read_excel")
def test_null_input_xlsx(data: Any) -> None:
    """Функция проверяющая работу при пустом файле."""

    data.return_value = pd.DataFrame([])
    assert reader_excel("../data/transactions.xlsx") == []
