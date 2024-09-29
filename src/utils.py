import json
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("../logs/src.log", "w")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def transaction_data(path: str) -> list[dict]:
    """Функция выводящая список транзакций из файла формата JSON"""

    logger.info("Запущена функция вывода списка транзакций")
    try:
        with open(path, encoding="utf8") as file:
            data = json.load(file)
    except FileNotFoundError:
        logger.error("Файл не найден")
        list_transaction: list = []
    else:
        if type(data) is not list:
            logger.error("Получен некорректный тип данных")
            list_transaction = []
        else:
            logger.info("Получены корректные данные")
            list_transaction = data

    logger.info("Завершена функция вывода списка транзакций")
    return list_transaction
