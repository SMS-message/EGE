def f2(x: int, y: int, z: int, w: int) -> int:
    return int((not (x and y)) and (y or z) or (not w))


for x in 0, 1:
    for y in 0, 1:
        for w in 0, 1:
            for z in 0, 1:
                f = f2(x, y, z, w)
                if not f:
                    print(y, w, x, z, "|", f)
