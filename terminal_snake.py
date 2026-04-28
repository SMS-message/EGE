from time import sleep
from argparse import ArgumentParser

COLORS = {
    "purple": '\033[95m',
    "cyan": '\033[96m',
    "blue": '\033[94m',
    "green": '\033[92m',
    "orange": '\033[93m',
    "red": '\033[91m',
    "white": "",
}

SLEEP_TIME: float
WIDTH: int
LENGTH: int
SYM: str
BG = " "


def setup():
    global SLEEP_TIME, WIDTH, LENGTH, SYM
    parser = ArgumentParser()
    parser.add_argument("-w", default=10, type=int)
    parser.add_argument("-l", default=10, type=int)
    parser.add_argument("-t", default=0.05, type=float)
    parser.add_argument("-s", default="*", type=str)
    parser.add_argument("-c", default="white", type=str)
    args = parser.parse_args()

    SLEEP_TIME = args.t
    WIDTH = args.w
    LENGTH = args.l
    SYM = args.s
    try:
        print(COLORS[args.c], end="")
    except KeyError:
        pass


def main() -> None:
    while True:
        try:
            for i in range(LENGTH):
                print(BG * i + SYM * WIDTH)
                sleep(SLEEP_TIME)
            for i in range(LENGTH, -1, -1):
                print(BG * i + SYM * WIDTH)
                sleep(SLEEP_TIME)
        except KeyboardInterrupt:
            quit(0)

if __name__ == '__main__':
    setup()
    main()
