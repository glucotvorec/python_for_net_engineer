# -*- coding: utf-8 -*-
"""
Задание 12.2


Функция ping_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона,
например, 192.168.100.1-10.

В этом задании необходимо создать функцию convert_ranges_to_ip_list,
которая конвертирует список IP-адресов в разных форматах в список,
где каждый IP-адрес указан отдельно.

Функция ожидает как аргумент список, в котором содержатся IP-адреса
и/или диапазоны IP-адресов.

Элементы списка могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо развернуть диапазон в отдельные
адреса, включая последний адрес диапазона.
Для упрощения задачи, можно считать, что в диапазоне всегда меняется только
последний октет адреса.

Функция возвращает список IP-адресов.

Например, если передать функции convert_ranges_to_ip_list такой список:
['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']

Функция должна вернуть такой список:
['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128',
 '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']

"""
import ipaddress
def ip_address_sequence_calculator(ip_low,dec_range):
    """
    The function takes the starting address and the decimal value of the address difference,
     returns a list of sequential addresses 
    """
    i = 0
    address_range = []
    while i < int(dec_range)+1:
        address_range.append(str(ip_low + i))
        i += 1
    return address_range




def convert_ranges_to_ip_list(host_list):
    result_list = []
    for host in host_list:
        if "-" in host:
            ip_range = host.split("-")
            #Проверяем метод указания диапазона, если второй элемент списка задан ip, приобразуем в объекты ipaddress
            if "." in ip_range[1]:
                #Вычесляем разницу между элементами диапазона
                ip_low = ipaddress.ip_address(ip_range[0])
                ip_hi = ipaddress.ip_address(ip_range[1])
                ip_difference = int(ip_hi) - int(ip_low)
                result_list.extend(ip_address_sequence_calculator(ip_low,ip_difference))
            else:
                ip_low = ipaddress.ip_address(ip_range[0])
                ip_difference = int(ip_range[1]) - int(ip_range[0].split(".")[3])
                result_list.extend(ip_address_sequence_calculator(ip_low,ip_difference))
        else:
            result_list.append(host)
    return result_list
        
if __name__ == "__main__":
    address_range = ['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']
    print(f"{convert_ranges_to_ip_list(address_range)}")