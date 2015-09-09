import pygame
from constants import *

class Head(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Head, self).__init__()
        self.image = pygame.Surface([SEGMENT_SIZE, SEGMENT_SIZE])
        self.image.fill(SNAKE_COLOR)
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.direction = RIGHT
        self.stepProgress = 0

    def goUp(self):
        self.direction = UP

    def goDown(self):
        self.direction = DOWN

    def goLeft(self):
        self.direction = LEFT

    def goRight(self):
        self.direction = RIGHT

    def update(self, time):
        self.stepProgress += time

        if self.stepProgress > STEP_DURATION:
            self.stepProgress = 0
            self.rect.x = (self.rect.x + (self.direction[0] * SEGMENT_SIZE)) % FIELD_WIDTH
            self.rect.y = (self.rect.y + (self.direction[1] * SEGMENT_SIZE)) % FIELD_HEIGHT
        else:
            pass

        print(self.rect.x)

