from itertools import product


class Device:
    def __init__(self, n: int):
        self.lst = [True] * n

    def append(self, arg: str):
        match arg:
            case "X":
                self.lst.append(False)
            case "O":
                self.lst.append(True)

    def remove(self, ind: int):
        del self.lst[ind]

    def change(self, ind: int):
        self.lst[ind] = not self.lst[ind]

    def find_working(self) -> list[int]:
        indexes = []
        for i, elem in enumerate(self.lst):
            if elem:
                indexes.append(i)

        return indexes

    def find_variants(self, indexes: list[int], num_of_broken: int) -> list[str]:
        lst = []

        # Сколько можно поставить в итоге
        final_num = num_of_broken - (len(self.lst) - sum(self.lst))
        # Количество мест
        places = sum(self.lst)

        a = product([True, False], repeat=places)
        a = filter(lambda x: len(x) - sum(x) == final_num, a)

        for i in a:
            pattern = self.lst[:]
            for ind, elem in zip(indexes, i):
                pattern[ind] = elem
            lst.append("".join(map(lambda x: "O" if x else "X", pattern)))

        return lst

    def __call__(self, arg: int, mode: int = 1) -> tuple[int] | list[str]:
        indexes = self.find_working()
        res = self.find_variants(indexes, arg)
        if mode:
            return (len(res),)
        return res

    def __str__(self) -> str:
        return "".join(map(lambda x: "O" if x else "X", self.lst))


if __name__ == '__main__':
    dev = Device(6)
    print(dev)
    dev.change(3)
    print(dev)
    dev.remove(4)
    print(dev)
    print()
    print(*dev(3, mode=0), sep='\n')
