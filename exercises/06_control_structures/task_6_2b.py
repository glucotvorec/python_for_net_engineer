# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
while True:
    ip_address = input("Enter the ip address: ").split(".")
    #validation of entered values
    try:
        if len(ip_address) < 4 or len(ip_address) > 4:
            raise ValueError()
        for octet in ip_address:
            if octet.isalnum and int(octet) <= 255:
                continue
            else:
                raise ValueError()
                break
    except (ValueError):
        print("Неправильный IP-адрес")
    else:
        break
if int(ip_address[0]) <= 223 and int(ip_address[0]) != 0:
    print("unicast")
elif int(ip_address[0]) >= 224 and int(ip_address[0]) <= 239:
    print("multicast")
elif int(ip_address[0]) == 255 and int(ip_address[1]) == 255 and int(ip_address[2]) == 255 and int(ip_address[3]) == 255:
    print("local broadcast")
elif int(ip_address[0]) == 0 and int(ip_address[1]) == 0 and int(ip_address[2]) == 0 and int(ip_address[3]) == 0:
    print("unassigned")
else:
    print("unused")