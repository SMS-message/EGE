"""
https://inf-ege.sdamgia.ru/problem?id=3784
"""

import ipaddress

net = ipaddress.ip_network("226.185.90.162/255.255.252.0", strict=False)

print(list(map(lambda ip: str(ip), net)).index("226.185.90.162"))
