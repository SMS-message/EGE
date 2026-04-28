"""
№ 24891 (Уровень: Базовый)
"""

import functools


@functools.lru_cache(maxsize=None)
def f(n: int):
    if n <= 10:
        return n
    return n - 7 + f(n - 21)

for i in range(1, 200_000):
    f(i)

print((f(185_734) - f(185_650)) // f(40))