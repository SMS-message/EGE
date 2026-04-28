GAME_OVER: int = 46


def game(
        heap: int,
        cur: int,
        win: list[int]
) -> bool:
    """

    :param heap: number of stones in heap at start;
    :param cur: current turn;
    :param win: list of win turns;
    :return: is it possible to win at these turns.
    """
    if heap >= GAME_OVER or cur > max(win):
        return cur in win
    cur += 1
    moves = [game(heap + 1, cur, win), game(heap * 3, cur, win)]

    if cur % 2 == max(win) % 2:
        return any(moves)
    return all(moves)


if __name__ == '__main__':
    # №19
    for i in range(1, GAME_OVER):
        if not game(i, 0, [1]) and game(i, 0, [2]):
            print(i)
            break

    # №20
    for i in range(1, GAME_OVER):
        if not game(i, 0, [1]) and game(i, 0, [3]):
            print(i, end=" ")
    print()

    # №21
    for i in range(1, GAME_OVER):
        if game(i, 0, [2, 4]) and not game(i, 0, [2]):
            print(i)
