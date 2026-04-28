"""
№ 23207 Основная волна 10.06.25 (Уровень: Средний)
"""

from delimiters import Number


def has_one_five(string: str):
    return string.count("5") == 1


if __name__ == '__main__':
    counter = 0
    i = 1_324_727 + 1
    while counter < 5:
        n = Number(i)
        match len(n.delimiters) - 2:
            case 1:
                cond1 = n.delimiters[1] ** 2 == n
                cond2 = has_one_five(str(n.delimiters[1]))
                cond3 = Number(n.delimiters[1]).is_prime()
                if cond1 and cond2 and cond3:
                    print(i, n.delimiters[1])
                    counter += 1
            case 2:
                cond1 = n.delimiters[1] * n.delimiters[2] == n
                cond2 = has_one_five(str(n.delimiters[1])) and has_one_five(str(n.delimiters[2]))
                cond3 = Number(n.delimiters[1]).is_prime() and Number(n.delimiters[2]).is_prime()
                if cond1 and cond2 and cond3:
                    print(i, n.delimiters[2])
                    counter += 1
        i += 1

# 1324795 264959
# 1324801 1151
# 1324903 2543
# 1325015 265003
# 1325029 5279
