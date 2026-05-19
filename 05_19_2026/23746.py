from itertools import product

a = tuple(product(sorted("СТРОКА"), repeat=5))


for i, var in enumerate(a[::-1]):
    if (len(a) - i) % 2 == 0:
        if var[0] not in ("А", "С", "Т"):
            if var.count("О") == 2:
                print(len(a) - i)
                break


