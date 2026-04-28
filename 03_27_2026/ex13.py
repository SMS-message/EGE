import ipaddress

net = ipaddress.ip_network("135.12.170.217/255.255.248.0", strict=False)

print(net)