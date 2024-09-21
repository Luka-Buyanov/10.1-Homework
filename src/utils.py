import json


def transaction_data(path: str) -> list[dict]:
    try:
        with open(path, encoding="utf8") as file:
            data = json.load(file)
    except FileNotFoundError:
        list_transaction: list = []
    else:
        if type(data) is not list:
            list_transaction = []
        else:
            list_transaction = data

    return list_transaction
