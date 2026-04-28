import typing

GAME_OVER: int = 75


def game(
        heap1: int,
        heap2: int,
        win: list[int],
        _cur: int = 0,
        _func: typing.Callable[[typing.Iterable[bool]], bool] = all
) -> bool:
    """
        :param heap1: number of stones in the first heap at start;
        :param heap2: number of stones in the second heap at start;
        :param win: list of win turns;
        :param _cur: current turn;
        :param _func: either all or any;
        :return: is it possible to win at these turns.
    """
    if heap1 + heap2 > 122:  # Из условия: если суммарное кол-во камней > 122, то выигрывает соперник
        return _cur % 2 != max(win) % 2
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


if __name__ == '__main__':
    # №19
    for s2 in range(1, 66 + 1):
        if game(8, s2, [2], _func=any):
            print(s2)
            break

    # №20
    for s2 in range(1, 66 + 1):
        if not game(8, s2, [1]) and game(8, s2, [3]):
            print(s2, end=' ')
    print()

    # №21
    ...
