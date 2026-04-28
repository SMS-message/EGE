from csv import reader
from functools import cache


@cache
def in_transposed(n: int, col: int):
    return data_transposed[col].count(n) > 335


ans = 0
with open("09.csv") as csv_file:
    data = tuple(map(lambda x: tuple(map(int, x)), reader(csv_file)))
    data_transposed = tuple(zip(*data))

    for x, line in enumerate(data):
        c = 0
        avg = sum(line) / len(line)
        for y, i in enumerate(line):
            if line.count(i) == 1:
                if in_transposed(i, y):
                    if i < avg:
                        c += 1
        if c == 1:
            ans += 1

print(ans)
