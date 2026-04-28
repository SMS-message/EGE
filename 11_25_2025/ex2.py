def to_base(n: int, base: int):
    mods = []
    while n:
        mods.append(n % base)
        n //= base

    return mods[::-1]


def find_r(n: int):
    tn = to_base(n, 3)
    if n % 3 == 0:
        tn += tn[-2:]
    else:
        tn += to_base((n % 3) * 5, 3)
    return int("".join(map(str, tn)), 3)


assert find_r(11) == 307
assert find_r(12) == 111

if __name__ == '__main__':
    lst = []
    for i in range(1, 100):
        if (r := find_r(i)) > 133:
            lst.append(r)
    print(min(lst))