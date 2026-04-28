"""
№ 23283 Основная волна 11.06.25 (Уровень: Базовый)
"""

with open("26_23283.txt") as f:
    K = int(f.readline())
    N = int(f.readline())

    data = tuple(map(lambda x: tuple(map(int, x.split())), f.readlines()))

mfc = [[] for i in range(K)]
c = 0

for t1, t2 in data:
    for i in range(K):
        if not mfc[i] or mfc[i][-1][-1] < t1:
            mfc[i].append((t1, t2))
            c += 1
            break

print(sorted(enumerate(mfc, 1), key=lambda x: x[-1][-1][0], reverse=True)[0][0])
print(c)
