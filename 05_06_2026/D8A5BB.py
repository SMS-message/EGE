"""
https://openfipi.devinf.ru/task/D8A5BB
"""

with open("26.txt") as f:
    n, m = map(int, f.readline().split())
    masses = [int(f.readline().strip()) for i in range(n)]
    containers = [int(f.readline().strip()) for i in range(m)]

masses.sort(reverse=True)
containers.sort()

dct = {}

for container in containers:
    for mass in masses:
        if mass <= container:
            dct[container] = mass
            break

for container in containers:
    ...

print(dct)