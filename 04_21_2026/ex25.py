def find_delimiters(x: int):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return [i, x // i]
    return [x]


def is_prime(x: int):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


i = 8_120_140 + 1
c = 0

while c < 5:
    dels = find_delimiters(i)
    m = 1
    if sum(map(is_prime, dels)) == 2:
        if sum(map(lambda x: str(x).count('2') == 2, dels)) == 2:
            m = dels[0] * dels[-1]

    if m == i:
        print(i, max(dels))
        c += 1
    i += 1
