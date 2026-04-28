import functools


@functools.lru_cache(None)
def f(n: int):
    if n == 0:
        return 6
    if n % 2 == 0:
        return 1 + f(n // 2)
    return f(n // 2)


c = 0

for i in range(1, 1_000_000_000):
    if f(i) == 9:
        c += 1

print(c)
