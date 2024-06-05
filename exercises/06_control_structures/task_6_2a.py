# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
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