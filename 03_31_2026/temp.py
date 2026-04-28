"""
№ 27314 (Уровень: Средний)
"""


def f(start: int, stop: int):
    if start > stop or start in (28, 36):
        return 0
    if start == stop:
        return 1
    return f(start + 1, stop) + f(start + 5, stop) + f(start * 3, stop)


# 2 -> 49 + 18 | 30 - 28 - 36

print(f(2, 18) * f(18, 49) + f(2, 30) * f(30, 49) - f(2, 18) * f(18, 30) * f(30, 49))
