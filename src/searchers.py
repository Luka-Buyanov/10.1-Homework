import logging
import re
from collections import Counter
from typing import Any

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("../logs/src.log", "w")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def string_search(dictionaries: list[dict], string: str) -> Any:
    """Функция поиска элементов списка по заданному слову"""

    logger.info("Запущена функция поиска по заданному слову")
    pattern = re.compile(f"{string}", flags=re.IGNORECASE)
    result = []
    for dictionary in dictionaries:
        description = dictionary["description"]
        if re.search(pattern, description) is not None:
            result.append(dictionary)

    if result:
        logger.info("Завершена функция поиска по заданному слову")
        return result
    else:
        logger.error("Соответствия не найдены")
        return "Ничего не найдено!"


def counter_categories(list_dictionaries: list[dict], list_categories: list[str]) -> Any:
    """Функция ведущая подсчёт категорий по переданному статусу"""

    logger.info("Запущена функция подсчёта операций по заданным категориям")
    list_state = []
    for dictionary in list_dictionaries:
        state = dictionary["state"]
        list_state.append(state)
        logger.info("Создан список всех категорий операций")
    if list_state:
        result = []
        counted = Counter(list_state)
        for category in list_categories:
            for count_category in counted:
                if count_category == category:
                    result.append(count_category)
        if result:
            logger.info("Завершена функция подсчёта операций по заданным категориям")
            return result
    logger.error("Соответствия не найдены")
    return "Ничего не найдено"
