# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

from sys import argv

ignore = ["duplex", "alias", "configuration"]
with open(argv[1]) as config_in, open(argv[2], "a") as config_out:
    for line in config_in:
        if line == None or line[0] == "!":
            continue
        else:
            for word in ignore:
                if word in line:
                    break
            else:
                line = line
                config_out.write(f"{line}")