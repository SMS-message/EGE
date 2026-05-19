"""
№ 20970 (Уровень: Средний)
"""

with open("26_20970.txt") as f:
    n, k = map(int, f.readline().split())
    data = tuple(map(lambda x: tuple(map(int, x.split())), f.readlines()))

data = sorted(data, key=lambda x: x[0] + x[1])
tickets = [[] for i in range(k + 1)]

q = []

c = 0

def find_queue(arr, start):
    lst = [9999]
    for event in arr:
        lst.append(abs(event[0] - start))
    arr.sort()
    index = lst.index(min(lst))
    queue = sum(map(lambda x: x[-1], arr[:index]))
    print(arr, start)
    return abs(queue)

for start, duration, num in data:
    if num == 0:
        dct = {}
        for i, master in enumerate(tickets[1:], 1):
            queue = find_queue(master, start)
            if queue in dct:
                continue
            else:
                dct[queue] = i
        index = dct[min(dct)]
        if find_queue(tickets[index], start) < 5:
            tickets[index].append((start, -1))
            tickets[index].append((start + duration, 1))
        else:
            c += 1
    elif find_queue(tickets[num], start) < 5:
        tickets[num].append((start, -1))
        tickets[num].append((start + duration, 1))
    else:
        c += 1

print(max(map(len, tickets)))
print(c)
print(tickets[1])
