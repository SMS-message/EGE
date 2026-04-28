from csv import reader

c = 0
with open("09 (2).csv") as csv_file:
    data = tuple(map(lambda x: tuple(map(int, x)), reader(csv_file)))

    for line in data:
        counts = dict()
        for i in line:
            count = line.count(i)
            if count in counts:
                counts[count].append(i)
            else:
                counts[count] = [i]

        if not (2 in counts and 1 in counts):
            continue
        if len(counts[2]) == 4 and len(counts[1]) == 2:
            if sum(set(counts[2])) < sum(counts[1]):
                c += 1

print(c)
