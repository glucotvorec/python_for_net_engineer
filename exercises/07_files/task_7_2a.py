# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт: Скрипт не должен выводить на стандартрый поток вывода команды,
в которых содержатся слова из списка ignore.

При этом скрипт также не должен выводить строки, которые начинаются на !.

Проверить работу скрипта на конфигурационном файле config_sw1.txt.
Имя файла передается как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "configuration"]
with open("/home/swordsman/Yandex.Disk/repo/python_for_net_engineer/exercises/07_files/config_sw1.txt") as config:
    for line in config:
        if line == None or line[0] == "!":
            continue
        else:
            for word in ignore:
                if word in line:
                    break
            else:
                line = line.strip("\n")
                print(f"{line}")