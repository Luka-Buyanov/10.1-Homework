import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "dictionary, state, result",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "EDITED",
            [],
        ),
    ],
)
def test_correct_state(dictionary: list[dict], state: str, result: list[dict]) -> None:
    """Функция проверяющая корректность сортировки по заданному статусу и случай отсутствия элементов по статусу"""

    assert filter_by_state(dictionary, state) == result


@pytest.mark.parametrize(
    "date_dictionary, reverse, sorted_dictionary",
    (
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            False,
            [
                {"date": "2019-07-03T18:35:29.512364", "id": 41428829, "state": "EXECUTED"},
                {"date": "2018-09-12T21:27:25.241689", "id": 594226727, "state": "CANCELED"},
                {"date": "2018-10-14T08:21:33.419441", "id": 615064591, "state": "CANCELED"},
                {"date": "2018-06-30T02:08:58.425572", "id": 939719570, "state": "EXECUTED"},
            ],
        ),
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            True,
            [
                {"date": "2018-06-30T02:08:58.425572", "id": 939719570, "state": "EXECUTED"},
                {"date": "2018-10-14T08:21:33.419441", "id": 615064591, "state": "CANCELED"},
                {"date": "2018-09-12T21:27:25.241689", "id": 594226727, "state": "CANCELED"},
                {"date": "2019-07-03T18:35:29.512364", "id": 41428829, "state": "EXECUTED"},
            ],
        ),
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            False,
            [
                {"date": "2019-07-03T18:35:29.512364", "id": 41428829, "state": "EXECUTED"},
                {"date": "2019-07-03T18:35:29.512364", "id": 41428829, "state": "EXECUTED"},
                {"date": "2018-09-12T21:27:25.241689", "id": 594226727, "state": "CANCELED"},
                {"date": "2018-09-12T21:27:25.241689", "id": 594226727, "state": "CANCELED"},
                {"date": "2018-10-14T08:21:33.419441", "id": 615064591, "state": "CANCELED"},
                {"date": "2018-10-14T08:21:33.419441", "id": 615064591, "state": "CANCELED"},
                {"date": "2018-06-30T02:08:58.425572", "id": 939719570, "state": "EXECUTED"},
                {"date": "2018-06-30T02:08:58.425572", "id": 939719570, "state": "EXECUTED"},
            ],
        ),
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            True,
            [
                {"date": "2018-06-30T02:08:58.425572", "id": 939719570, "state": "EXECUTED"},
                {"date": "2018-10-14T08:21:33.419441", "id": 615064591, "state": "CANCELED"},
                {"date": "2018-10-14T08:21:33.419441", "id": 615064591, "state": "CANCELED"},
                {"date": "2018-09-12T21:27:25.241689", "id": 594226727, "state": "CANCELED"},
                {"date": "2019-07-03T18:35:29.512364", "id": 41428829, "state": "EXECUTED"},
            ],
        ),
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "коопатлкпоаT18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2090-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-вапвапвапT21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "уацуавыауы14T08:21:33.419441"},
                {"id": 615064591, "state": "CANCELED", "date": "бананчикиT08:21:33.419441"},
            ],
            True,
            [
                {"date": "уацуавыауы14T08:21:33.419441", "id": 615064591, "state": "CANCELED"},
                {"date": "коопатлкпоаT18:35:29.512364", "id": 41428829, "state": "EXECUTED"},
                {"date": "бананчикиT08:21:33.419441", "id": 615064591, "state": "CANCELED"},
                {"date": "2018-вапвапвапT21:27:25.241689", "id": 594226727, "state": "CANCELED"},
                {"date": "2090-06-30T02:08:58.425572", "id": 939719570, "state": "EXECUTED"},
            ],
        ),
    ),
)
def test_correct_sort_by_date(date_dictionary: list[dict], reverse: bool, sorted_dictionary: list[dict]) -> None:
    """Функция проверяющая корректность сортировки по дате и ситуацию нестандартного ввода"""

    assert sort_by_date(date_dictionary, reverse) == sorted_dictionary
