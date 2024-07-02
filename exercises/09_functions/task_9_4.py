# -*- coding: utf-8 -*-
"""
Задание 9.4

Создать функцию convert_config_to_dict, которая обрабатывает конфигурационный
файл коммутатора и возвращает словарь:
* Все команды верхнего уровня (глобального режима конфигурации), будут ключами.
* Если у команды верхнего уровня есть подкоманды, они должны быть в значении
  у соответствующего ключа, в виде списка (пробелы в начале строки надо удалить).
* Если у команды верхнего уровня нет подкоманд, то значение будет пустым списком

У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

При обработке конфигурационного файла, надо игнорировать строки, которые начинаются
с '!', а также строки в которых содержатся слова из списка ignore.

Для проверки надо ли игнорировать строку, использовать функцию ignore_command.

Часть словаря, который должна возвращать функция (полный вывод можно посмотреть
в тесте test_task_9_4.py):
{
    "version 15.0": [],
    "service timestamps debug datetime msec": [],
    "service timestamps log datetime msec": [],
    "no service password-encryption": [],
    "hostname sw1": [],
    "interface FastEthernet0/0": [
        "switchport mode access",
        "switchport access vlan 10",
    ],
    "interface FastEthernet0/1": [
        "switchport trunk encapsulation dot1q",
        "switchport trunk allowed vlan 100,200",
        "switchport mode trunk",
    ],
    "interface FastEthernet0/2": [
        "switchport mode access",
        "switchport access vlan 20",
    ],
}

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ignore = ["duplex", "alias", "configuration"]


def ignore_command(command, ignore):
    """
    Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает
    * True, если в команде содержится слово из списка ignore
    * False - если нет
    """
    ignore_status = False
    for word in ignore:
        if word in command:
            ignore_status = True
    return ignore_status
    

def convert_config_to_dict(config_filename):
    """
    Функция преобразует файл конфигурации с оборудования cisco в словарь
    все команды верхнего уровня принимаются как ключи словоря, вложенные команды 
    становятся элементами списка"""
    config_dic = {}
    up_command = None
    with open(config_filename) as cisco_config_file:
    # Перебираем строки конфигурации
        for line in cisco_config_file:
            if not line.startswith('!') and line.isalnum and not ignore_command(line, ignore):
                #print(f"{line = }")
                if not line.startswith(" ") and not line == "\n":
                    up_command = line.strip()
                    config_dic[up_command] = []
                elif not line == "\n":
                    config_dic[up_command].append(line.strip())
                else:
                    continue
    return config_dic
                   
config_name = "/home/swordsman/Yandex.Disk/repo/python_for_net_engineer/exercises/09_functions/config_sw1.txt"
configuration = convert_config_to_dict(config_name)
for up, sub in configuration.items():
    print(fr"{up}:{sub}")    