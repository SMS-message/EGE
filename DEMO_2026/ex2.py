def f(x, y, z, w):
    return int((x or y) and not (y == z) and not w)


for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            for w in [0, 1]:
                f_res = f(x, y, z, w)
                if f_res == 1:
                    print(x, y, z, w, f_res)

# Ответ: zyxw
