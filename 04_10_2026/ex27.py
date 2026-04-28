import math
from itertools import product


def center(cl: list[tuple[float, float, str]]):
    lst = []
    for star in cl:
        s = 0
        for other_star in cl:
            s += math.dist(star[:-1], other_star[:-1])
        lst.append((s, star))
    return min(lst)[1]


with open("27_A_28766.txt") as f:
    data = tuple(map(lambda x: (*map(float, x.split()[:-1]), x.split()[-1]), f.readlines()))

red_giants = [star for star in data if star[-1][0] == "Y" and star[-1][-3:] == "III"]

a1, a2 = [], []

for star in data:
    if star[1] > 10:
        a1.append(star)
    else:
        a2.append(star)

ca1 = center(a1)

d = []

for red_giant in red_giants:
    d.append(math.dist(ca1[:-1], red_giant[:-1]))

print(min(d) * 10_000)
print(max(d) * 10_000)

with open("27_B_28766.txt") as f:
    data = tuple(map(lambda x: (*map(float, x.split()[:-1]), x.split()[-1]), f.readlines()))


b1, b2, b3 = [], [], []

for star in data:
    if star[1] > 24:
        b1.append(star)
    elif star[0] > 22:
        b2.append(star)
    else:
        b3.append(star)

c1, c2, c3 = map(center, [b1, b2, b3])

ymg_ds = set()
for i, cl in enumerate([b1, b2, b3], 1):
    yellow_mass_giants = []
    for star in cl:
        if star[-1][0] == "Z" and star[-1][-1] == "I" and len(star[-1]) == 3:
            yellow_mass_giants.append(star)
    for star1, star2 in product(yellow_mass_giants, repeat=2):
        ymg_ds.add(math.dist(star1[:-1], star2[:-1]))
    # print(f"b{i}: {len(yellow_mass_giants)}")
print(min(ymg_ds - {0.0}) * 10_000)
print(math.dist(c2[:-1], c3[:-1]) * 10_000)
