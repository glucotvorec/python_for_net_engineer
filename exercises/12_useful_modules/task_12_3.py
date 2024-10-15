# -*- coding: utf-8 -*-
"""
Задание 12.3

Создать функцию print_ip_table, которая отображает таблицу доступных
и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

"""
from tabulate import tabulate
def print_ip_table(reachable,unreachable):
    ip_dict = {}
    ip_dict = {"Reachable": reachable, "Unreachable": unreachable}
    print(tabulate(ip_dict, headers="keys"))

if __name__ == "__main__":
    alive = ["10.10.10.1", "10.10.10.2", "10.10.45.1"]
    dead = ["1.1.1.1", "8.8.8.8", "127.0.0.1"]
    print_ip_table(alive,dead)
