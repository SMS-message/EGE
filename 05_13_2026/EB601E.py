"""
https://openfipi.devinf.ru/task/EB601E
"""

with open("355_26.txt") as f:
    n, k = map(int, f.readline().split())
    data = list(map(lambda x: tuple(map(int, x.split())), f.readlines()))

candidates = []

for i, n1, n2, n3, speech in data:
    candidates.append([n1 + n2 + n3 + speech, speech, i])

candidates.sort(reverse=True, key=lambda x: (x[0], x[1], -x[-1]))

top = candidates[:k]

half_pass_i_cand = list(map(lambda x: x[1] + x[2] + x[3] + x[4], data)).count(top[-1][0])
if half_pass_i_cand > 1:
    half_pass_i = top[-1][0]
    for i in range(len(top) - 1, -1, -1):
        if top[i][0] != half_pass_i:
            pass_i = top[i][0]
            break

last_in_top = top[len(top) - list(map(lambda x: x[0], top[::-1])).index(pass_i) - 1][-1]
print(last_in_top, 0 if half_pass_i_cand == 1 else half_pass_i_cand)
