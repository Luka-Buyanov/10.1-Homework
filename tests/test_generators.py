import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.mark.parametrize(
    "transactions, currency, filter_transactions",
    (
        (
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                },
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                },
                {
                    "id": 873106923,
                    "state": "EXECUTED",
                    "date": "2019-03-23T01:09:46.296404",
                    "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 44812258784861134719",
                    "to": "Счет 74489636417521191160",
                },
                {
                    "id": 895315941,
                    "state": "EXECUTED",
                    "date": "2018-08-19T04:27:37.904916",
                    "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод с карты на карту",
                    "from": "Visa Classic 6831982476737658",
                    "to": "Visa Platinum 8990922113665229",
                },
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                    "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод организации",
                    "from": "Visa Platinum 1246377376343588",
                    "to": "Счет 14211924144426031657",
                },
            ],
            "USD",
            [
                {
                    "date": "2018-06-30T02:08:58.425572",
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "id": 939719570,
                    "operationAmount": {"amount": "9824.07", "currency": {"code": "USD", "name": "USD"}},
                    "state": "EXECUTED",
                    "to": "Счет 11776614605963066702",
                },
                {
                    "date": "2019-04-04T23:20:05.206878",
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "id": 142264268,
                    "operationAmount": {"amount": "79114.93", "currency": {"code": "USD", "name": "USD"}},
                    "state": "EXECUTED",
                    "to": "Счет 75651667383060284188",
                },
                {
                    "date": "2018-08-19T04:27:37.904916",
                    "description": "Перевод с карты на карту",
                    "from": "Visa Classic 6831982476737658",
                    "id": 895315941,
                    "operationAmount": {"amount": "56883.54", "currency": {"code": "USD", "name": "USD"}},
                    "state": "EXECUTED",
                    "to": "Visa Platinum 8990922113665229",
                },
                "Нет операций",
            ],
        ),
        (
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                },
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                },
                {
                    "id": 873106923,
                    "state": "EXECUTED",
                    "date": "2019-03-23T01:09:46.296404",
                    "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 44812258784861134719",
                    "to": "Счет 74489636417521191160",
                },
                {
                    "id": 895315941,
                    "state": "EXECUTED",
                    "date": "2018-08-19T04:27:37.904916",
                    "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод с карты на карту",
                    "from": "Visa Classic 6831982476737658",
                    "to": "Visa Platinum 8990922113665229",
                },
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                    "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод организации",
                    "from": "Visa Platinum 1246377376343588",
                    "to": "Счет 14211924144426031657",
                },
            ],
            "RUB",
            [
                {
                    "date": "2019-03-23T01:09:46.296404",
                    "description": "Перевод со счета на счет",
                    "from": "Счет 44812258784861134719",
                    "id": 873106923,
                    "operationAmount": {"amount": "43318.34", "currency": {"code": "RUB", "name": "руб."}},
                    "state": "EXECUTED",
                    "to": "Счет 74489636417521191160",
                },
                {
                    "date": "2018-09-12T21:27:25.241689",
                    "description": "Перевод организации",
                    "from": "Visa Platinum 1246377376343588",
                    "id": 594226727,
                    "operationAmount": {"amount": "67314.70", "currency": {"code": "RUB", "name": "руб."}},
                    "state": "CANCELED",
                    "to": "Счет 14211924144426031657",
                },
                "Нет операций",
                "Нет операций",
            ],
        ),
        (
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                },
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                },
                {
                    "id": 873106923,
                    "state": "EXECUTED",
                    "date": "2019-03-23T01:09:46.296404",
                    "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 44812258784861134719",
                    "to": "Счет 74489636417521191160",
                },
                {
                    "id": 895315941,
                    "state": "EXECUTED",
                    "date": "2018-08-19T04:27:37.904916",
                    "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод с карты на карту",
                    "from": "Visa Classic 6831982476737658",
                    "to": "Visa Platinum 8990922113665229",
                },
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                    "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод организации",
                    "from": "Visa Platinum 1246377376343588",
                    "to": "Счет 14211924144426031657",
                },
            ],
            "BANANAS",
            [],
        ),
        ([], "USD", []),
    ),
)
def test_filter_by_currency(transactions: list[dict], currency: str, filter_transactions: list[dict]) -> None:
    """Функция проверяющая корректность работы функции 'filter_by_currency', при работе с различными вводными данными,
    включая пустые строки и отсутствие подходящих операций"""

    result = []
    usd_transactions = filter_by_currency(transactions, currency)
    count = sum(1 for x in usd_transactions)
    for i in range(count):
        result.append(next(usd_transactions))
    assert result == filter_transactions


def test_transaction_descriptions(test_transaction_description: list[dict]) -> None:
    """Функция проверяющая корректность работы функции 'transaction_descriptions'"""

    result = []
    list_descriptions = transaction_descriptions(test_transaction_description)
    for i in range(6):
        result.append(next(list_descriptions))
    assert result == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
        "Нет операций",
    ]


def test_none_transaction_descriptions(test_none_transaction_description: list[dict]) -> None:
    """Функция проверяющая корректность работы функции 'transaction_descriptions' при пустом списке"""

    result = []
    list_descriptions = transaction_descriptions(test_none_transaction_description)
    for i in range(2):
        result.append(next(list_descriptions))
    assert result == ["Нет операций", "Нет операций"]


@pytest.mark.parametrize(
    "start_number, end_number, expected_result",
    (
        (
            1,
            20,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
                "0000 0000 0000 0006",
                "0000 0000 0000 0007",
                "0000 0000 0000 0008",
                "0000 0000 0000 0009",
                "0000 0000 0000 0010",
                "0000 0000 0000 0011",
                "0000 0000 0000 0012",
                "0000 0000 0000 0013",
                "0000 0000 0000 0014",
                "0000 0000 0000 0015",
                "0000 0000 0000 0016",
                "0000 0000 0000 0017",
                "0000 0000 0000 0018",
                "0000 0000 0000 0019",
                "0000 0000 0000 0020",
            ],
        ),
        (
            2000,
            2020,
            [
                "0000 0000 0000 2000",
                "0000 0000 0000 2001",
                "0000 0000 0000 2002",
                "0000 0000 0000 2003",
                "0000 0000 0000 2004",
                "0000 0000 0000 2005",
                "0000 0000 0000 2006",
                "0000 0000 0000 2007",
                "0000 0000 0000 2008",
                "0000 0000 0000 2009",
                "0000 0000 0000 2010",
                "0000 0000 0000 2011",
                "0000 0000 0000 2012",
                "0000 0000 0000 2013",
                "0000 0000 0000 2014",
                "0000 0000 0000 2015",
                "0000 0000 0000 2016",
                "0000 0000 0000 2017",
                "0000 0000 0000 2018",
                "0000 0000 0000 2019",
            ],
        ),
        (
            2000000,
            2000020,
            [
                "0000 0000 0200 0000",
                "0000 0000 0200 0001",
                "0000 0000 0200 0002",
                "0000 0000 0200 0003",
                "0000 0000 0200 0004",
                "0000 0000 0200 0005",
                "0000 0000 0200 0006",
                "0000 0000 0200 0007",
                "0000 0000 0200 0008",
                "0000 0000 0200 0009",
                "0000 0000 0200 0010",
                "0000 0000 0200 0011",
                "0000 0000 0200 0012",
                "0000 0000 0200 0013",
                "0000 0000 0200 0014",
                "0000 0000 0200 0015",
                "0000 0000 0200 0016",
                "0000 0000 0200 0017",
                "0000 0000 0200 0018",
                "0000 0000 0200 0019",
            ],
        ),
        (
            20000000000000,
            20000000000020,
            [
                "0020 0000 0000 0000",
                "0020 0000 0000 0001",
                "0020 0000 0000 0002",
                "0020 0000 0000 0003",
                "0020 0000 0000 0004",
                "0020 0000 0000 0005",
                "0020 0000 0000 0006",
                "0020 0000 0000 0007",
                "0020 0000 0000 0008",
                "0020 0000 0000 0009",
                "0020 0000 0000 0010",
                "0020 0000 0000 0011",
                "0020 0000 0000 0012",
                "0020 0000 0000 0013",
                "0020 0000 0000 0014",
                "0020 0000 0000 0015",
                "0020 0000 0000 0016",
                "0020 0000 0000 0017",
                "0020 0000 0000 0018",
                "0020 0000 0000 0019",
            ],
        ),
    ),
)
def test_card_number_generator(start_number: int, end_number: int, expected_result: list[int]) -> None:

    result = []
    list_numbers = card_number_generator(start_number, end_number)
    for i in range(20):
        result.append(next(list_numbers))
    assert result == expected_result
