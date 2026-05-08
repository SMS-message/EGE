"""
https://openfipi.devinf.ru/task/05BFA6
"""


with open("3_26.txt") as f:
    n, d = map(int, f.readline().split())
    data = tuple(map(lambda x: tuple(map(int, x.split())), f.readlines()))

s_data = sorted(data, reverse=True)

ls = []
max_l = 0
for start in range(len(s_data)):
    lst = [s_data[start]]

    for i in s_data[start + 1:]:
        if lst[-1][-1] != i[-1]:
            if lst[-1][0] - i[0] >= d:
                lst.append(i)
    ls.append(lst)

ans = max(ls, key=lambda x: (len(x), x[-1][0]))
print(len(ans), ans[-1][0])


