import csv
from typing import Any

import pandas as pd


def reader_csv(file_path: str) -> list[Any]:
    """Функция выводящая данные из файла формата .csv. Выводит список словарей с данными."""

    data = []
    with open(file_path, encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            if row is not None:
                data.append(row)
    return data


def reader_excel(file_path: str) -> list[Any]:
    """Функция выводящая данные из файла формата .xlsx. Выводит список словарей с данными."""

    excel_data = pd.read_excel(file_path)
    result = excel_data.to_dict(orient="records")
    return result
