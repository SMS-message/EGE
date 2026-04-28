def f(x: int, y: int, z: int, w: int):
    return int((w <= x) and (not (y and z)) and z)


for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                res = f(x, y, z, w)
                if res:
                    print(w, y, z, x, res)
