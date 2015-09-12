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
        font = pygame.font.Font(FONT, FONT_SIZE)
        text = font.render(content, True, HUD_COLOR)
        textRect = text.get_rect()

        self.image.fill(BACKGROUND_COLOR)
        self.image.blit(text, textRect)

