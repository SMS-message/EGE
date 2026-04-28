def to_base(n: int, base: int):
    mods = []
    while n:
        mods.append(n % base)
        n //= base
    mods = mods[::-1]
    return mods


def find_r(n: int):
    t_n = to_base(n, 3)
    if n % 3 == 0:
        t_n += t_n[-2:]
    else:
        t_n.extend(to_base(sum(t_n) * 3, 3))

    return int("".join(map(str, t_n)), 3)


assert find_r(8) == 228
assert find_r(9) == 81

lst = []

for i in range(1, 10000):
    if (r := find_r(i)) > 275:
        if r % 2 == 0:
            lst.append(r)

print(min(lst))