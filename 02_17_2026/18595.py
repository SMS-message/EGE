"""
№ 18595 (Уровень: Базовый)
"""

A = [x / 10 for x in range(2000)]

for x in range(2000):
    x /= 10
    f = (not ((48 <= x <= 94) or (83 <= x <= 100))) <= (not (x in A))
    if not f:
        A.remove(x)


print("[" + A[0].__str__(), end=", ")
for i, elem1 in enumerate(A):
    if i + 1 == len(A):
        break
    elem2 = A[i + 1]
    if elem2 - elem1 > 0.101:
        print(elem1.__str__() + "]", ";[" + elem2.__str__(), end=', ')

print(A[-1].__str__() + "]")
