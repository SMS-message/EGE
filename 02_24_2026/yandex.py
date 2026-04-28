import functools


@functools.lru_cache(None)
def f(n: int):
    if n <= 1000:
        return n ** (n ** 2)
    return n + 2 * f(n - 2) + 6 * f(n - 6)

for i in range(1, 1000):
    f(i)

print(f(1000))