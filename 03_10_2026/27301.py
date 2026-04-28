"""
№ 27301 (Уровень: Средний)
"""

with open("17_27301.txt") as file:
    data = tuple(map(int, file.readlines()))

max_n = max(filter(lambda x: x.__str__()[:2] == "45", data))

lst = []

for i, val1 in enumerate(data):
    if i + 2 == len(data):
        break

    val2 = data[i + 1]
    val3 = data[i + 2]

    if sum(map(lambda x: bool(x < 0), [val1, val2, val3])) == 1:
        s = sum([val1, val2, val3])
        if s >= max_n:
            lst.append(s)

print(len(lst), min(filter(lambda x: str(x)[-2:] == "45", lst)))
