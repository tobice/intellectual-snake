import pygame
from src.constants import *

class DirectionControl(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        super(DirectionControl, self).__init__()
        self.image = pygame.Surface([SEGMENT_SIZE, SEGMENT_SIZE])
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()

        self.letter = ''
        self.direction = direction

        self.setHeadPosition(x, y)

    def setHeadPosition(self, x, y):
        self.rect.x = FIELD_MARGIN + x + self.direction[0] * SEGMENT_SIZE
        self.rect.y = FIELD_MARGIN + y + self.direction[1] * SEGMENT_SIZE

    def setLetter(self, letter):
        self.letter = letter

        # Paint the letter
        font = pygame.font.Font(None, 30)
        text = font.render(self.letter, True, WHITE)
        textRect = text.get_rect(centerx=SEGMENT_SIZE/2)

        self.image.fill((0, 0, 0))
        self.image.blit(text, textRect)
