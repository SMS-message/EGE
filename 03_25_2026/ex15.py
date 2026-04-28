"""
https://inf-ege.sdamgia.ru/problem?id=76230
"""

A = []

for x in range(2000):
    x /= 10
    f = (not (x in A)) <= (((23 <= x <= 42) and (7 <= x <= 68)) <= (x in A))
    if not f:
        A.append(x)
print(A)

print(A[0])
for i, n1 in enumerate(A):
    if i + 1 == len(A):
        break
    n2 = A[i + 1]
    if n2 - n1 >= 0.11:
        print(n1, "|", n2)
print(A[-1])
