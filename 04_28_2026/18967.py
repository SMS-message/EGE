"""
№ 18967 (Уровень: Средний)
"""

with open("26_18967.txt") as f:
    n, k = map(int, f.readline().split())
    data = tuple(map(lambda x: tuple(map(int, x.split())), f.readlines()))

stomp = 0
free = n
all_occ = []
clients = []
do_no_count = []

data = sorted(data, key=lambda x: x[1])

for i, t, num in data:
    if i in do_no_count:
        continue
    if i not in clients:
        if free >= num:
            free -= num
            clients.append(i)
            if free == 0:
                all_occ.append(t)
        else:
            stomp += num
            do_no_count.append(i)
    else:
        clients.remove(i)
        if free == 0:
            all_occ.append(t)
        free += num

lst = []
for i in range(0, len(all_occ), 2):
    lst.append(all_occ[i + 1] - all_occ[i])

print(stomp, max(lst))
