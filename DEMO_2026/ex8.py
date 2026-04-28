from itertools import product
from numbers import *


def check(x: int, variant: list | tuple):
    cond1 = x % 2 == 0
    cond2 = variant[0] not in ["А", "С", "Т"]
    cond3 = variant.count("О") == 2

    return cond1 and cond2 and cond3


a = product(tuple(sorted("СТРОКА")), repeat=5)
for i, var in list(enumerate(a, 1))[::-1]:
    if check(i, var):
        print(i, var)
        break

# Ответ: 5058
