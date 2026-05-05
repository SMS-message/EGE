"""
№ 27779 Апробация 04.03.26 (Уровень: Базовый)
"""

with open("26_27779.txt") as f:
    n = int(f.readline())
    data = tuple(map(int, f.readlines()))

s_data = sorted(set(data), reverse=True)
max_lst = []

for i in range(len(s_data)):
    lst = [s_data[i]]
    for j in range(i + 1, len(s_data)):
        if lst[-1] - s_data[j] >= 8:
            lst.append(s_data[j])
    max_lst = max(lst, max_lst, key=len)

print(len(max_lst), max_lst[-1])
