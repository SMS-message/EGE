A = []

for x in range(0, 1200):
    x /= 10

    if not ((25 <= x <= 64) <= (((40 <= x <= 115) and not (x in A)) <= (not (25 <= x <= 64)))):
        A.append(x)

print(A[-1] - A[0])
