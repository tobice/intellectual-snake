import pygame
from pygame.locals import *
from constants import *
from Head import *

class IntellectualSnake:
    def __init__(self):
        self.running = True
        self.screen = pygame.display.set_mode((COLUMNS * SEGMENT_SIZE, ROWS * SEGMENT_SIZE))

        # Display The Background
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((250, 250, 250))

        self.head = Head(SEGMENT_SIZE * COLUMNS / 2, SEGMENT_SIZE * ROWS / 2)

    def update(self, time):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                self.running = False
            elif event.type == KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.head.goLeft()
                if event.key == pygame.K_RIGHT:
                    self.head.goRight()
                if event.key == pygame.K_UP:
                    self.head.goUp()
                if event.key == pygame.K_DOWN:
                    self.head.goDown()

        self.head.update(time)

    def render(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.head.image, self.head.rect)

    def isRunning(self):
        return self.running
