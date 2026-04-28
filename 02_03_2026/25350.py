from math import log2, ceil

"""
№ 25350 (Уровень: Базовый)
"""

l = 105
n = 65_536
I0 = 7 * 2 ** 20

for N in range(1, 100_000):
    I = ceil(log2(N)) * l
    I_bytes = ceil(I / 8)

    if I_bytes * n > I0:
        print(N)
        break