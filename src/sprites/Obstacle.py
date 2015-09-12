import pygame
from src.constants import *

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, word, orientation):
        super(Obstacle, self).__init__()

        # Calculate dimensions based on the word length and orientation
        dimensions = (len(word) * SEGMENT_SIZE, SEGMENT_SIZE)
        dimensions = dimensions if orientation == HORIZONTAL else tuple(reversed(dimensions))

        self.image = pygame.Surface((dimensions[0], dimensions[1]))
        self.image.fill(OBSTACLE_COLOR)
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
        self.word = word
        self.orientation = orientation

        self.currentPosition = 0

        self.renderWord()

    def renderWord(self):
        self.image.fill(OBSTACLE_COLOR)
        for i, letter in enumerate(self.word):
            self.renderLetter(letter,
                OBSTACLE_TYPED_LETTER_COLOR if i < self.currentPosition else OBSTACLE_LETTER_COLOR,
                i * SEGMENT_SIZE if self.orientation == HORIZONTAL else 0,
                i * SEGMENT_SIZE if self.orientation == VERTICAL else 0)

    def renderLetter(self, letter, color, x, y):
        # Paint the letter
        font = pygame.font.Font(None, int(1.2 * SEGMENT_SIZE))
        text = font.render(letter, True, color)
        textRect = text.get_rect(centerx=SEGMENT_SIZE/2)
        textRect.x += x
        textRect.y += y

        self.image.blit(text, textRect)

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
