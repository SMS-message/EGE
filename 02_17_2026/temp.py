"""
№ 23753 Демоверсия 2026 (Уровень: Базовый)
"""


def to_int(num: list, base: int):
    res = 0

    for i, digit in enumerate(num[::-1]):
        res += digit * base ** i

    return res


for x in range(28, -1, -1):
    a = to_int([9, 2, 3, x, 8, 7, 4], 29)
    b = to_int([5, 2, 4, x, 6, 1, 5, 2], 29)

    if (a + b) % 28 == 0:
        print((a + b) // 28)
        break
