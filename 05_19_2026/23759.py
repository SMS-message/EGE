import math


def game(
        heap: int,
        win: list[int],
        _cur: int = 0
):
    if heap <= 30 or _cur > max(win):
        return _cur in win

    _cur += 1

    moves = [
        game(heap - 3, win, _cur),
        game(heap - 5, win, _cur),
        game(math.floor(heap / 4), win, _cur)
    ]


    if _cur % 2 == max(win) % 2:
        return any(moves)
    return all(moves)

for s in range(31, 31 + 100):
    if not game(s, [1]) and game(s, [2]):
        print(s)
        break

for s in range(31, 31 + 100):
    if not game(s, [1]) and game(s, [3]):
        print(s, end=' ')

print()

for s in range(31, 31 + 300):
    if game(s, [2, 4]) and not game(s, [2]):
        print(s)
        break
