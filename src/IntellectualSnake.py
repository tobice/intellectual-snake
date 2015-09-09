import pygame
from pygame.locals import *

SQUARE_SIZE = 20
ROWS = 30
COLUMNS = 60

class IntellectualSnake:
    def __init__(self):
        self.running = True
        self.screen = pygame.display.set_mode((COLUMNS * SQUARE_SIZE, ROWS * SQUARE_SIZE))

        # Display The Background
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((250, 250, 250))

    def update(self, time):
        if time > 0:
            print("FPS: " + `(1.0/time)`)

        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                self.running = False

    def render(self):
        self.screen.blit(self.background, (0, 0))

    def isRunning(self):
        return self.running
