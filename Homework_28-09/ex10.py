"""
№ 20969 (Уровень: Базовый)
"""

from fnmatch import fnmatch

if __name__ == '__main__':
    mask = "*192?3*68"
    dlmtr = 154682
    for i in range(dlmtr, 10 ** 11 + 1, dlmtr):
        if fnmatch(str(i), mask) and i % dlmtr == 0:
            print(i, i // dlmtr)

# 11419243968 73824
# 19253887268 124474
# 31922343068 206374
# 65519273468 423574
# 76192331468 492574
