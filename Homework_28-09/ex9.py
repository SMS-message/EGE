"""
№ 21422 Досрочная волна 2025 (Уровень: Базовый)
"""

from delimiters import Number


def ends_with_seven(string: str):
    return string[-1] == "7"


if __name__ == '__main__':
    counter = 0
    i = 1_125_000 + 1
    while counter < 5:
        n = Number(i)
        try:
            x = min(filter(lambda x: ends_with_seven(str(x)) and x != i and x != 7, n.delimiters))
            print(i, x)
            counter += 1
        except ValueError:
            pass
        i += 1

# 1125003 467
# 1125006 97
# 1125009 17
# 1125011 3187
# 1125012 177
