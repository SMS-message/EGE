def f(
        x: int,
        y: int,
        z: int,
        w: int,
):
    return int((x or y) and not (y == z) and not w)


for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                r = f(x, y, z, w)
                if r:
                    print(z, y, x, w, r)
