import pygame
from src.constants import *

class DirectionControl(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        super(DirectionControl, self).__init__()
        self.image = pygame.Surface([SEGMENT_SIZE, SEGMENT_SIZE])
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.letter = ''
        self.direction = direction

    def setLetter(self, letter):
        self.letter = letter

        # Paint the letter
        font = pygame.font.Font(None, 30)
        text = font.render(self.letter, 1, (10, 10, 10))
        textRect = text.get_rect(centerx=SEGMENT_SIZE/2)

        self.image.fill(WHITE)
        self.image.blit(text, textRect)
