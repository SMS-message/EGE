def main():
    from csv import reader

    with open("demo_2025_9.csv") as csv_file:
        rd = reader(csv_file)

        data = tuple(map(lambda x: tuple(map(int, x)), rd))
        data = tuple(enumerate(data, 1))[::-1]

        for j, line in data:
            if len(set(line)) == 4:
                n = 0
                for i in line:
                    if line.count(i) == 3:
                        n = i

                unic = set(line) - {n}
                avg = (sum(unic) / len(unic))

                if j == 24959:
                    print(unic)
                    print(line, avg, n)
                    break
                if n > avg:
                    print(j)
                    break


def solution():
    f = open('demo_2025_9.csv')
    number = 0
    otv = []
    for s in f:
        number += 1
        m = [int(x) for x in s.split(",")]
        p3 = [x for x in m if m.count(x) == 3]
        n = [x for x in m if m.count(x) == 1]
        if len(p3) == 3 and len(n) == 3:
            if (sum(p3)) > (sum(n)):
                otv.append(number)
    print(max(otv))


if __name__ == '__main__':
    main()
