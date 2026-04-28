for A in range(100_000):
    boolean = True
    for x in range(1, 40):
        for y in range(78100, 78200):
            boolean *= (78125 != 4 * x + y) or (A > x) and (A > y)
            if not boolean:
                break
        if not boolean:
            break

    if boolean:
        print(A)
        break
