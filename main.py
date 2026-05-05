def find_d(x: int):
    lst = []
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            lst.append(i)
            lst.append(x // i)
    if not lst:
        return [x, 1]
    return lst

def f(x: int, depth: int = 0):
    depth += 1
    if x <= 0:
        return
    if depth >= end:
        return
    mnd, mxd = sorted(find_d(x))
    f(x - mnd, depth)
    f(x + mxd, depth)


end = 12
f(2)
