from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.reading import reader_csv, reader_excel
from src.searchers import string_search
from src.utils import transaction_data
from src.widget import get_date, mask_account_card


def main() -> None:
    """Функция, выводящая пользовательский интерфейс."""

    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    number = 0
    while number != 4:
        print(
            """
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
4. Выход"""
        )

        i = 0
        while i != 1:
            number = int(input())
            if number >= 5 or number < 1:
                print("Введите число из списка")
            else:
                i += 1
        if number == 4:
            break
        elif number == 1:
            print("Для обработки выбран JSON-файл.")
            data = transaction_data("../data/operations.json")
        elif number == 2:
            print("Для обработки выбран CSV-файл.")
            data = reader_csv("../data/transactions.csv")
        else:
            print("Для обработки выбран XLSX-файл.")
            data = reader_excel("../data/transactions_excel.xlsx")

        if not data:
            print("Файл не найден, попробуйте снова.")
            exit(0)

        status = ""
        i = 0
        while i != 1:
            print(
                """Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"""
            )
            status = str(input())
            status = status.upper()
            if status == "EXECUTED" or status == "CANCELED" or status == "PENDING":
                i += 1
            else:
                print(f"Статус операции {status} недоступен.")

        sorted_data = filter_by_state(data, status)

        answer = str(input("Отсортировать операции по дате? Да/Нет\n"))
        answer = answer.upper()
        if answer == "ДА":
            answer = str(input("Отсортировать по возрастанию или по убыванию?\n"))
            answer = answer.upper()
            if answer == "ПО УБЫВАНИЮ":
                sorted_data = sort_by_date(sorted_data)
            else:
                sorted_data = sort_by_date(sorted_data, True)

        answer = str(input("Выводить только рублевые транзакции? Да/Нет\n"))
        answer = answer.upper()
        if answer == "ДА":
            sorted_data_generator = filter_by_currency(sorted_data, "RUB")
            sorted_data = []
            for item in sorted_data_generator:
                sorted_data.append(item)

        answer = str(input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n"))
        answer = answer.upper()
        if answer == "ДА":
            answer = str(input("Введите слово для поиска:\n"))
            sorted_data = string_search(sorted_data, answer)

        print("Распечатываю итоговый список транзакций...\n\n")
        count = len(sorted_data)
        if count >= 1:
            print(f"Всего операций: {count}\n")
            for operation in sorted_data:
                data = get_date(operation["date"])
                description = operation["description"]
                from_operation = ""
                if "from" in operation:
                    from_operation = mask_account_card(operation["from"])
                to_operation = mask_account_card(operation["to"])
                if "amount" in operation:
                    summ = operation["amount"]
                    code = operation["currency_code"]
                else:
                    operation_amount = operation["operationAmount"]
                    summ = operation_amount["amount"]
                    currency = operation_amount["currency"]
                    code = currency["code"]
                if description == "Открытие вклада":
                    print(
                        f"""{data} {description}
{to_operation}
Сумма: {summ} {code}.
"""
                    )
                else:
                    print(
                        f"""{data} {description}
{from_operation} -> {to_operation}
Сумма: {summ} {code}.
"""
                    )
        else:
            print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")

    print("Goodbye!")
