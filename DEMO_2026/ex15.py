P = range(25, 65)
Q = range(40, 115)


def check(x: int):
    return (x in P) <= (((x in Q) and not (x in A)) <= (not (x in P)))


if __name__ == '__main__':
    lst = []
    lim = 500
    for i in range(1000):
        lim_count = 0
        for j in range(1, 1000):
            A = range(i, j)
            for x in range(100):
                if not check(x):
                    lim_count += 1
                    break
            else:
                lst.append(A)
        if lim_count > lim:
            print(min(lst, key=len))
            quit(0)

# Ответ: 24
