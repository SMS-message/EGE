"""
№ 23382 Резервный день 19.06.25 (Уровень: Средний)
"""

from delimiters import Number


def has_one_two(string: str):
    return string.count("2") == 1


if __name__ == '__main__':
    counter = 0
    i = 6_651_220 + 1
    while counter < 5:
        n = Number(i)
        match len(n.delimiters) - 2:
            case 1:
                cond1 = n.delimiters[1] ** 2 == n
                cond2 = has_one_two(str(n.delimiters[1]))
                cond3 = Number(n.delimiters[1]).is_prime()
                if cond1 and cond2 and cond3:
                    print(i, n.delimiters[1])
                    counter += 1
            case 2:
                cond1 = n.delimiters[1] * n.delimiters[2] == n
                cond2 = has_one_two(str(n.delimiters[1])) and has_one_two(str(n.delimiters[2]))
                cond3 = Number(n.delimiters[1]).is_prime() and Number(n.delimiters[2]).is_prime()
                if cond1 and cond2 and cond3:
                    print(i, n.delimiters[2])
                    counter += 1
        i += 1

# 6651241 2579
# 6651262 3325631
# 6651286 3325643
# 6651314 3325657
# 6651347 289189
