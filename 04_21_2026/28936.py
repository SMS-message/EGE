for A in range(1, 2_000_000):
    flag = False
    for x in range(480, 500):
        for y in range(5 * 480, 5 * 501):
            f = (x * y < A) or (5 * x < y) or (486 <= x)
            if not f:
                flag = True
                break
        if flag:
            break
    else:
        print(A)
        break