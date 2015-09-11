import pygame
from src.constants import *

class Head(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Head, self).__init__()
        self.image = pygame.Surface([SEGMENT_SIZE, SEGMENT_SIZE])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE) # Head is transparent
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.direction = RIGHT
        self.stepProgress = 0
        self.moved = False

    def changeDirection(self, direction):
        if direction == self.direction:
            return False

        # U-turn is not allowed
        if [sum(x) for x in zip(direction, self.direction)] == [0, 0]:
            return False

        self.direction = direction
        return True

    def update(self, time):
        self.stepProgress += time

        if self.stepProgress > STEP_DURATION:
            self.stepProgress = 0
            self.rect.x = (self.rect.x + (self.direction[0] * SEGMENT_SIZE)) % FIELD_WIDTH
            self.rect.y = (self.rect.y + (self.direction[1] * SEGMENT_SIZE)) % FIELD_HEIGHT
            self.moved = True
        else:
            self.moved = False
