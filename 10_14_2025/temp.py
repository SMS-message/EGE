def f1(*args: tuple[int]):
    x, y, z = args
    return (x <= y) and (y <= z)


def f2(*args: tuple[int]):
    x, y, z = args
    return (z or y) <= (x == z)


def f3(*args: tuple[int]):
    x, y, z = args
    return (not x or z) and (not x or not y or not z)


def f4(*args: tuple[int]):
    x, y, z = args
    return (not x and y and z) or (not x and y and not z) or (not x or not y or not z)


def f5(*args: tuple[int]):
    x, y, z, w = args
    return x and (y and z or y and not w or not z and not w)





for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                res = int(f5(x, y, z, w))
                if res:
                    print(y, w, z, x, res)