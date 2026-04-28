import typing


def to_vector(lst: typing.Iterable):
    for i in lst:
        if isinstance(i, list):
            yield from to_vector(i)
        else:
            yield i


def rec_fill(val: typing.Any, repeat: int = 1):
    if repeat < 1:
        return val
    yield from rec_fill(val, repeat - 1)


a = [[1, 2, 3], [[4, 5], [6, 7]], 8]

print(list(to_vector(a)))


print(*rec_fill(1, 1))