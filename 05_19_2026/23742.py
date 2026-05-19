def find_r(n: int):
    bn = f"{n:b}"
    if n % 3 == 0:
        bn += bn[-3:]
    else:
        bn += f"{(n % 3) * 3:b}"

    return int(bn, 2)


assert find_r(12) == 100
assert find_r(4) == 19

for n in range(500):
    if (r := find_r(n)) >= 200:
        print(n, r)
        break