def f5(x: int, y: int, z: int, w: int) -> int:
    return int((x <= y) and (y <= z) and (z <= w))


for x in 0, 1:
    for y in 0, 1:
        for w in 0, 1:
            for z in 0, 1:
                f = f5(x, y, z, w)
                if f:
                    print(z, y, w, x, "|", f)
