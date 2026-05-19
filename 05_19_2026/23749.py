import math

K = 2783

n = 3_845_627

for N in range(1, 2 ** 14):
    if math.ceil(math.ceil(math.log2(N)) * K / 8) * n >= 11 * 1024 * 1024 * 1024:
        print(N)
        break