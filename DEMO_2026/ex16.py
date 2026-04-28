from sys import setrecursionlimit


def f(n: int):
    return 2 * (g(n - 3) + 8)


def g(x: int):
    if x < 10:
        return 2 * x
    return g(x - 2) + 1


setrecursionlimit(10_000)
print(f(15_548))

# Ответ: 15588
