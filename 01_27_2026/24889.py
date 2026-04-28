import csv


count = 0
with open("9_24889.csv") as csv_file:
    data = tuple(map(lambda x: tuple(map(int, x)), csv.reader(csv_file)))

    for line in data:
        dct = {}

        for i in line:
            if (c := line.count(i)) in dct:
                dct[c].append(i)
            else:
                dct[c] = [i]

        if 1 in dct:
            for i in 3, 4:
                if i in dct:
                    if max(line) in dct[i]:
                        if len(dct[1]) == 8 - i:
                            min1, max1 = min(dct[1]), max(dct[1])
                            sum_m_m = min1 + max1
                            sum1 = sum(set(dct[1]) - {min1, max1})
                            if sum_m_m <= sum1:
                                count += 1

print(count)
