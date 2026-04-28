from math import lcm


def find_divs(x: int):
    lst = []

    for d in range(2, int(x ** 0.5) + 1):
        if x % d == 0:
            lst.append(d)
            lst.append(x // d)

    return sorted(set(lst))

def is_prime(x: int):
    for d in range(2, int(x ** 0.5) + 1):
        if x % d == 0:
            return False
    return True

B = find_divs(211)

for y in range(2, 10_000):
    C = find_divs(y)
    for x in range(1, 1000):
        f = ((x in B) or (not ( 35 <= x <= 99))) <= (x not in C)
        if not f:
            break
    else:
        if C:
            print(y, len(C))