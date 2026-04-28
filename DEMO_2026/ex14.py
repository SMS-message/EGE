def task_1():
    a = 2 * 2187 ** 2020 + 729 ** 2021 - 2 * 243 ** 2022 + 81 ** 2023 - 2 * 27 ** 2024 - 6561
    b = []

    while a:
        b.append(a % 27)
        a //= 27

    print(sum(map(lambda x: x > 9, b)))


def task_2():
    alp = list("01234567890abcdefghijklmnopqr")
    for x in alp[::-1]:
        v = int(f"923{x}874", 29) + int(f"524{x}6152", 29)
        if v % 28 == 0:
            print(x, v // 28)
            break


def task3():
    a = 9 * 11 ** 210 + 8 * 11 ** 150
    for x in range(3000, 0, -1):
        i = a - x
        lst = []
        while i:
            lst.append(i % 11)
            i //= 11
        if lst.count(0) == 60:
            print(x)
            break


if __name__ == '__main__':
    task_1()
    task_2()
    task3()
