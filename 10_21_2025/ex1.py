def f1(x: int,
       y: int,
       z: int, 
       w: int) -> int:
    return int(((z <= y) and ((not x) <= w)) <= ((z == w) or (y and (not x))))


for x in 0, 1:
    for y in 0, 1:
        for w in 0, 1:
            for z in 0, 1:
                f = f1(x, y, z, w)
                if not f:
                    print(y, z, w, x, "|", f)
