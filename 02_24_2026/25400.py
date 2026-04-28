import functools


@functools.lru_cache(None)
def f(n: int):
    if n < 31054:
        return f(n + 4) + 3020
    return 3 * (g(n - 2) - 15)


@functools.lru_cache(None)
def g(n: int):
    if n >= 28:
        return g(n - 5) - 15
    return 3 * n - 4


for i in range(1, 100_000):
    g(i)

for i in range(100_000, 1, -1):
    f(i)

print(f(15))
