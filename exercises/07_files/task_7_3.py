# -*- coding: utf-8 -*-
"""
Задание 7.3

Скрипт должен обрабатывать записи в файле CAM_table.txt. Каждая строка,
где есть MAC-адрес, должна быть обработана таким образом, чтобы
на стандартный поток вывода была выведена таблица вида:

100      01bb.c580.7000      Gi0/1
200      0a4b.c380.7c00      Gi0/2
300      a2ab.c5a0.700e      Gi0/3
10       0a1b.1c80.7000      Gi0/4
500      02b1.3c80.7b00      Gi0/5
200      1a4b.c580.7000      Gi0/6
300      0a1b.5c80.70f0      Gi0/7
10       01ab.c5d0.70d0      Gi0/8
1000     0a4b.c380.7d00      Gi0/9


Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
cam_dic = {}
with open("/home/swordsman/Yandex.Disk/repo/python_for_net_engineer/exercises/07_files/CAM_table.txt") as file_cam:
    for line in file_cam:
        line_list = line.strip(" ").split()
        for cam in line_list:
            if  cam[0].isdigit() and not "." in cam:
                cam_dic['vlan'] = cam
            elif "." in cam:
                cam_dic['mac'] = cam
            elif 'Gi' in cam:
                cam_dic['interface'] = cam
            else:
                continue
        if cam_dic:
            print(f'{cam_dic["vlan"]:8} {cam_dic["mac"]} {cam_dic["interface"]:>10}')