from enum import Enum


class Point:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __eq__(self, another_point) -> bool:
        eq_x = self.x == another_point.x
        eq_y = self.y == another_point.y

        return eq_x and eq_y


class Direction(Enum):
    LEFT = 'left'
    RIGHT = 'right'
    UP = 'up'
    DOWN = 'down'
