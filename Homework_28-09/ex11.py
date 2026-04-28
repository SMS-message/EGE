"""
№ 20814 Апробация 05.03.25 (Уровень: Базовый)
"""

from delimiters import Number


def find_r(n: Number | int):
    if isinstance(n, int):
        n = Number(n)
    return sum(n.delimiters[1:-1])


assert find_r(20) == 21

if __name__ == '__main__':
    counter = 0
    i = 500_000 + 1
    while counter < 5:
        r = find_r(i)
        if str(r)[-1] == "9":
            print(i, r)
            counter += 1
        i += 1

# 500014 250009
# 500038 495289
# 500040 1170359
# 500054 250029
# 500058 667289
