import pygame
from .utl import Direction
from pygame.locals import *
from .StateModel import Manager

from .SnakeModel import Snake


class Game:

    def __init__(self):
        self.manager = Manager()
        pygame.init()
        pygame.display.set_caption("Hello Lanh")

        self.surface = pygame.display.set_mode((800, 800), 0)

        self.background = pygame.Surface(self.surface.get_size())
        self.background = self.background.convert()
        self.background.fill(("#d4f0f0"))

        font = pygame.font.Font(None, 36)
        text = font.render("Hello There", True, (10, 10, 10))
        text_pos = text.get_rect()
        text_pos.centerx = self.background.get_rect().centerx
        self.background.blit(text, text_pos)

        self.clock = pygame.time.Clock()

        self.snake = Snake(self.surface, self.manager)
        self.surface.blit(self.background, (0, 0))
        pygame.display.flip()

    # def render_bg(self):
    #     bg = pygame.image.load("src/self.background.jpeg")
    #     self.surface.blit(bg, (0, 0))
    #     pygame.display.flip()

    def check_input(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                # if event.key == K_ESCAPE:
                #     running = False

                # if event.key == K_RETURN:
                #     pygame.mixer.music.unpause()
                #     pause = False

                if event.key == K_LEFT:
                    self.snake.direction = Direction.LEFT

                if event.key == K_RIGHT:
                    self.snake.direction = Direction.RIGHT

                if event.key == K_UP:
                    self.snake.direction = Direction.UP

                if event.key == K_DOWN:
                    self.snake.direction = Direction.DOWN

            elif event.type == QUIT:
                self.manager.alive = False

    def run(self):
        while self.manager.alive:
            self.check_input()
            self.surface.blit(self.background, (0, 0))
            self.snake.update()
            self.snake.draw()
            pygame.display.flip()
            self.clock.tick(60)
