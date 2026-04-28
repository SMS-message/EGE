from csv import reader

c = 0
with open("09.csv") as csv_file:
    data = tuple(map(lambda x: tuple(map(int, x)), reader(csv_file)))

    for line in data:
        dct = dict()
        for i in line:
            count = line.count(i)
            if count in dct:
                dct[count].append(i)
            else:
                dct[count] = [i]
        if max(dct) >= 3 and 1 in dct:
            avg1 = sum(dct[1]) / len(dct[1])
            lst = []
            for i in dct:
                if i != 1:
                    lst.extend(dct[i])
            if avg1 > (sum(lst) / len(lst)):
                c += 1
print(c)
