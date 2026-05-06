"""
Задание 13 - IP адреса и маски

В этом задании обычно задан адрес сети и маска. Требуется определить количество адресов в сети, удовлетворяющих некоторым условиям
"""

# Код на kompege - 27625
from ipaddress import *

ip = ip_address('172.16.96.0')  # Создание IP
mask = ip_address('255.255.224.0')
net = ip_network(f'{ip}/{mask}', 0)  # Создание сети

# net[0] - адрес сети                    (net.network_address)
# net[-1] - широковещательный адрес сети (net.broadcast_address)

cnt = 0
for i in net:  # Перебор всех IP, находящихся в сети net
    i = f'{i:b}'  # Перевод в 2-СС
    if i.count('1') % 2 == 0:
        cnt += 1
print(cnt)
