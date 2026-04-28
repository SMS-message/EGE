"""
№ 21718 ЕГКР 19.04.25 (Уровень: Базовый)
"""

from fnmatch import fnmatch

if __name__ == '__main__':
    mask = "4*4736*1"
    dlmtr = 7993
    for i in range(dlmtr, 10 ** 10 + 1, dlmtr):
        if fnmatch(str(i), mask) and i % dlmtr == 0:
            print(i, i // dlmtr)

# 44736821 5597
# 4064736241 508537
# 4303247361 538377
# 4347368721 543897
# 4447361151 556407
# 4473658121 559697
# 4794736931 599867
