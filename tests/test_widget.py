import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "no_mask, mask",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_correct_choice(no_mask: str, mask: str) -> None:
    """Функция проверяющая корректность маскировки при различных входных данных"""

    assert mask_account_card(no_mask) == mask


@pytest.mark.parametrize(
    "bad_format, good_format",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2021-08-18T07:29:38.675407", "18.08.2021"),
        ("aoaoaoaoaoaoa", "ao.oa.aoao"),
        ("Счет 35383033474447895560", "83.35.Счет"),
    ],
)
def test_correct_data(bad_format: str, good_format: str) -> None:
    """Функция проверяющая корректность преобразования даты в привычный формат и работу с нестандартным вводом"""

    assert get_date(bad_format) == good_format
