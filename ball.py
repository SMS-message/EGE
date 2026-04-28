from typing import Tuple, List
from dataclasses import dataclass

class Ball(object):
    def __init__(self,
                 material: str,
                 color: Tuple[int, int, int] | str,
                 radius: float | int):
        """
        Base class for ball

        :param material:
        :param color:
        :param radius:
        """
        self._m = material
        self._color = color
        self._r = radius

    def __add__(self, other) -> List:
        if isinstance(other, Ball):
            return [self, other]
        raise TypeError(f"unsupported operand type(s) for +: 'Ball' and '{type(other)}'")

    def __repr__(self) -> str:
        return f"Ball({self._m.__repr__()}, {self._color.__repr__()}, {self._r.__repr__()})"

    @property
    def color(self) -> str | Tuple[int, int, int]:
        return self._color

    @color.setter
    def color(self, value: Tuple[int, int, int] | str):
        if isinstance(value, Tuple | str | List):
            self._color = value
        else:
            raise TypeError("Wrong type for 'color' attribute, use 'Tuple[int, int, int]' or 'str' instead")

    @staticmethod
    def default_ball():
        """
        Creates a default Ball with params: \n
        - material: Rubber
        - color: #FF0000
        - radius: 5

        :return: Ball
        """
        return Ball("Rubber", "#FF0000", 5)

@dataclass
class Dot(object):
    color: Tuple[int, int, int] | str
    shape: str

class FootBall(Ball):
    def __init__(self,
                 material: str,
                 color: Tuple[int, int, int] | str,
                 radius: float | int,
                 num_of_dots: int,
                 dot_variant: Dot):
        super().__init__(material, color, radius)
        self._n_of_dots = num_of_dots
        self._dot_var = dot_variant

    def __repr__(self) -> str:
        ball_params = super().__repr__()[:-1]
        return ball_params + f", {self._n_of_dots}, {self._dot_var})"

    @staticmethod
    def make_football(other: Ball,
                      num_of_dots: int,
                      dot_variant: Dot):
        return FootBall(other._m, other.color, other._r, num_of_dots, dot_variant)

    @staticmethod
    def default_ball():
        return FootBall.make_football(Ball("Rubber", "#FFFFFF", 4), 10, Dot("#000000", "pentagon"))



def main() -> None:
    ball1 = Ball.default_ball()
    ball2 = Ball.default_ball()
    ball2.color = "#00FF00"

    print(ball1 + ball2)

    pile_of_balls = [Ball.default_ball() for _ in range(3)]
    for ball in pile_of_balls:
        print("Ball with color: {}".format(ball.color))

    my_football = FootBall.default_ball()

    print(my_football)


if __name__ == "__main__":
    main()
