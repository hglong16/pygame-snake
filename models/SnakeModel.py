import pygame
from pygame.locals import *
from .utl import Point, Direction
from .Constants import SIZE


class Cube:

    def __init__(self, x, y, parent_surface, color="#FF986a"):
        self.parent_surface = parent_surface
        self.pos = Point(x, y)
        self.color = color

    def draw(self):
        image = pygame.Rect(
            round(self.pos.x) * SIZE,
            round(self.pos.y) * SIZE, SIZE, SIZE)
        print(self.pos.x, round(self.pos.x))
        print(self.pos.y, round(self.pos.y))
        pygame.draw.rect(self.parent_surface, self.color, image)


class Snake:

    def __init__(self, parent_surface, manager):
        self.parent_surface = parent_surface
        self.manager = manager
        self.head = Cube(1, 1, parent_surface)
        self.direction = Direction.RIGHT

    def draw(self):
        self.head.draw()

    def update(self):
        if self.direction == Direction.RIGHT:
            self.head.pos.x += 1 * self.manager.factor
        if self.direction == Direction.LEFT:
            self.head.pos.x -= 1 * self.manager.factor
        if self.direction == Direction.DOWN:
            self.head.pos.y += 1 * self.manager.factor
        if self.direction == Direction.UP:
            self.head.pos.y -= 1 * self.manager.factor
