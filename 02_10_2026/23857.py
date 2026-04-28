"""
№ 23857 (Уровень: Базовый)
"""

import ipaddress

network = ipaddress.ip_network("192.168.12.207/255.192.0.0", strict=False)

for address in list(network)[::-1]:
    bin_address = f"{int("".join(map(lambda x: f"{x:b}", map(int, address.__str__().split(".")))), 2):032b}"
    if bin_address.count("1") == bin_address.count("0"):
        print(address.__str__().replace(".", ""))
        break
