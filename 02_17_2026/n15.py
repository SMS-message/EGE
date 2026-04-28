"""
№ 14660 Открытый курс "Слово пацана" (Уровень: Базовый)
"""

A = [x / 10 for x in range(1000)]

for x in range(1000):
    x /= 10

    f = ((x in A) <= (16 <= x <= 84) or (27 <= x <= 43))
    if not f:
        A.remove(x)

print("[" + A[0].__str__(), end=", ")
for i, elem1 in enumerate(A):
    if i + 1 == len(A):
        break
    elem2 = A[i + 1]

    if elem2 - elem1 > 0.11:
        print(elem2.__str__() + "];", "[" + elem1.__str__(), end=", ")

print(A[-1].__str__() + "]")
