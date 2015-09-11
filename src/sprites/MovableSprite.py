import pygame
from src.constants import *

class MovableSprite(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y):
        super(MovableSprite, self).__init__()
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.targetX = x
        self.targetY = y

    def moveTo(self, targetX, targetY):
        self.targetX = targetX
        self.targetY = targetY

    def moveInDirection(self, direction, distance=SEGMENT_SIZE):
        self.moveTo(
            self.rect.x + direction[0] * distance,
            self.rect.y + direction[1] * distance)

    def update(self, time):
        if abs(self.rect.x - self.targetX) > SEGMENT_SIZE:
            self.rect.x = self.targetX
        if abs(self.rect.y - self.targetY) > SEGMENT_SIZE:
            self.rect.y = self.targetY

        speed = SEGMENT_SIZE / STEP_DURATION

        # Because of the discrete nature (after all, we are updating the position frame by frame) it
        # might happen that a coordinate goes actually beyond its target. We must avoided that
        # because it would cause unwanted collisions on the game field

        if self.rect.x > self.targetX:
            self.rect.x = max(self.targetX, self.rect.x - speed * time)
        elif self.rect.x < self.targetX:
            self.rect.x = min(self.targetX, self.rect.x + speed * time)

        if self.rect.y > self.targetY:
            self.rect.y = max(self.targetY, self.rect.y - speed * time)
        elif self.rect.y < self.targetY:
            self.rect.y = min(self.targetY, self.rect.y + speed * time)
