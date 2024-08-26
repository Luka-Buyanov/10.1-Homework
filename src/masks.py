def get_mask_card_number(card_number_: int) -> str:
    """Функция маскирующая номер карты звёздочками"""

    masked_card_ = ""
    card_number = str(card_number_)
    for i in range(len(card_number)):
        if i == 4 or i == 8 or i == 12:
            masked_card_ += " "
        if i < 6:
            masked_card_ += card_number[i]
        elif 5 < i < 12:
            masked_card_ += "*"
        elif i > 11:
            masked_card_ += card_number[i]
    return masked_card_


def get_mask_account(account_number_: int) -> str:
    """Функция маскирующая номер аккаунтра звёзочками"""

    masked_account_ = ""
    account_number = str(account_number_)
    for i in range(-6, 0):
        if i < -4:
            masked_account_ += "*"
        elif i < 0:
            masked_account_ += account_number[i]
    return masked_account_
