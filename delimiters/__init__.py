class Number(int):
    def __init__(self, num: int):
        self.n = num
        self.delimiters = []
        self.find_delimiters()

    def __int__(self):
        return self.n

    def find_delimiters(self):
        for i in range(1, int(self.n ** 0.5 + 1)):
            if self.n % i == 0:
                self.delimiters.append(i)
        self.delimiters = sorted(set(self.delimiters + [self.n // i for i in self.delimiters][::-1]))

    def is_prime(self) -> bool:
        return len(self.delimiters) == 2
