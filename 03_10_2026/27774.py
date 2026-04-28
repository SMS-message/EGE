"""
№ 27774 Апробация 04.03.26 (Уровень: Базовый)
"""

import typing

GAME_OVER = 207


def game(
        heap1: int,
        heap2: int,
        win: list[int],
        _cur: int = 0,
        _func: typing.Callable = all
):
    if heap1 + heap2 >= GAME_OVER or _cur > max(win):
        return _cur in win

    _cur += 1

    moves = [
        game(heap1 + 1, heap2, win, _cur, _func),
        game(heap1 * 2, heap2, win, _cur, _func),
        game(heap1, heap2 + 1, win, _cur, _func),
        game(heap1, heap2 * 2, win, _cur, _func),
    ]

    if _cur % 2 == max(win) % 2:
        return any(moves)
    return _func(moves)


print("№19:", end=' ')
for s in range(1, 190):
    if game(17, s, [2], _func=any):
        print(s, end=" ")
        break

print("\n№20:", end=' ')
for s in range(1, 190):
    if not game(17, s, [1]) and game(17, s, [3]):
        print(s, end=" ")

print("\n№21:", end=' ')
for s in range(1, 190):
    if game(17, s, [2, 4]) and not game(17, s, [2]):
        print(s, end=' ')
        break
