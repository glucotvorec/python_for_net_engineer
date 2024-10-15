# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping (запуск ping через subprocess).
IP-адрес считается доступным, если выполнение команды ping отработало с кодом 0 (returncode).
Нюансы: на Windows returncode может быть равен 0 не только, когда ping был успешен,
но для задания нужно проверять именно код. Это сделано для упрощения тестов.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
import subprocess

def ping_ip_addresses(host_list):

    """Данная функция принемает в качестве аргумента список ip адресов
    и используя системную утилиту ping проверяет доступность хостов. 
    Возвращает кортеж из двух списков, Alive and Dead Host"""

    alive_host = []
    dead_host = []
    result = ()
    for host in host_list:
        ping_result = subprocess.run(["ping", "-c", "3", host], stdout=subprocess.DEVNULL)
        if ping_result.returncode == 0:
            alive_host.append(host)
        else:
            dead_host.append(host)
    result = (alive_host, dead_host)
    return result


if __name__ == "__main__":
    host_list = ["127.0.0.1", "1.1.1.1", "192.168.1.1", "169.127.15.15"]
    print(f"{ping_ip_addresses(host_list)}")
