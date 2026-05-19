"""
№ 28945 ЕГКР 18.04.26 (Уровень: Базовый)
"""

def first():
    with open('26_28945.txt') as f:
        n = int(f.readline())
        data = tuple(map(lambda x: tuple(map(int, x.split())), f.readlines()))

    data = sorted(map(lambda x: (x[0], x[0] + x[-1]), data), key=lambda x: x[-1])

    completed = [data[0]]

    for i, datum in enumerate(data[1:], 1):
        start, end = datum
        if start >= completed[-1][-1]:
            completed.append(data[i])
            data[i] = None

    lst = []

    for i in range(n - data[::-1].index(None), n):
        start, end = data[i]
        if start >= completed[-2][-1]:
            lst.append(10_000 - end)

    print(len(completed), min(lst))

def second():
    with open("26_28945.txt") as f:
        n = int(f.readline())
        data = tuple(map(lambda x: tuple(map(int, x.split())), f.readlines()))

    data = sorted(map(lambda x: [x[0], x[0] + x[1]], data), key=lambda x: x[-1])

    last = 0
    path = []

    for i, datum in enumerate(data):
        start, end = datum
        if start >= last:
            path.append((start, end))
            last = end

    print(len(path), end=" ")

    for start, end in data[-10:]:
        if start >= path[-2][1] and (start, end) not in path:
            print(10_000 - end)
            break

if __name__ == '__main__':
    second()