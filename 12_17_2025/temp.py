class NaturalNumber:
    def __init__(self, num: int | None | float | complex):
        self.n = num

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.n})"

    def __add__(self, other):
        res = self.n + other.n
        init = other if issubclass(other.__class__, self.__class__) else self
        return init.__class__(res)

    def __sub__(self, other):
        res = self.n - other.n
        init = other if issubclass(other.__class__, self.__class__) else self
        if res > 0:
            return init.__class__(res)
        return init.__class__(None if init is self else res)


class Integer(NaturalNumber):
    pass


class RealNumber(Integer):
    pass


class ComplexNumber(RealNumber):
    pass
