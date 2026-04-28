def f4(x: int, y: int, z: int, w: int) -> int:
    return int((not x) and y or z and (not y) or (not z) and w)


for x in 0, 1:
    for y in 0, 1:
        for w in 0, 1:
            for z in 0, 1:
                f = f4(x, y, z, w)
                if not f:
                    print(x, y, z, w, "|", f)
