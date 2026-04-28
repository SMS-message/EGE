"""
№ 25353 ЕГКР 13.12.25 (Уровень: Базовый)
"""


def to_base(x: int, base: int):
    lst = []

    while x:
        lst.append(x % base)
        x //= base

    return lst[::-1]

expr = 3 * 27 ** 9 + 2 * 27 ** 6 + 27 ** 3

for x in range(1, 27_001):
    if to_base(expr - x, 27).count(0) == 6:
        print(x)
        break
