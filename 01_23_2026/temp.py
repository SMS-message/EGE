GAME_OVER: int = 46


def game(
        heap1: int,
        heap2: int,
        win: list[int],
        _cur: int = 0,
) -> bool:
    """

        :param heap1: number of stones in first heap at start;
        :param heap2: number of stones in second heap at start;
        :param _cur: current turn;
        :param win: list of win turns;
        :return: is it possible to win at these turns.
        """
    if heap1 + heap2 >= GAME_OVER or _cur > max(win):
        return _cur in win

    _cur += 1

    heap1, heap2 = min(heap1, heap2), max(heap1, heap2)
    moves = [game(heap1 + i, heap2, win, _cur) for i in range(1, heap1 + 1)]

    if _cur % 2 == max(win) % 2:
        return any(moves)
    return all(moves)


if __name__ == '__main__':
    # №19
    n = []
    for s1 in range(1, 100):
        for s2 in range(1, 100):
            if game(s1, s2, [1]):
                n.append((s1, s2))
    print(min(n))

    # №20
    n = []
    s1 = 5
    for s2 in range(1, 41):
        if not game(s1, s2, [1]) and game(s1, s2, [3]):
            n.append(s2)
    print(min(n), max(n))

    # №21
    s1 = 5
    for s2 in range(1, 41):
        if game(s1, s2, [2, 4]) and not game(s1, s2, [2]):
            print(s2)
            break
