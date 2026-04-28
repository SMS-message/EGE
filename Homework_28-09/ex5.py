"""
№ 23282 Основная волна 11.06.25 (Уровень: Средний)
"""

from delimiters import Number


def find_m(n: Number | int):
    if isinstance(n, int):
        n = Number(n)
    if n.is_prime():
        return 0
    del_lst = [j for j in n.delimiters[1:-1] if Number(j).is_prime()]
    if del_lst:
        return min(del_lst) + max(del_lst)
    return 0


assert find_m(298) == 151

if __name__ == '__main__':
    counter = 0
    i = 5_400_000 + 1
    while counter < 5:
        m = find_m(i)
        if m > 60_000 and str(m)[::-1] == str(m):
            print(i, m)
            counter += 1
        i += 1

# 5400042 900009
# 5400420 90009
# 5400866 158851
# 5406116 1351531
# 5406420 90109
