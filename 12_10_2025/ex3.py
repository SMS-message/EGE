from csv import reader

c = 0
with open("Задание 9.csv") as csv_file:
    data = tuple(map(lambda x: tuple(map(int, x)), reader(csv_file)))

    for line in data:
        counts = dict()
        for i in line:
            count = line.count(i)
            if count in counts:
                counts[count].append(i)
            else:
                counts[count] = [i]

        if 4 in counts:
            if len(counts[1]) == 3:
                repeated = counts[4][0]
                avg = sum(counts[1]) / len(counts[1])
                if repeated > avg:
                    c += 1

print(c)
