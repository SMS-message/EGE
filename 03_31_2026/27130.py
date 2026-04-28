"""
№ 27130 (Уровень: Средний)
"""


def f(start: int, stop: int):
    if start == stop:
        return 1
    if start < stop:
        return 0
    if int(str(start)[-2]) > int(str(start)[-1]):
        return f(start - 3, stop) + f(int(str(start)[:1] + str(start)[-1] + str(start)[-2]), stop)
    return f(start - 3, stop)


print(f(1001, 959) * f(959, 902))
