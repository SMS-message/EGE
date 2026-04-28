"""
№ 23561 Пересдача 03.07.25 (Уровень: Базовый)
"""

for A in range(1, 100_000_000):
    for x in range(1, 1000):
        if not ((x % 128 == 0) <= ((not (x % A == 0)) <= (not (x % 80 == 0)))):
            break
    else:
        print(A)
