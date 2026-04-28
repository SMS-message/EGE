"""
https://inf-ege.sdamgia.ru/problem?id=2231
"""

import ipaddress


net = ipaddress.ip_network("162.198.0.157/255.255.255.224", strict=False)

print(list(map(lambda ip: str(ip), net)).index("162.198.0.157"))
