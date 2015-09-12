import pygame
from src.constants import *

class BonusWord(pygame.sprite.Sprite):
    def __init__(self, x, y, word):
        super(BonusWord, self).__init__()

        self.image = pygame.Surface((150 + SEGMENT_SIZE * len(word), SEGMENT_SIZE))
        self.image.fill(BACKGROUND_COLOR)
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
        self.word = word

        self.currentPosition = 0

        self.renderWord()

    def renderWord(self):
        self.image.fill(BACKGROUND_COLOR)
        offset = self.renderLetter("BONUS word: ", OBSTACLE_LETTER_COLOR, 0)
        for i, letter in enumerate(self.word):
            offset += self.renderLetter(letter,
                OBSTACLE_TYPED_LETTER_COLOR if i < self.currentPosition else OBSTACLE_LETTER_COLOR,
                offset)

    def renderLetter(self, letter, color, x):
        # Paint the letter
        font = pygame.font.Font(None, int(1.2 * SEGMENT_SIZE))
        text = font.render(letter, True, color)
        textRect = text.get_rect()
        textRect.x += x

        self.image.blit(text, textRect)
        return text.get_width()

    def typeLetter(self, letter):
        if self.currentPosition >= len(self.word):
            self.currentPosition = 0  # shouldn't happen

        if self.word[self.currentPosition] == letter:
            self.currentPosition += 1
        else:
            self.currentPosition = 0

        self.renderWord()

        # Return True when we reach the end of the word
        return self.currentPosition == len(self.word)
