import pygame
from src.constants import *

class Segment(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Segment, self).__init__()
        self.image = pygame.Surface([SEGMENT_SIZE, SEGMENT_SIZE])
        self.image.fill(SNAKE_COLOR)
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
