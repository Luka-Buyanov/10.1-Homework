import csv
import logging
from typing import Any

import pandas as pd

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("../logs/src.log", "w")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def reader_csv(file_path: str) -> list[Any]:
    """Функция выводящая данные из файла формата .csv. Выводит список словарей с данными."""

    logger.info("Запущена функция вывода данных из .csv")
    data = []
    try:
        with open(file_path, encoding="utf-8") as file:
            logger.info("Открыт файл для чтения")
            reader = csv.DictReader(file, delimiter=";")
            for row in reader:
                if row is not None:
                    data.append(row)
    except FileNotFoundError:
        logger.error("Файл не найден")
        print("Ошибка, файл не найден!")
    logger.info("Завершена функция вывода данных из .csv")
    return data


def reader_excel(file_path: str) -> list[Any]:
    """Функция выводящая данные из файла формата .xlsx. Выводит список словарей с данными."""

    result = []
    logger.info("Запущена функция вывода данных из .xlsx")
    try:
        excel_data = pd.read_excel(file_path)
    except FileNotFoundError:
        logger.error("Файл не найден")
        print("Ошибка, файл не найден!")
    else:
        result = excel_data.to_dict(orient="records")
    logger.info("Завершена функция вывода данных из .xlsx")
    return result
