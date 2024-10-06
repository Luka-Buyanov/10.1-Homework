from typing import Any

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_: str) -> str:
    """Маскирует звёздочками номер карты или счёта"""

    card_name_ = ""
    card_number_ = ""
    for i in range(len(card_)):
        if card_[i].isdigit():
            card_number_ += card_[i]
        else:
            card_name_ += card_[i]
    card_number = int(card_number_)

    if "Счет " in card_name_:
        mask_number = get_mask_account(card_number)
    else:
        mask_number = get_mask_card_number(card_number)

    return card_name_ + mask_number


def get_date(input_date_: Any) -> Any:
    """Преобразует дату в привычный формат"""

    year = input_date_[0:4]
    month = input_date_[5:7]
    day = input_date_[8:10]
    output_date_ = day + "." + month + "." + year

    return output_date_
