import os
from typing import Any

import requests
from dotenv import load_dotenv


def conversion(transaction: dict) -> Any:
    """Функция выводящая сумму транзакций"""

    def converter(summa: str, value: str) -> Any:
        """Подфункция конвертирующая сумму транзакции"""

        load_dotenv()
        api_key = os.getenv("API_KEY")
        convert = requests.get(
            f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&amount={summa}&from={value}",
            headers={"apikey": api_key},
        )
        converted = convert.json()
        data = converted.get("result")
        return data

    amount = transaction["operationAmount"]
    summ = amount["amount"]
    currency = amount["currency"]
    code = currency["code"]
    if code == "RUB":
        summ = float(summ)
        return summ
    else:
        result = converter(summ, code)
        if result is None:
            print("Ошибка!")
        return result
