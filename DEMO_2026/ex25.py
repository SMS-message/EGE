from typing import Tuple


def find_delimiters(n: int) -> Tuple[int, int]:
    x = 0
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            x = i
            break
    try:
        if x == n // x:
            return x, 0
        return x, n // x
    except ZeroDivisionError:
        return 0, 0


def task1():
    counter = 0
    for i in range(800_000, 1_000_001):
        if counter >= 5:
            return
        M = sum(find_delimiters(i))
        if str(M)[-1] == "4":
            print(i, M)
            counter += 1


def task2():
    lst = []
    for_masks = []

    for i1 in range(10):
        for_masks.append(f"{i1}")
        for i2 in range(10):
            for_masks.append(f"{i1}{i2}")
            for i3 in range(10):
                for_masks.append(f"{i1}{i2}{i3}")

    for x in for_masks:
        for i1 in range(10):
            for i2 in range(10):
                mask = f"3{i1}12{i2}14{x}5"
                if int(mask) % 1917 == 0 and int(mask) <= 10 ** 10:
                    lst.append((int(mask), int(mask) // 1917))
    print(*map(lambda y: f"{y[0]} {y[-1]}", sorted(lst)), sep="\n")


def task2_alt():
    import fnmatch

    for i in range(0, 10 ** 10, 1917):
        if fnmatch.fnmatch(f"{i}", "3?12?14*5"):
            print(i, i // 1917)


if __name__ == '__main__':
    task1()
    print()
    task2_alt()
