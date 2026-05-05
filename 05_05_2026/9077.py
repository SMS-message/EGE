"""
№ 9077 Danov2306 (Уровень: Сложный)
"""

with open("26_9077.txt") as f:
    m, n = map(int, f.readline().split())
    data = tuple(map(lambda x: tuple(map(int, x.split())), f.readlines()))

data = sorted(data)
stops = [[] for _ in range(m)]
day = []

for start, length, a, b in data:
    stops[a - 1].append((start, -1))
    stops[b - 1].append((start + length, 1))
    day.extend([[start, -1], [start + length - 1, 1]])
day.sort()

k = 0
for i in range(m):
    stops[i] = sorted(stops[i])
    min_n = 1
    cur_n = 0
    for t, n in stops[i]:
        cur_n += n
        min_n = min(min_n, cur_n)
    k += min_n if min_n < 0 else 0

print(-k)

min_n = 1
cur_n = 0
for t, n in day:
    cur_n += n
    min_n = min(min_n, cur_n)
print(-min_n)
