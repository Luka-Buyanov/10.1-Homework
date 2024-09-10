from datetime import datetime, timedelta
from typing import Any


def log(filename: Any = None) -> Any:
    """Функция декоратор вызывающая функции для записи результатов работы функции"""

    def decorator(func: Any) -> Any:
        """Подфункция декоратора, использующая функцию под декоратором"""

        def checking(*args: Any, **kwargs: Any) -> None:
            """Подфункция декоратора, вычисляет время работы функции, выводит результаты в лог-файл"""

            log_info = ""
            start_time: datetime = datetime.now()
            work_time: timedelta = datetime.now() - datetime.now()
            try:
                result = func(*args, **kwargs)
            except Exception as error:
                end_time: datetime = datetime.now()
                work_time = end_time - start_time
                log_info = f"""File name: {func.__name__}, Error: {error.__class__.__name__}, Why error: {error}
Inputs: {*args, *kwargs}, Start time: {start_time}, End time: {end_time}, Work time: {work_time}"""
            else:
                end_time = datetime.now()
                work_time = end_time - start_time
                log_info = f"""File name: {func.__name__}, Ok, Result = {result}
Start time: {start_time}, End time: {end_time}, Work time: {work_time}"""
            finally:
                if filename is None:
                    print(log_info)
                else:
                    file = open(f"..\\logs\\{filename}", "w")
                    file.write(log_info)
                    file.close()

        return checking

    return decorator
