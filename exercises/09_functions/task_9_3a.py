# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию: добавить поддержку конфигурации, когда настройка access-порта
выглядит так:
    interface FastEthernet0/20
        switchport mode access
        duplex auto

То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
Пример словаря:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt

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
    interface_name = None
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
                elif words[0] == 'switchport' and words[1] == 'mode' and words[2] == 'access':
                    # Сохраняем информацию об интерфейсе доступа
                    access_interfaces[interface_name] = 0
                elif not interface_name == None and access_interfaces.get(interface_name) == 0:                 
                    if  words[0] == 'switchport' and words[1] == 'access' and words[2] == 'vlan':
                        access_interfaces[interface_name] = int(words[3])
                    else: 
                        access_interfaces[interface_name] = 1
    final_tuple=(access_interfaces, trunk_interfaces)
    return final_tuple
# Выводим результаты
config_name = "/home/glucotvorec/Yandex.Disk/repo/python_for_net_engineer/exercises/09_functions/config_sw2.txt"
int_vlan_map = get_int_vlan_map(config_name)
print(f"{int_vlan_map}")