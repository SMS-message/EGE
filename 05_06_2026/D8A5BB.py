"""
https://openfipi.devinf.ru/task/D8A5BB
"""

with open("1_26.txt") as f:
    n, m = map(int, f.readline().split())
    masses = [int(f.readline().strip()) for _ in range(n)]
    containers = [int(f.readline().strip()) for _ in range(m)]

masses.sort(reverse=True)
containers.sort()

packed = []

for mass in masses:
    for container in containers:
        if container >= mass:
            packed.append([container, mass])
            containers.remove(container)
            break

print(len(packed), max(map(lambda x: x[-1], packed)))