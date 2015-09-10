import pygame
from src.constants import *

class HudText(pygame.sprite.Sprite):
    def __init__(self, x, y, width, content):
        super(HudText, self).__init__()

        self.image = pygame.Surface([width, SEGMENT_SIZE])
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.setContent(content)

    def setContent(self, content):
        # Paint the text
        font = pygame.font.Font(None, 30)
        text = font.render(content, 1, (10, 10, 10))
        textRect = text.get_rect()

        self.image.fill(WHITE)
        self.image.blit(text, textRect)

