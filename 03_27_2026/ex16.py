from functools import cache


@cache
def f(n: int | float):
    if n == 0:
        return 0
    if n % 3 == 0:
        return f(n / 3)
    return n % 3 + f(n - n % 3)


for i in range(1000):
    if f(i) == 11:
        print(i)
