from ipaddress import ip_network


net = ip_network("191.128.66.83/255.192.0.0", strict=False)

print(tuple(net.hosts())[-1])