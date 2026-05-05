"""
№ 27636 Апробация 04.03.26 (Уровень: Базовый)
"""

with open("26_27636.txt") as f:
    s, n = map(int, f.readline().split())
    left = s
    data = tuple(map(int, f.readlines()))

c = 0
transported = 0
for i in sorted(data):
    if left >= i:
        left -= i
        transported += i
        c += 1
    else:
        break

print(n - c, sum(data) - transported)
