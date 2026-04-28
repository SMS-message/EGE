"""
№ 25279 (Уровень: Базовый)
"""

A = []

for x in range(5000):
    x /= 10
    f = (x not in A) <= ((66 <= x <= 67) or (x < 32 or x > 125) or (x < 30 or x > 491))
    if not f:
        A.append(x)

print(A[-1] - A[0] - 1)
