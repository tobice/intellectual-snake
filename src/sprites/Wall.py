import pygame
from src.constants import *

class Wall(pygame.sprite.Sprite):
    """ Transparent rectangle working as an obstacle marking up the field"""
    def __init__(self, x, y, width, height):
        super(Wall, self).__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
