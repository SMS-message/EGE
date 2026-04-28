from turtle import *

m = 20


def init():
    left(90)
    screensize(2000, 2000)
    speed(0)


def main():
    for _ in [0] * 6:
        forward(13 * m)
        right(90)
        forward(15 * m)
        right(90)
    up()
    forward(4 * m)
    right(90)
    forward(6 * m)
    left(90)

    down()
    for _ in [0] * 6:
        forward(29 * m)
        right(90)
        forward(22 * m)
        right(90)
    up()
    for x in range(6, 16):
        for y in range(4, 14):
            goto(x * m, y * m)
            dot(10, "red")



if __name__ == '__main__':
    init()
    main()
    print(14 * 16 + 30 * 23 - 100)
    done()
