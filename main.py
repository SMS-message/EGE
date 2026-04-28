i = 10 ** 5

while True:
    if sum(map(int, list(str(i)))) * 15873 == i:
        print(i)
    i += 1
    if i > 10 ** 6:
        break