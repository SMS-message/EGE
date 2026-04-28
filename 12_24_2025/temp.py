import math


class Cycling(object):
    def __init__(self, size: int):
        self.mtrx = [[x + y * size for x in range(1, 1 + size)] for y in range(size)]

    def get(self):
        mtrx = self.mtrx.copy()

        c = math.ceil(len(mtrx) / 2)

        for i, line in enumerate(mtrx):
            for j, val in enumerate(line):
                ...


    def __str__(self) -> str:
        return "\n".join(["\t".join(map(str, line)) for line in self.mtrx])



# [0, 0] -> [n / 2 + 0, n / 2 + 0]
# [0, 1] -> [n / 2 - 1, n / 2 - 1]
# [0, 2] -> [n / 2 - 1, n / 2 + 0]
# [0, 3] -> [n / 2 - 1, n / 2 + 1]
# [0, 4] -> [n / 2 + 0, n / 2 + 1]
# [0, 5] -> [n / 2 + 1, n / 2 + 1]
# [0, 6] -> [n / 2 + 1, n / 2 + 0]
# [0, 7] -> [n / 2 + 1, n / 2 - 1]
# [0, 8] -> [n / 2 + 0, n / 2 - 1]


cyc = Cycling(5)
print(cyc)
