import functools


def f(n: int):
    return 2 * (g(n - 3) + 8)

@functools.cache
def g(n: int):
    if n < 10:
        return 2 * n
    return g(n - 2) + 1



for i in range(16_000):
    f(i)

print(f(15548))