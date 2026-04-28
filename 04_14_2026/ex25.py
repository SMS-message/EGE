def find_divisors(x: int):
    lst = []
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            lst.append(i)
            lst.append(x // i)
    return set(lst)

i = 700_000 + 1
c = 0

while c < 5:
    divs = find_divisors(i) - {7}
    f = tuple(filter(lambda x: str(x)[-1] == "7", divs))
    if f:
        print(i, min(f))
        c += 1
    i += 1