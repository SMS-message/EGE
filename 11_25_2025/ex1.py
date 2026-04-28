def find_r(n: int):
    bn = f"{n:b}"
    bn = bn[1:]
    if bn.count("1") % 2 == 0:
        bn = "10" + bn
    else:
        bn = "1" + bn
        bn += "0"

    return int(bn, 2)


assert find_r(4) == 8
assert find_r(6) == 12


if __name__ == '__main__':
    lst = []
    for i in range(1000000, 1, -1):
        if (r := find_r(i)) < 450:
            lst.append(r)
    print(max(lst))
