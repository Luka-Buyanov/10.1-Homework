# Банковский виджет
Это виджет, который показывает несколько последних успешных банковских операций клиента. 
Написан на Python. 
Создаётся в рамках домашнего задания 2 курса "Python - разработчик" от Skypro.

## Содержание
- [Используемые версии](#используемые-версии)
- [Использование](#использование)
- [Тестирование](#тестирование)
- [Сделано](#сделано)
- [To do](#to-do)

## Используемые версии
- python = "3.12"
- black = "24.8.0"
- flake8 = "7.1.1"
- isort = "5.13.2"
- mypy = "1.11.2"

## Использование
Скачать и открыть в pycharm.

## Тестирование
В проекте имеются инструменты для проверки:
- black
- isort
- flake 8
- mypy

Для их использования введите команду:

``
(название инструмента) .
``

В проекте проведено множество тестов с различными входными данными.
Для их запуска перейдите в файл с тестом через PyCharm и запустите соответствующий файл.

Проверено:
- Модуль masks
- - Функция  get_mask_card_number :
- - - Тестирование правильности маскирования номера карты.
- - - Проверка, что функция корректно обрабатывает входные строки, где отсутствует номер карты.
- - Функция  get_mask_account :
- - - Тестирование правильности маскирования номера счета. 
- - - Проверка работы функции с различными форматами и длинами номеров счетов.
- - - Проверка, что функция корректно обрабатывает входные строки, где номер счета меньше ожидаемой длины.
- Модуль widget
- - Функция mask_account_card :
- - - Тесты для проверки, что функция корректно распознает и применяет нужный тип маскировки в зависимости от типа входных данных (карта или счет).
- - - Параметризованные тесты с разными типами карт и счетов для проверки универсальности функции.
- - Функция get_data :
- - - Тестирование правильности преобразования даты.
- - - Проверка, что функция корректно обрабатывает входные строки, где отсутствует дата.
- Модуль processing
- - Функция filter_by_state :
- - - Тестирование фильтрации списка словарей по заданному статусу 
state.
- - - Проверка работы функции при отсутствии словарей с указанным статусом 
state в списке.
- - - Параметризация тестов для различных возможных значений статуса
state.
- - Функция sort_by_date :
- - - Тестирование сортировки списка словарей по датам в порядке убывания и возрастания.
- - - Проверка корректности сортировки при одинаковых датах.
- - - Тесты на работу функции с некорректными или нестандартными форматами дат.
- - Функция filter_by_currency:
- - - Тест, что функция корректно фильтрует транзакции по заданной валюте.
- - - Тест, что функция правильно обрабатывает случаи, когда транзакции в заданной валюте отсутствуют.
- - - Тест, что генератор не завершается ошибкой при обработке пустого списка или списка без соответствующих валютных операций.
- - Функция transaction_descriptions:
- - - Тест, что функция возвращает корректные описания для каждой транзакции.
- - - Тест работы функции с различным количеством входных транзакций, включая пустой список.
- - Функция card_number_generator:
- - - Тесты, которые проверяют, что генератор выдает правильные номера карт в заданном диапазоне.
- - - Проверка корректность форматирования номеров карт.

## Сделано
Добавлено несколько функций:

- Функция фильтрующая список операций по заданной валюте: filter_by_currency
- Функция выводящая описание каждой транзакции: transaction_descriptions
- Функция генерирующая номера кард в диапазоне между первым и вторым числом: card_number_generator

## To do
-[x] Создать проект
-[x] Реализовать функции маскировки номеров счёта и карты
-[x] Написать первоначальный README
-[x] Реализовать функции сортировки по дате и состоянию
-[x] Провести тесты при разных входных данных
- [x] Реализовать функции по генерации номеров, сортировке по валюте и выводу информации о транзакции.
- [x] Протестировать реализованные функции.
-[ ] Продолжать работу по поступающим заданиям