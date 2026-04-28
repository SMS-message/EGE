A = []

for x in range(1500):
    x /= 10
    f = (25 <= x <= 64) <= (((40 <= x <= 115) and not (x in A)) <= (not (25 <= x <= 64)))
    if not f:
        A.append(x)

print("[" + A[0].__str__(), end=", ")
for i, elem1 in enumerate(A):
    if i + 1 == len(A):
        break
    elem2 = A[i + 1]
    if elem2 - elem1 > 0.101:
        print(elem1.__str__() + "];", "[" + elem2.__str__(), end=', ')

print(A[-1].__str__() + "]")