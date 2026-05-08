import functools
import itertools


@functools.cache
def is_prime(x: int):
    for d in range(2, int(x ** 0.5) + 1):
        if x % d == 0:
            return False
    return True


start = 1_411_111_115
stop = start + 12 + 1

for i in range(start, stop):
    if i == 1_411_111_120:
        continue
    if sum(map(int, list(str(i)))) % 3 != 0:
        for p in itertools.permutations(str(i)):
            if i != int(''.join(p)) and is_prime(int(''.join(p))):
                print(i)
                break


