def g(n: int):
    if n >= 5200:
        return n / 10 + 30
    return g(n + 1) - 0.5

def f(n):
    if n >= 67:
        return n
    return 3 * (g(n - 2) - 1)

print(f(10_007))