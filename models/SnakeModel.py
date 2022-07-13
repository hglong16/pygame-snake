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
        image = pygame.Rect(round(self.pos.x), round(self.pos.y), SIZE, SIZE)
        pygame.draw.rect(self.parent_surface, self.color, image)


class Snake:

    def __init__(self, parent_surface, manager):
        self.parent_surface = parent_surface
        self.manager = manager
        self.head = Cube(50, 50, parent_surface)
        self.direction = Direction.RIGHT

    def draw(self):
        self.head.draw()

    def update(self):
        if self.direction == Direction.RIGHT:
            self.head.pos.x += self.manager.velocity * SIZE * self.manager.factor
        if self.direction == Direction.LEFT:
            self.head.pos.x -= self.manager.velocity * SIZE * self.manager.factor
        if self.direction == Direction.DOWN:
            self.head.pos.y += self.manager.velocity * SIZE * self.manager.factor
        if self.direction == Direction.UP:
            self.head.pos.y -= self.manager.velocity * SIZE * self.manager.factor
