# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
route_dic = {}
with open("/home/swordsman/Yandex.Disk/repo/python_for_net_engineer/exercises/07_files/ospf.txt") as file_ospf:
    for line in file_ospf:
        line_list = line.strip().split()
        for route in line_list:
            if route and route[0].isdigit() and "/" in route:
                prefix = route
                route_dic[prefix] = {}
            elif route.startswith("["):
                route_dic[prefix]["metric"] = route.strip("[]")
            elif route[0].isdigit() and route[-2].isdigit():
                route_dic[prefix]["nhop"] = route.strip(",")
            elif "d" in route and "h" in route:
                route_dic[prefix]["update"] = route.strip(",")
            elif "Ethernet" in route:
                route_dic[prefix]["interface"] = route
            #print(f"{route_dic}")
        print(f"""
                  Prefix              {prefix}
                  AD/Metric           {route_dic[prefix]['metric']}
                  Next-Hop            {route_dic[prefix]['nhop']}
                  Last update         {route_dic[prefix]['update']}
                  Outbound Interface  {route_dic[prefix]['interface']}
                  """)