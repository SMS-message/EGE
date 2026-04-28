"""
№ 25348 (Уровень: Базовый)
"""

from csv import reader

count = 0
with open('9_25348.csv') as csv_file:
    data = map(lambda x: tuple(map(int, x)), reader(csv_file))
    for line in data:
        dct = {}
        for i in line:
            if (c := line.count(i)) in dct:
                dct[c].append(i)
            else:
                dct[c] = [i]

        if 3 in dct and 1 in dct:
            if len(dct[1]) == 4:
                if max(line) in dct[1]:
                    count += 1

print(count)
