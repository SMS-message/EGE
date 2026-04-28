with open("DEMO_17.txt") as f:
    data = tuple(map(int, f.readlines()))

n_min = min(filter(lambda x: len(str(x).strip("-")) == 2, data))

lst = []

for i, n1 in enumerate(data):
    if i + 1 == len(data):
        break
    n2 = data[i + 1]
    m = map(lambda x: len(str(x).strip("-")) == 2, [n1, n2])
    if sum(m) == 1:
        if (n1 + n2) % n_min == 0:
            lst.append(n1 + n2)

print(len(lst), max(lst))
