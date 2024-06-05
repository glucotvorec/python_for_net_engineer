# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
cam_dic = {}
while True:
    vlan_num = input("Enter VLAN number: ")
    #validation of entered values
    try:
        if not vlan_num.isalnum() or int(vlan_num) > 4095:
            raise ValueError()
    except (ValueError):
        print("Enters an invalid VLAN number ")
    else:
        break
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
        if cam_dic and cam_dic["vlan"] == vlan_num:
            print(f'{cam_dic["vlan"]:8} {cam_dic["mac"]} {cam_dic["interface"]:>10}')