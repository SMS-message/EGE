with open("26_25363.txt") as f:
    n = int(f.readline())
    s = []
    for i, line in enumerate(f, start=1):
        t_w, t_a = map(int, line.split())
        s.append((t_w, i, "W"))
        s.append((t_a, i, "A"))

    print(s)

    s.sort()
    r1, r2 = [], []
    last_i = None
    for t, i, tt in s:
        if i in r1 or i in r2:
            continue
        if tt == "W":
            r1.append(i)
            last_i = i
        else:
            r2.insert(0, i)
            last_i = i

r = r1 + r2
print(last_i, n - r.index(last_i) - 1)
