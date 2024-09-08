import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_correct_masks_card(test_mask_card: int) -> None:
    """Функция проверяющая корректность маскировки номера карты"""

    assert get_mask_card_number(test_mask_card) == "7777 88** **** 9999"


def test_no_number_string(no_number_string: int) -> None:
    """Функция проверяющая работу со строкой не только из цифр"""

    assert get_mask_card_number(no_number_string) == "aoao 09** **** gggg"


def test_correct_masks_account(test_mask_account: int) -> None:
    """Функция проверяющая корректность маскировки номера аккаунта"""

    assert get_mask_account(test_mask_account) == "**4305"


@pytest.mark.parametrize(
    "no_mask, mask", [(37494638594635448621, "**8621"), (1234567, "**4567"), ("banandddd", "**dddd")]
)
def test_correct_masks_no_standard_account(no_mask: int, mask: str) -> None:
    """Функция проверяющая работу функции с различными размерами и форматами номера аккаунта"""

    assert get_mask_account(no_mask) == mask
