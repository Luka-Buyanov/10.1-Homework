import os
from datetime import datetime
from typing import Any

from src.decorators import log


def test_none_date(capsys: Any) -> None:
    """Функция проверяющая работу в ситуации отсутствия даты и ошибки"""

    @log()
    def my_function(x: int, y: int) -> int:
        return x + y

    my_function(1, 2)
    captured = capsys.readouterr()
    start_time: datetime = datetime.now().replace(microsecond=0)
    end_time: datetime = datetime.now().replace(microsecond=0)

    assert (
        captured.out
        == f"""File name: my_function, Ok, Result = 3
Start time: {start_time}, End time: {end_time}, Work time: 0:00:00\n"""
    )


def test_get_date(capsys: Any) -> None:
    """Функция проверяющая работу в ситуации наличия даты и без ошибки"""

    @log(filename="mylog.txt")
    def my_function(x: int, y: int) -> int:
        return x + y

    start_time: datetime = datetime.now().replace(microsecond=0)
    end_time: datetime = datetime.now().replace(microsecond=0)
    my_function(1, 2)
    logs = open("..\\logs\\mylog.txt", "r")
    file_contents = logs.read()
    logs.close()
    os.remove("..\\logs\\mylog.txt")
    assert (
        f"""File name: my_function, Ok, Result = 3
Start time: {start_time}, End time: {end_time}, Work time: 0:00:00"""
        in file_contents
    )


def test_none_date_error(capsys: Any) -> None:
    """Функция проверяющая работу в ситуации отсутствия даты, но наличии ошибки"""

    @log()
    def my_function(x: int, y: int) -> int:
        return x + y

    my_function(1, "2")
    captured = capsys.readouterr()
    start_time: datetime = datetime.now().replace(microsecond=0)
    end_time: datetime = datetime.now().replace(microsecond=0)

    assert (
        captured.out
        == f"""File name: my_function, Error: TypeError, Why error: unsupported operand type(s) for +: 'int' and 'str'
Inputs: (1, '2'), Start time: {start_time}, End time: {end_time}, Work time: 0:00:00\n"""
    )


def test_get_date_error(capsys: Any) -> None:
    """Функция проверяющая работу в ситуации наличия названия файла и ошибки"""

    @log(filename="mylog.txt")
    def my_function(x: int, y: int) -> int:
        return x + y

    start_time: datetime = datetime.now().replace(microsecond=0)
    end_time: datetime = datetime.now().replace(microsecond=0)
    my_function(1, "2")
    logs = open("..\\logs\\mylog.txt", "r")
    file_contents = logs.read()
    logs.close()
    os.remove("..\\logs\\mylog.txt")
    assert (
        f"""File name: my_function, Error: TypeError, Why error: unsupported operand type(s) for +: 'int' and 'str'
Inputs: (1, '2'), Start time: {start_time}, End time: {end_time}, Work time: 0:00:00"""
        in file_contents
    )
