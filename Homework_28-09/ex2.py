"""
№ 23763 Демоверсия 2026 (Уровень: Базовый)
"""

from delimiters import Number


def find_m(n: Number | int):
    if isinstance(n, int):
        n = Number(n)
    if n.is_prime():
        return 0
    del_lst = n.delimiters[1:-1]
    return min(del_lst) + max(del_lst)


if __name__ == '__main__':
    counter = 0
    i = 800_000 + 1
    while counter < 5:
        m = find_m(i)
        if str(m)[-1] == "4":
            print(i, m)
            counter += 1
        i += 1

# 800004 400004
# 800009 114294
# 800013 266674
# 800024 400014
# 800033 61554
