def f(n: int):
    if n >= 19:
        return f(n - 4) + 3580
    return n

def g(n: int):
    if n >= 248045:
        return n / 20 + 28
    return g(n + 9) - 4




print(6 * (g(f(673) - 7) - 36))