import functools
import time


@functools.cache
def is_prime(n: int):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_d(n: int):
    lst = []
    flag = False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            if flag:
                return []
            lst.append(i)
            lst.append(n // i)
            flag = True
    return lst


i = 8_996_452 + 1
c = 0

t = time.time()
while c < 5:
    ds = find_d(i)
    if ds:
        if sum(map(lambda x: str(x).count("3") == 2, ds)) == 2:
            if sum(map(is_prime, ds)) == 2:
                print(i, max(ds))
                c += 1
    i += 1

print(time.time() - t)
