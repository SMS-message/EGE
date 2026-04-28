"""
№ 27629 Апробация 04.03.26 (Уровень: Базовый)
"""

with open("17_27629.txt") as file:
    data = tuple(map(int, file.readlines()))

f = filter(lambda x: str(x)[-2:] == "43" and str(x).strip("-").__len__() == 4, data)
max_n = max(f)

lst = []

for i, val1 in enumerate(data):
    if i + 1 == len(data):
        break

    val2 = data[i + 1]
    if any(map(lambda x: 1 if str(x).strip("-").__len__() == 4 else 0, [val1, val2])):
        if (val2 + val1) ** 2 < max_n ** 2:
            lst.append((val1 + val2) ** 2)

print(len(lst), max(lst))
