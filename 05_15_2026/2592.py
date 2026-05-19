"""
№ 2592 (Уровень: Гроб)
"""

def is_prime(x: int):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


for n in range(55_000_000, 60_000_000 + 1):
    a = n
    while a % 2 == 0:
        a //= 2
    if a == 1:
        continue
    if (a ** 0.25).is_integer():
        if is_prime(int(a ** 0.25)):
            print(n, a)
