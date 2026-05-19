import csv

with open("9_29341.csv") as f:
    data = tuple(map(lambda x: tuple(map(int, x)), csv.reader(f)))

c = 0
for line in data:
    s_line = sorted(line)
    if s_line[-1] < sum(s_line[:3]):
        if min(line) + max(line) != sum(s_line[1:3]):
            c += 1

print(c)
