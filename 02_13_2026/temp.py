"""
https://inf-ege.sdamgia.ru/problem?id=60255
"""

import ipaddress

def b(n):
    return f"{int(n):08b}"

net = ipaddress.ip_network("192.168.32.160/255.255.255.240", strict=False)
c = 0

for ip in net:
    str_ip = str(ip)
    if "".join([b(i) for i in str_ip.split('.')]).count("1") % 2 == 0:
        c += 1

print(c)
