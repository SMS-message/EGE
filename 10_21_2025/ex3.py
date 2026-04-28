def f3(x: int, y: int, z: int, w: int) -> int:
    return int(not (x <= z) or (y == w) or not y)


for x in 0, 1:
    for y in 0, 1:
        for w in 0, 1:
            for z in 0, 1:
                f = f3(x, y, z, w)
                if not f:
                    print(x, z, y, w, "|", f)
