A = []

for x in range(0, 600):
    x /= 10
    if not ((not (x in A)) <= ((22 <= x <= 40) == (32 <= x <= 50))):
        A.append(x)


print(A[-1] - A[0])