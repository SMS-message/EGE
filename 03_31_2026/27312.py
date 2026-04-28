"""
№ 27312 (Уровень: Средний)
"""

def f(
        start: int,
        stop: int
):
    if start < stop:
        return 0
    if start == stop:
        return 1
    return f(start - 1, stop) + f(start // 2, stop) + f(start // 3, stop)

# 106 -> 6, - 48 | - 61

f106_61 = f(106, 61)
f106_48 = f(106, 48)
f61_48 = f(61, 48)

print(f106_48 )