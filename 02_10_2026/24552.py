"""
№ 24552 (Уровень: Средний)
"""

import ipaddress

network = ipaddress.ip_network("202.71.92.91/255.255.192.0", strict=False)

for address in list(network)[-2:0:-1]:
    c = 0
    octets = tuple(map(int, address.__str__().split(".")))
    for octet in octets:
        if octet % 2 != 0:
            c += 1

    if c == 2:
        print("".join(map(str, octets)))
        break
