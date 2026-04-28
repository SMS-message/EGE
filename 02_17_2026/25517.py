"""
№ 25517 (Уровень: Средний)
"""

def to_base(x: int, base: int):
    lst = []

    while x:
        lst.append(x % base)
        x //= base

    return lst[::-1]


value = (16 ** 350 * (15 * 3 - 29) ** (4 ** (2 + 5)) + 1007) // 63

print(to_base(value, 4).count(1))
