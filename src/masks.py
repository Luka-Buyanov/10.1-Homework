import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("../logs/src.log", "w")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s: %(message)s" )
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number_: int) -> str:
    """Функция маскирующая номер карты звёздочками"""

    logger.info("Запущена функция маскировки номера карты")
    if type(card_number_) is int and len(str(card_number_)) == 16:
        logger.info("Переданы корректные данные")
    elif type(card_number_) is int and len(str(card_number_)) != 16:
        logger.error("Передан правильный тип (int), но неправильная длина")
    else:
        logger.error("Переданы некорректные данные")

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
    logger.info("Завершена функция маскировки номера карты")
    return masked_card_


def get_mask_account(account_number_: int) -> str:
    """Функция маскирующая номер аккаунтра звёзочками"""

    logger.info("Запущена функция маскировки номера аккаунта")
    if type(account_number_) is int and len(str(account_number_)) == 20:
        logger.info("Переданы корректные данные")
    elif type(account_number_) is int and len(str(account_number_)) != 20:
        logger.error("Передан правильный тип (int), но неправильная длина")
    else:
        logger.error("Переданы некорректные данные")

    masked_account_ = ""
    account_number = str(account_number_)
    for i in range(-6, 0):
        if i < -4:
            masked_account_ += "*"
        elif i < 0:
            masked_account_ += account_number[i]
    logger.info("Завершена функция маскировки номера аккаунта")
    return masked_account_
