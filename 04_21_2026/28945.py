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
