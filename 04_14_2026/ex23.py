def f(
        start: int,
        end: int
):
    if start == 7:
        return 0
    if start > end:
        return 0
    if start == end:
        return 1
    return f(start + 1, end) + f(start + 3, end) + f(start * 2, end)


print(f(2, 15) * f(15, 25))
