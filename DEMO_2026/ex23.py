def func(start: int, end: int):
    if start < end or start == 7:
        return 0
    if start == end:
        return 1
    return func(start - 1, end) + func(start - 4, end) + func(start // 3, end)


print(func(19, 13))
print(func(13, 2))

# Ответ: 68
