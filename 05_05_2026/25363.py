"""
№ 25363 ЕГКР 13.12.25 (Уровень: Базовый)
"""

with open('26_25363.txt') as f:
    n = int(f.readline())
    data = tuple(map(lambda x: tuple(map(int, x.split())), f.readlines()))

lst = []

for i, datum in enumerate(data, 1):
    standby, active = datum
    lst.append((standby, 's', i))
    lst.append((active, 'a', i))

lst.sort()

top = []
bottom = []
last_i = 0

for tm, tp, i in lst:
    if i in top + bottom:
        continue
    if tp == 's':
        top.append(i)
    else:
        bottom.insert(0, i)
    last_i = i

rating = top + bottom
print(last_i, len(rating[rating.index(last_i) + 1:]))

