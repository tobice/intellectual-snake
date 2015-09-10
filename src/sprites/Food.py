import pygame
from src.constants import *

class Food(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Food, self).__init__()
        self.image = pygame.Surface([SEGMENT_SIZE, SEGMENT_SIZE])
        self.image.fill(FOOD_COLOR)
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
