# -*- coding: utf-8 -*-
"""
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный
файл коммутатора и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов,
  а значения access VLAN (числа):
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов,
  а значения список разрешенных VLAN (список чисел):
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент
имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
def get_int_vlan_map(config_filename):
    """ 
    Функция проходит по файлу конфигурации коммутатора и возвращает 
    кортеж из двух словарей содержащих название интерфейсов и номера vlan 
    к которым относятся интерфейсы"""
    # Словари для хранения транковых и интерфейсов доступа
    trunk_interfaces = {}
    access_interfaces = {}
 
    with open(config_filename) as cisco_config_file:
        # Перебираем строки конфигурации
        for line in cisco_config_file:
            # Удаляем комментарии и пустые строки
            if not line.strip().startswith('!') and line and len(line.split()) >= 2:
                # Разделяем строку на слова
                line = line.strip()
                words = line.split()     
                if words[0] == "interface" and "Ethernet" in words[1]:
                    interface_name = words[1]
                # Проверяем, является ли интерфейс транковым
                elif words[0] == 'switchport' and words[1] == 'trunk' and words[2] == "allowed":
                    # Сохраняем информацию о транковом интерфейсе
                    trunk_interfaces[interface_name] = [int(num) for num in words[4].split(',')]
                # Проверяем, является ли интерфейс доступом
                elif words[0] == 'switchport' and words[1] == 'access' and words[2] == 'vlan':
                    # Сохраняем информацию об интерфейсе доступа
                    access_interfaces[interface_name] = int(words[3])
    final_tuple=(access_interfaces, trunk_interfaces)
    return final_tuple
# Выводим результаты
config_name = "/home/swordsman/Yandex.Disk/repo/python_for_net_engineer/exercises/09_functions/config_sw1.txt"
int_vlan_map = get_int_vlan_map(config_name)
print(f"{int_vlan_map}")