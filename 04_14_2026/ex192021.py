def game(
        heap1: int,
        heap2: int,
        win: list[int],
        _cur: int = 0,
        _func=all
):
    if heap1 + heap2 >= 65 or _cur > max(win):
        return _cur in win

    _cur += 1

    moves = [
        game(heap1 + 1, heap2, win, _cur),
        game(heap1, heap2 + 1, win, _cur),
        game(heap1 * 3, heap2, win, _cur),
        game(heap1, heap2 * 3, win, _cur),
    ]

    if _cur % 2 == max(win) % 2:
        return any(moves)
    return _func(moves)


for s in range(1, 58 + 1):
    if game(6, s, [2], _func=any):
        print(s)
        break

for s in range(1, 58 + 1):
    if not game(6, s, [1]) and game(6, s, [3]):
        print(s, end=" ")
print()

for s in range(1, 58 + 1):
    if game(6, s, [2, 4]) and not game(6, s, [2]):
        print(s)
