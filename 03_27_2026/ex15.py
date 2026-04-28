A = []

for x in range(1100):
    x /= 10
    f = not (not (x in A) and (22 <= x <= 72)) or (42 <= x <= 102)
    if not f:
        A.append(x)

print(A[0])
for i, n1 in enumerate(A):
    if i + 1 == len(A):
        break
    n2 = A[i + 1]
    if n2 - n1 >= 0.101:
        print(n1, "|", n2)

print(A[-1])
