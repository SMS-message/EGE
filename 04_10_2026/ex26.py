with open("26_17643.txt") as f:
    n = int(f.readline())
    data = tuple(map(lambda x: tuple(map(int, x.split())), f.readlines()))

dct = {}
s = 0

for key, price, available in data:
    s += price
    if key not in dct:
        dct[key] = [0, price, 0, key]
    if available:
        dct[key][2] -= 1
    else:
        dct[key][0] += 1

sales_leader = max(x for x in dct.values() if x[1] > s / n)

print(sales_leader[0] * sales_leader[1])
print(abs(sales_leader[2]))
