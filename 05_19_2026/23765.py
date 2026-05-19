with open('26_23765.txt') as f:
    n = int(f.readline())
    data = tuple(map(lambda x: tuple(map(int, x.split())), f.readlines()))

lst = []
already_found = []
top = []
bottom = []

for i, datum in enumerate(data, 1):
    keep, exp_date = datum
    lst.append([keep, 0, i])
    lst.append([exp_date, 1, i])

lst.sort()

for t, tp, i in lst:
    if i in already_found:
        continue
    if tp == 0:
        top.append(i)
        already_found.append(i)
        last_i = i
    else:
        bottom.append(i)
        already_found.append(i)
        last_i = i

print(last_i)
rating = top + bottom[::-1]
print(len(rating) - rating.index(last_i) - 1)