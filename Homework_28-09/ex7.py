"""
№ 21909 Открытый вариант 2025 (Уровень: Базовый)
"""

from delimiters import Number


def find_r(n: Number | int):
    if isinstance(n, int):
        n = Number(n)
    return sum(n.delimiters)


assert find_r(20) == 42

if __name__ == '__main__':
    counter = 0
    i = 500_000 + 1
    while counter < 5:
        r = find_r(i)
        if str(r)[-1] == "6":
            print(i, r)
            counter += 1
        i += 1

# 500032 1070356
# 500035 606816
# 500039 501456
# 500050 949716
# 500052 1333696
